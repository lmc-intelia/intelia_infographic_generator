#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai>=1.0.0",
#     "pillow>=10.0.0",
#     "pyyaml>=6.0",
# ]
# ///
"""iig3d: 3D corporate-family infographics through Google Nano Banana Pro.

One file, sectioned in the order of the design: catalogue, routing, refs, spec, aspect,
palette, prompt, creds, render, add, docs, check, cli. Every subcommand prints exactly one
JSON object on stdout; diagnostics go to stderr.
"""

from __future__ import annotations

import argparse
import colorsys
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

import yaml

SKILL_ROOT = Path(__file__).resolve().parents[1]
SUBCOMMANDS = ["list", "route", "refs", "prompt", "render", "add", "docs", "check", "palette"]


class UsageError(Exception):
    """Bad input: exit code 1, message on stdout as JSON."""


# --- catalogue ---

MEMBER_PREFIX = "3d-"


@dataclass
class Member:
    raw: dict

    @property
    def name(self) -> str:
        return self.raw["name"]

    @property
    def items(self) -> dict:
        return self.raw["items"]

    @property
    def aspect_default(self) -> str:
        return self.raw["aspect_default"]

    @property
    def prompt_fragment(self) -> str:
        return self.raw["prompt_fragment"]

    @property
    def refs(self) -> list[dict]:
        return self.raw["refs"]

    @property
    def pairings(self) -> dict[str, list[str]]:
        return self.raw["pairings"]

    @property
    def alternates(self) -> list[str]:
        return self.raw["alternates"]


@dataclass
class Catalogue:
    root: Path
    family: dict
    schema: dict
    members: dict[str, Member] = field(default_factory=dict)

    @property
    def routing(self) -> dict[str, dict]:
        return self.family["routing"]

    @property
    def layouts(self) -> list[str]:
        return list(self.routing)

    def member(self, name: str) -> Member:
        try:
            return self.members[name]
        except KeyError:
            raise UsageError(f"unknown member {name!r}; valid: {', '.join(sorted(self.members))}") from None

    def ref_path(self, member: str, ref: dict) -> Path:
        return self.root / "refs" / member / ref["file"]


def read_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(data, handle, sort_keys=False, allow_unicode=True, width=120)


def load_catalogue(root: Path | None = None) -> Catalogue:
    root = Path(root or SKILL_ROOT)
    cat_dir = root / "catalogue"
    cat = Catalogue(root=root, family=read_yaml(cat_dir / "family.yaml"), schema=read_yaml(cat_dir / "schema.yaml"))
    for path in sorted((cat_dir / "members").glob("*.yaml")):
        raw = read_yaml(path)
        problems = validate_member(raw, cat.schema)
        if problems:
            raise UsageError(f"{path.name}: " + "; ".join(problems))
        cat.members[raw["name"]] = Member(raw)
    return cat


_TYPES = {"str": str, "int": int, "list": list, "map": dict}


def _check_type(value, spec, where: str, problems: list[str]) -> None:
    """Walk one schema node: a bare type name or {type, keys|items|values}."""
    if isinstance(spec, str):
        expected = _TYPES[spec]
        if not isinstance(value, expected):
            problems.append(f"{where}: expected {spec}, got {type(value).__name__}")
        return
    kind = spec["type"]
    if kind == "enum":
        if value not in spec["values"]:
            problems.append(f"{where}: expected one of {spec['values']}, got {value!r}")
        return
    if not isinstance(value, _TYPES[kind]):
        problems.append(f"{where}: expected {kind}, got {type(value).__name__}")
        return
    if kind == "map" and "keys" in spec:
        for key, sub in spec["keys"].items():
            if key not in value:
                problems.append(f"{where}.{key}: missing")
            else:
                _check_type(value[key], sub, f"{where}.{key}", problems)
    if kind == "list" and "items" in spec:
        for index, item in enumerate(value):
            _check_type(item, spec["items"], f"{where}[{index}]", problems)


def validate_member(raw: dict, schema: dict) -> list[str]:
    """Problems with a member record against schema.yaml `member`; empty when valid."""
    problems: list[str] = []
    for key, spec in schema["member"].items():
        if key not in raw:
            problems.append(f"{key}: missing")
        else:
            _check_type(raw[key], spec, key, problems)
    return problems


# --- routing ---

UMBRELLA = "industrial-3d"
DEFAULT_LAYOUT = "bento-grid"


@dataclass
class Route:
    member: str
    layout: str
    alternates: list[str]
    reason: str
    style: str = UMBRELLA

    def as_dict(self) -> dict:
        return {
            "member": self.member,
            "layout": self.layout,
            "style": self.style,
            "alternates": list(self.alternates),
            "reason": self.reason,
        }


def route(cat: Catalogue, layout: str | None, style: str | None) -> Route:
    """Resolve (layout, style) to a family member.

    Explicit 3d-* style wins; a 3d-* layout names its own member; otherwise the family routing
    table maps a general layout to its primary member. Style omitted or `industrial-3d` both
    mean "route by layout".
    """
    if style and style != UMBRELLA:
        if style not in cat.members:
            raise UsageError(f"unknown style {style!r}; valid: {UMBRELLA}, {', '.join(sorted(cat.members))}")
        member = cat.member(style)
        return Route(style, layout or style, list(member.alternates), f"explicit member style {style}", style)
    if layout is None:
        layout = DEFAULT_LAYOUT
    if layout in cat.members:
        member = cat.member(layout)
        return Route(layout, layout, list(member.alternates), f"device layout {layout} names its member")
    if layout not in cat.routing:
        raise UsageError(f"unknown layout {layout!r}; valid: {', '.join(cat.layouts)} or a 3d-* member name")
    row = cat.routing[layout]
    return Route(row["primary"], layout, list(row["alternates"]), f"routing table: {layout} -> {row['primary']}")


# --- spec ---

SPEC_KEYS = {
    "title",
    "subtitle",
    "language",
    "layout",
    "style",
    "aspect",
    "palette_css",
    "palette_vars",
    "items",
    "stats",
    "notes",
    "refs",
}
ITEM_KEYS = {"label", "detail", "icon", "value"}


@dataclass
class Item:
    label: str
    detail: str = ""
    icon: str | None = None
    value: str | None = None


@dataclass
class Spec:
    title: str
    items: list[Item]
    subtitle: str = ""
    language: str = "en"
    layout: str | None = None
    style: str | None = None
    aspect: str | None = None
    palette_css: Path | None = None
    palette_vars: list[str] = field(default_factory=list)
    stats: list[dict] = field(default_factory=list)
    notes: str = ""
    refs: list[Path] = field(default_factory=list)
    path: Path | None = None


def _str(value) -> str:
    return "" if value is None else str(value)


def load_spec(path: Path) -> Spec:
    """Parse the YAML content spec; unknown keys and missing title/items/label fail by name."""
    path = Path(path)
    raw = read_yaml(path)
    if not isinstance(raw, dict):
        raise UsageError(f"{path}: spec must be a mapping")
    unknown = sorted(set(raw) - SPEC_KEYS)
    if unknown:
        raise UsageError(f"{path}: unknown key(s) {', '.join(unknown)}; allowed: {', '.join(sorted(SPEC_KEYS))}")
    if not raw.get("title"):
        raise UsageError(f"{path}: missing title")
    items_raw = raw.get("items")
    if not isinstance(items_raw, list) or not items_raw:
        raise UsageError(f"{path}: items must be a non-empty list")
    items: list[Item] = []
    for index, entry in enumerate(items_raw):
        if not isinstance(entry, dict) or not entry.get("label"):
            raise UsageError(f"{path}: items[{index}] missing label")
        extra = sorted(set(entry) - ITEM_KEYS)
        if extra:
            raise UsageError(f"{path}: items[{index}] unknown key(s) {', '.join(extra)}")
        items.append(
            Item(
                label=_str(entry["label"]),
                detail=_str(entry.get("detail")),
                icon=entry.get("icon"),
                value=None if entry.get("value") is None else _str(entry["value"]),
            )
        )
    base = path.resolve().parent
    css = raw.get("palette_css")
    return Spec(
        title=_str(raw["title"]),
        items=items,
        subtitle=_str(raw.get("subtitle")),
        language=_str(raw.get("language")) or "en",
        layout=raw.get("layout"),
        style=raw.get("style"),
        aspect=None if raw.get("aspect") is None else _str(raw["aspect"]),
        palette_css=(base / css).resolve() if css else None,
        palette_vars=[str(v) for v in raw.get("palette_vars") or []],
        stats=[dict(s) for s in raw.get("stats") or []],
        notes=_str(raw.get("notes")),
        refs=[(base / r).resolve() for r in raw.get("refs") or []],
        path=path.resolve(),
    )


# --- aspect ---

RATIO_RE = re.compile(r"^(\d+(?:\.\d+)?):(\d+(?:\.\d+)?)$")


def _ratio_value(ratio: str) -> float:
    match = RATIO_RE.match(ratio.strip())
    if not match or float(match.group(1)) == 0 or float(match.group(2)) == 0:
        raise UsageError(f"aspect {ratio!r} is not a W:H ratio or one of landscape, portrait, square")
    return float(match.group(1)) / float(match.group(2))


def snap_aspect(cat: Catalogue, aspect: str | None, member_default: str) -> tuple[str, str | None]:
    """Return (supported ratio, original when snapped). Presets and None use the family map."""
    presets = cat.family["aspect_map"]
    if aspect is None:
        return presets[member_default], None
    if aspect in presets:
        return presets[aspect], None
    supported = cat.family["supported_ratios"]
    if aspect in supported:
        return aspect, None
    target = _ratio_value(aspect)
    nearest = min(supported, key=lambda r: abs(_ratio_value(r) - target))
    return nearest, aspect


def orientation(cat: Catalogue, ratio: str) -> str:
    return "portrait" if ratio in cat.family["portrait_ratios"] else "landscape"


# --- refs ---


def _ordered_pool(member: Member, layout: str) -> list[dict]:
    """Pairing refs for the layout first (falling back to the first pairing), then every other ref."""
    by_id = {r["id"]: r for r in member.refs}
    pairing = member.pairings.get(layout) or next(iter(member.pairings.values()), [])
    pool = [by_id[rid] for rid in pairing if rid in by_id]
    pool += [r for r in member.refs if r not in pool]
    return pool


def select_refs(
    cat: Catalogue,
    member_name: str,
    layout: str,
    user_refs: list[Path] | None = None,
    style_refs: bool = True,
) -> list[Path]:
    """Pairing refs for the layout (2 to 3), padded from the member pool when short, with the
    flag rules applied: never two watermarks, never only low-res refs, clean refs first.
    User refs are appended; the total is capped by family ref_rules.max_total."""
    rules = cat.family["ref_rules"]
    low, high = rules["per_render"]
    member = cat.member(member_name)
    picked: list[dict] = []
    if style_refs:
        pool = _ordered_pool(member, layout)
        pairing_len = len(member.pairings.get(layout) or next(iter(member.pairings.values()), []))
        picked = pool[: min(high, max(pairing_len, 0))]
        rest = [r for r in pool if r not in picked]
        rest.sort(key=lambda r: ("clean" not in r["flags"], "low-res" in r["flags"]))
        while len(picked) < low and rest:
            picked.append(rest.pop(0))
        seen_watermark = False
        kept: list[dict] = []
        for ref in picked:
            if "watermark" in ref["flags"]:
                if seen_watermark:
                    continue
                seen_watermark = True
            kept.append(ref)
        picked = kept
        while len(picked) < low and rest:
            candidate = rest.pop(0)
            if "watermark" in candidate["flags"] and seen_watermark:
                continue
            seen_watermark = seen_watermark or "watermark" in candidate["flags"]
            picked.append(candidate)
        if picked and all("low-res" in r["flags"] for r in picked):
            extra = next((r for r in rest if "low-res" not in r["flags"] and not ("watermark" in r["flags"] and seen_watermark)), None)
            if extra:
                picked.append(extra)
        picked.sort(key=lambda r: "clean" not in r["flags"])
    paths: list[Path] = []
    for ref in picked:
        path = cat.ref_path(member.name, ref)
        if not path.is_file():
            raise UsageError(f"reference image missing: {path}")
        paths.append(path)
    for extra_path in user_refs or []:
        extra_path = Path(extra_path)
        if not extra_path.is_file():
            raise UsageError(f"reference image not found: {extra_path}")
        paths.append(extra_path)
    return paths[: rules["max_total"]]


# --- palette ---

PALETTE_MIN, PALETTE_MAX = 3, 8
CSS_VAR_RE = re.compile(r"--([A-Za-z0-9_-]+)\s*:\s*([^;}]+)")
COLOUR_RE = re.compile(r"#[0-9A-Fa-f]{8}\b|#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3,4}\b|rgba?\([^)]*\)|hsla?\([^)]*\)")


@dataclass(frozen=True)
class Colour:
    name: str
    hex: str

    def as_dict(self) -> dict:
        return {"name": self.name, "hex": self.hex}


def _nums(body: str) -> list[float]:
    return [float(n) for n in re.findall(r"-?\d+(?:\.\d+)?", body)]


def normalise_colour(value: str) -> str | None:
    """Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour."""
    value = value.strip()
    if value.startswith("#"):
        digits = value[1:]
        if len(digits) in (3, 4):
            digits = "".join(ch * 2 for ch in digits[:3])
        elif len(digits) == 8:
            digits = digits[:6]
        elif len(digits) != 6:
            return None
        return "#" + digits.upper()
    lower = value.lower()
    if lower.startswith("rgb"):
        nums = _nums(value[value.index("(") + 1 :])
        if len(nums) < 3:
            return None
        r, g, b = (max(0, min(255, round(n))) for n in nums[:3])
        return f"#{r:02X}{g:02X}{b:02X}"
    if lower.startswith("hsl"):
        nums = _nums(value[value.index("(") + 1 :])
        if len(nums) < 3:
            return None
        h, sat, light = nums[0] % 360 / 360, nums[1] / 100, nums[2] / 100
        r, g, b = (round(c * 255) for c in colorsys.hls_to_rgb(h, light, sat))
        return f"#{r:02X}{g:02X}{b:02X}"
    return None


def is_neutral(hex_colour: str) -> bool:
    """Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10 %."""
    r, g, b = (int(hex_colour[i : i + 2], 16) / 255 for i in (1, 3, 5))
    _h, light, sat = colorsys.rgb_to_hls(r, g, b)
    return sat < 0.15 or light > 0.92 or light < 0.10


def extract_palette(css_path: Path, vars: list[str] | None = None) -> list[Colour]:
    """Colours from a CSS file: custom properties in declaration order, then bare literals;
    normalised, neutrals and duplicates dropped, capped at 8. `vars` restricts and orders."""
    css_path = Path(css_path)
    if not css_path.is_file():
        raise UsageError(f"palette CSS not found: {css_path}")
    text = css_path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    named: list[Colour] = []
    for name, raw in CSS_VAR_RE.findall(text):
        hex_colour = normalise_colour(raw)
        if hex_colour:
            named.append(Colour(name, hex_colour))
    if vars:
        by_name = {c.name: c for c in named}
        chosen: list[Colour] = []
        missing: list[str] = []
        for var in vars:
            key = var.lstrip("-")
            if key in by_name:
                chosen.append(by_name[key])
            else:
                missing.append(var)
        if missing:
            raise UsageError(f"{css_path}: custom propert{'y' if len(missing) == 1 else 'ies'} not found: {', '.join(missing)}")
        colours = chosen
    else:
        seen: set[str] = set()
        colours = []
        var_values = {normalise_colour(raw) for _n, raw in CSS_VAR_RE.findall(text)}
        literal_index = len(named)
        for literal in COLOUR_RE.findall(re.sub(CSS_VAR_RE, "", text)):
            hex_colour = normalise_colour(literal)
            if hex_colour and hex_colour not in var_values:
                literal_index += 1
                named.append(Colour(f"colour-{literal_index}", hex_colour))
        for colour in named:
            if is_neutral(colour.hex) or colour.hex in seen:
                continue
            seen.add(colour.hex)
            colours.append(colour)
        colours = colours[:PALETTE_MAX]
    if len(colours) < PALETTE_MIN:
        raise UsageError(f"{css_path}: only {len(colours)} usable colour(s); need at least {PALETTE_MIN} saturated colours")
    return colours


def palette_paragraph(colours: list[Colour]) -> str:
    listing = ", ".join(f"{c.name} {c.hex}" for c in colours)
    return f"Project palette override: cycle item colours in this order: {listing}; never repeat a colour on adjacent items; keep the family backdrop, neutrals, shadows and typography unchanged."


# --- prompt ---

SECRET_RE = re.compile(r"AIza[0-9A-Za-z_-]{20,}|sk-[A-Za-z0-9_-]{20,}|(?<![A-Za-z0-9])[A-Za-z0-9_-]{40,}(?![A-Za-z0-9])")
TEMPLATE_PATH = "templates/base-prompt.md"


@dataclass
class Prompt:
    text: str
    frontmatter: dict
    warnings: list[str] = field(default_factory=list)


def redact(text: str) -> str:
    return SECRET_RE.sub("[redacted]", text)


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def _bullets(lines: list[str]) -> str:
    return "\n".join(f"- {line}" for line in lines)


def render_layout_block(member: Member) -> str:
    """The member's device layout as the markdown block the Layout Guidelines slot expects."""
    layout = member.raw["layout"]
    variants = "\n".join(f"| **{v['name']}** | {v['focus']} | {v['emphasis']} |" for v in layout["variants"])
    return "\n\n".join(
        [
            f"# {member.name}",
            member.raw["device"] + ".",
            "## Structure\n\n" + _bullets(layout["structure"]),
            "## Variants\n\n| Variant | Focus | Visual Emphasis |\n|---------|-------|-----------------|\n" + variants,
            "## Best For\n\n" + _bullets(member.raw["best_for"]),
            "## Visual Elements\n\n" + _bullets(layout["visual_elements"]),
            "## Text Placement\n\n" + _bullets(layout["text_placement"]),
        ]
    )


def content_block(spec: Spec) -> str:
    lines = [f'Title: "{redact(spec.title)}"']
    if spec.subtitle:
        lines.append(f'Subtitle: "{redact(spec.subtitle)}"')
    lines += ["", "Items (in order):"]
    for index, item in enumerate(spec.items, 1):
        entry = f'{index}. "{redact(item.label)}"'
        if item.detail:
            entry += f" - {redact(item.detail)}"
        if item.value:
            entry += f" ({redact(item.value)})"
        if item.icon:
            entry += f" [icon: {item.icon}]"
        lines.append(entry)
    if spec.stats:
        lines += ["", "Stats:"]
        for stat in spec.stats:
            caption = stat.get("caption")
            lines.append(f'- "{redact(str(stat.get("value", "")))}"' + (f" - {redact(str(caption))}" if caption else ""))
    if spec.notes:
        lines += ["", f"Design notes: {redact(spec.notes)}"]
    return "\n".join(lines)


def text_labels(spec: Spec) -> list[str]:
    labels = [spec.title]
    if spec.subtitle:
        labels.append(spec.subtitle)
    for index, item in enumerate(spec.items, 1):
        labels.append(f"{index:02d} {item.label}")
        if item.value:
            labels.append(item.value)
    labels += [str(stat.get("value", "")) for stat in spec.stats if stat.get("value")]
    return [redact(label) for label in labels]


def word_count(labels: list[str]) -> int:
    return sum(len(label.split()) for label in labels)


def assemble(
    cat: Catalogue,
    spec: Spec,
    route_: Route,
    ratio: str,
    refs: list[Path] | None = None,
    palette: list[Colour] | None = None,
    palette_source: Path | None = None,
    strict: bool = False,
    aspect_snapped_from: str | None = None,
) -> Prompt:
    """Fill templates/base-prompt.md; warnings for text budget and item range; strict raises."""
    member = cat.member(route_.member)
    template = (cat.root / TEMPLATE_PATH).read_text(encoding="utf-8")
    negative = cat.family["negative_list"]
    style_block = member.prompt_fragment.strip()
    if not style_block.endswith(negative.split(". ")[-1]):
        style_block += "\n\n" + negative
    if palette:
        style_block += "\n\n" + palette_paragraph(palette)
    labels = text_labels(spec)
    slots = {
        "{{LAYOUT}}": route_.layout,
        "{{STYLE}}": route_.style,
        "{{ASPECT_RATIO}}": ratio,
        "{{LANGUAGE}}": spec.language,
        "{{LAYOUT_GUIDELINES}}": render_layout_block(member),
        "{{STYLE_GUIDELINES}}": style_block,
        "{{CONTENT}}": content_block(spec),
        "{{TEXT_LABELS}}": "\n".join(f'"{label}"' for label in labels),
    }
    text = template
    for slot, value in slots.items():
        text = text.replace(slot, value)
    warnings: list[str] = []
    orient = orientation(cat, ratio)
    budget = cat.family["text_budget"][orient]
    words = word_count(labels)
    if words > budget:
        warnings.append(f"on-image text is {words} words, over the {budget}-word budget for {orient} ({ratio}); shorten labels or split into two images")
    lo, hi = member.items["min"], member.items["max"]
    count = len(spec.items)
    if not lo <= count <= hi:
        hint = f"; consider {route_.alternates[0]}" if route_.alternates else ""
        warnings.append(f"{count} items is outside the {member.name} range {lo} to {hi}{hint}")
    if aspect_snapped_from:
        warnings.append(f"aspect {aspect_snapped_from} snapped to {ratio}")
    if strict and warnings:
        raise UsageError("strict: " + "; ".join(warnings))
    frontmatter: dict = {
        "layout": route_.layout,
        "style": route_.style,
        "style_member": member.name,
        "aspect": ratio,
        "language": spec.language,
        "references": [{"ref_id": f"{index:02d}", "filename": Path(ref).name, "usage": "direct"} for index, ref in enumerate(refs or [], 1)],
    }
    if palette:
        frontmatter["palette"] = {"source": str(palette_source), "colours": [c.as_dict() for c in palette]}
    return Prompt(text=text.rstrip() + "\n", frontmatter=frontmatter, warnings=warnings)


def write_prompt(out_dir: Path, prompt: Prompt, slug: str) -> Path:
    """prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites."""
    prompts_dir = Path(out_dir) / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    taken = [int(m.group(1)) for f in prompts_dir.iterdir() if (m := re.match(r"^(\d{2})-", f.name))]
    number = max(taken, default=0) + 1
    path = prompts_dir / f"{number:02d}-infographic-{slug}.md"
    header = yaml.safe_dump(prompt.frontmatter, sort_keys=False, allow_unicode=True).rstrip()
    path.write_text(f"---\n{header}\n---\n{prompt.text}", encoding="utf-8")
    return path


# --- creds ---

KEY_NAMES = ("GEMINI_API_KEY", "GOOGLE_API_KEY")


def parse_env_file(path: Path) -> dict[str, str]:
    """Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments ignored."""
    found: dict[str, str] = {}
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError:
        return found
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        found[key] = value
    return found


def api_key(explicit: str | None, cwd: Path | None = None) -> tuple[str, str]:
    """(key, source). Order: --api-key, ./.env in the calling directory, process environment.
    No parent-directory walk. The source string never contains the key."""
    if explicit:
        return explicit, "--api-key"
    env_path = Path(cwd or Path.cwd()) / ".env"
    values = parse_env_file(env_path)
    for name in KEY_NAMES:
        if values.get(name):
            return values[name], f"{env_path}:{name}"
    for name in KEY_NAMES:
        if os.environ.get(name):
            return os.environ[name], f"env:{name}"
    raise UsageError(f"no API key: expected GEMINI_API_KEY in {env_path} or the environment")


# --- render ---

DEFAULT_MODEL = "gemini-3-pro-image"
RESOLUTIONS = ("1K", "2K", "4K")
STYLE_NOTE = "The images above are style references only. Match their rendering style, depth, lighting, palette treatment and typography. Do not copy their text or data."
EXIT_CODES = {"ok": 0, "dry-run": 0, "error": 2}


def exit_code(result: dict) -> int:
    return EXIT_CODES.get(result.get("status", "error"), 2)


def load_prompt_text(path: Path) -> str:
    text = Path(path).read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :]
    return text.strip()


def backup_existing(path: Path) -> Path | None:
    if not path.exists():
        return None
    stamp = time.strftime("%Y%m%d-%H%M%S")
    target = path.with_name(f"{path.stem}-backup-{stamp}{path.suffix}")
    path.rename(target)
    return target


def _genai_client(api_key: str):
    from google import genai

    return genai.Client(api_key=api_key)


def render(
    prompt_path: Path,
    out_png: Path,
    ratio: str,
    resolution: str = "2K",
    model: str | None = None,
    refs: list[Path] | tuple[Path, ...] = (),
    retries: int = 1,
    dry_run: bool = False,
    api_key: str | None = None,
    client_factory=None,
    prompt_warnings: list[str] | None = None,
) -> dict:
    """Call Nano Banana Pro with the persisted prompt file and save an RGB PNG.

    Returns the single result record the CLI prints; status ok | dry-run | error."""
    if resolution not in RESOLUTIONS:
        raise UsageError(f"resolution must be one of {', '.join(RESOLUTIONS)}, got {resolution!r}")
    model = model or os.environ.get("IIG3D_MODEL") or DEFAULT_MODEL
    prompt_path, out_png = Path(prompt_path), Path(out_png)
    prompt = load_prompt_text(prompt_path)
    if not prompt:
        raise UsageError(f"empty prompt: {prompt_path}")
    ref_paths = [Path(r) for r in refs]
    base = {
        "path": str(out_png.resolve()),
        "bytes": 0,
        "model": model,
        "aspect_ratio": ratio,
        "resolution": resolution,
        "refs": len(ref_paths),
        "attempts": 0,
        "elapsed_seconds": 0.0,
        "prompt_file": str(prompt_path.resolve()),
        "prompt_chars": len(prompt),
        "warnings": list(prompt_warnings or []),
    }
    if dry_run:
        return {"status": "dry-run", **base}

    from io import BytesIO

    from google.genai import types
    from PIL import Image as PILImage

    client = (client_factory or _genai_client)(api_key)
    contents: list = [PILImage.open(r) for r in ref_paths]
    if contents:
        contents.append(STYLE_NOTE)
    contents.append(prompt)
    image_cfg = types.ImageConfig(image_size=resolution, aspect_ratio=ratio)
    config = types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=image_cfg,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )
    started = time.time()
    last_error: Exception | None = None
    for attempt in range(1, retries + 2):
        try:
            print(f"[{attempt}] {model} {ratio} {resolution} refs={len(ref_paths)}", file=sys.stderr)
            response = client.models.generate_content(model=model, contents=contents, config=config)
            image = None
            for part in response.parts or []:
                if getattr(part, "text", None):
                    print(f"Model text: {part.text.strip()[:300]}", file=sys.stderr)
                elif getattr(part, "inline_data", None) is not None:
                    data = part.inline_data.data
                    if isinstance(data, str):
                        import base64

                        data = base64.b64decode(data)
                    image = PILImage.open(BytesIO(data))
                    break
            if image is None:
                raise RuntimeError("no image part in response (content may have been refused)")
            if image.mode == "RGBA":
                flat = PILImage.new("RGB", image.size, (255, 255, 255))
                flat.paste(image, mask=image.split()[3])
                image = flat
            elif image.mode != "RGB":
                image = image.convert("RGB")
            out_png.parent.mkdir(parents=True, exist_ok=True)
            backup = backup_existing(out_png)
            image.save(str(out_png), "PNG")
            result = {
                "status": "ok",
                **base,
                "bytes": out_png.stat().st_size,
                "attempts": attempt,
                "elapsed_seconds": round(time.time() - started, 1),
            }
            if backup:
                result["backup"] = str(backup)
            return result
        except Exception as err:
            last_error = err
            print(f"Attempt {attempt} failed: {err}", file=sys.stderr)
            if attempt <= retries:
                time.sleep(2 * attempt)
    return {
        "status": "error",
        **base,
        "attempts": retries + 1,
        "elapsed_seconds": round(time.time() - started, 1),
        "error": str(last_error),
    }


# --- docs ---

GENERATED_NOTE = "<!-- Generated by `iig3d.py docs` from catalogue/*.yaml. Do not edit by hand. -->"


def _table(headers: list[str], rows: list[list[str]]) -> str:
    line = "| " + " | ".join(headers) + " |"
    sep = "|" + "|".join("-" * (len(h) + 2) for h in headers) + "|"
    body = "\n".join("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join([line, sep, body])


def member_markdown(cat: Catalogue, member: Member) -> str:
    raw = member.raw
    layout = raw["layout"]
    refs_rows = [[f"`{r['file']}`", r["shows"].replace("|", "\\|"), ", ".join(r["flags"])] for r in member.refs]
    variants = [[f"**{v['name']}**", v["focus"], v["emphasis"]] for v in layout["variants"]]
    pairings = [f"- `{layout_name}`: refs {', '.join(ids)}" for layout_name, ids in member.pairings.items()]
    parts = [
        f"# {member.name}",
        GENERATED_NOTE,
        f"Member of the 3D corporate family. {raw['device']}. Backdrop: {raw['backdrop']}. Items: {member.items['min']} to {member.items['max']}. Default aspect: {member.aspect_default}.",
        "## Reference images\n\n" + _table(["Ref", "Shows", "Flags"], refs_rows),
        "## Colour palette\n\n" + _bullets(raw["style"]["palette"]),
        "## Visual elements\n\n" + _bullets(raw["style"]["visual_elements"]),
        "## Typography\n\n" + _bullets(raw["style"]["typography"]),
        "## Composition rules\n\n" + _bullets(raw["style"]["composition"]),
        "## Layout\n\n### Structure\n\n"
        + _bullets(layout["structure"])
        + "\n\n### Variants\n\n"
        + _table(["Variant", "Focus", "Visual emphasis"], variants)
        + "\n\n### Visual elements\n\n"
        + _bullets(layout["visual_elements"])
        + "\n\n### Text placement\n\n"
        + _bullets(layout["text_placement"]),
        "## Prompt fragment\n\n```\n" + member.prompt_fragment.strip() + "\n```",
        "## Best for\n\n" + _bullets(raw["best_for"]),
        "## Recommended pairings\n\n" + "\n".join(pairings) + "\n\nAlternates: " + ", ".join(f"`{a}`" for a in member.alternates),
        f"Source: {raw['source']['origin']} (added {raw['source']['added']}).",
    ]
    return "\n\n".join(parts) + "\n"


def catalogue_markdown(cat: Catalogue) -> str:
    family = cat.family
    members = [[f"`{m.name}`", m.raw["device"], m.raw["backdrop"], f"{m.items['min']}-{m.items['max']}", str(len(m.refs))] for m in cat.members.values()]
    routing = [[f"`{layout}`", f"`{row['primary']}`", ", ".join(f"`{a}`" for a in row["alternates"]) or "-"] for layout, row in cat.routing.items()]
    palette = [[c["name"], f"`{c['hex']}`"] for c in family["palette"]["items"]]
    parts = [
        "# iig3d catalogue",
        GENERATED_NOTE,
        f"{len(cat.members)} members of the 3D corporate family. `{UMBRELLA}` is the umbrella style: it routes to a member by layout.",
        "## Members\n\n" + _table(["Style", "Structural device", "Backdrop", "Items", "Refs"], members),
        "## Layout routing\n\n" + _table(["Layout", "Primary member", "Alternates"], routing),
        "## Shared palette\n\n" + _table(["Name", "Hex"], palette) + f"\n\nLight backdrop {' to '.join(family['palette']['light_backdrop'])}; blue-grey {' to '.join(family['palette']['blue_grey_backdrop'])}; "
        f"dark {' to '.join(family['palette']['dark_backdrop'])}. {family['palette']['override_rule']}.",
        "## Shared typography\n\n" + _bullets(family["typography"]),
        "## Negative list\n\n" + family["negative_list"],
    ]
    return "\n\n".join(parts) + "\n"


def expected_docs(cat: Catalogue) -> dict[Path, str]:
    docs = {cat.root / "docs" / "CATALOGUE.md": catalogue_markdown(cat)}
    for member in cat.members.values():
        docs[cat.root / "docs" / "members" / f"{member.name}.md"] = member_markdown(cat, member)
    return docs


def render_docs(cat: Catalogue) -> list[Path]:
    written: list[Path] = []
    for path, text in expected_docs(cat).items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        written.append(path)
    return written


def stale_docs(cat: Catalogue) -> list[str]:
    """`docs stale: <path>` for every generated file that is missing or differs from the YAML."""
    problems = []
    for path, text in expected_docs(cat).items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            problems.append(f"docs stale: {path.relative_to(cat.root).as_posix()} (run `iig3d.py docs`)")
    return problems


# --- cli ---


def _add_common(sub: argparse.ArgumentParser) -> None:
    sub.add_argument("--skill-root", default=None, help="skill directory (default: this script's parent)")


def _add_prepare_args(sub: argparse.ArgumentParser) -> None:
    sub.add_argument("--spec", required=True, help="YAML content spec")
    sub.add_argument("--out-dir", required=True, help="output directory (prompts/ and infographic.png)")
    sub.add_argument("--layout", default=None)
    sub.add_argument("--style", default=None, help="3d-* member or industrial-3d")
    sub.add_argument("--aspect", default=None, help="landscape | portrait | square | W:H")
    sub.add_argument("--palette-css", default=None, help="CSS file whose colours replace the item colours")
    sub.add_argument("--palette-vars", default=None, help="comma-separated custom properties to use, in order")
    sub.add_argument("--ref", action="append", default=[], help="user reference image (repeatable)")
    sub.add_argument("--no-style-refs", action="store_true", help="do not pass the member's bundled refs")
    sub.add_argument("--strict", action="store_true", help="turn prompt warnings into exit 1")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="iig3d", description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    p_list = sub.add_parser("list", help="members and layouts")
    _add_common(p_list)
    p_route = sub.add_parser("route", help="resolve layout and style to a member")
    p_route.add_argument("--layout", default=None)
    p_route.add_argument("--style", default=None)
    _add_common(p_route)
    p_refs = sub.add_parser("refs", help="reference images for a member and layout")
    p_refs.add_argument("--member", required=True)
    p_refs.add_argument("--layout", required=True)
    p_refs.add_argument("--ref", action="append", default=[])
    _add_common(p_refs)
    p_prompt = sub.add_parser("prompt", help="assemble and persist the prompt file")
    _add_prepare_args(p_prompt)
    _add_common(p_prompt)
    p_render = sub.add_parser("render", help="assemble the prompt and render with Nano Banana Pro")
    _add_prepare_args(p_render)
    p_render.add_argument("--dry-run", action="store_true")
    p_render.add_argument("--resolution", default="2K", choices=RESOLUTIONS)
    p_render.add_argument("--model", default=None)
    p_render.add_argument("--retries", type=int, default=1)
    p_render.add_argument("--api-key", default=None)
    p_render.add_argument("--no-confirm", action="store_true", help="accepted for parity with SKILL.md; no effect here")
    _add_common(p_render)
    p_add = sub.add_parser("add", help="add a reference image to the catalogue")
    p_add.add_argument("--image", required=True)
    p_add.add_argument("--meta", required=True)
    _add_common(p_add)
    p_docs = sub.add_parser("docs", help="regenerate catalogue markdown")
    _add_common(p_docs)
    p_check = sub.add_parser("check", help="validate the catalogue, refs and docs")
    p_check.add_argument("--allow-watermark", action="store_true")
    _add_common(p_check)
    p_palette = sub.add_parser("palette", help="preview colours extracted from a CSS file")
    p_palette.add_argument("--css", required=True)
    p_palette.add_argument("--vars", default=None, help="comma-separated custom properties")
    return parser


def _split_vars(value: str | None) -> list[str]:
    return [v.strip() for v in value.split(",") if v.strip()] if value else []


def cmd_list(cat: Catalogue) -> dict:
    members = [
        {
            "name": m.name,
            "device": m.raw["device"],
            "items": m.items,
            "aspect_default": m.aspect_default,
            "refs": len(m.refs),
            "pairings": list(m.pairings),
        }
        for m in cat.members.values()
    ]
    layouts = [{"layout": layout, "primary": row["primary"], "alternates": row["alternates"]} for layout, row in cat.routing.items()]
    return {"status": "ok", "members": members, "layouts": layouts, "umbrella": UMBRELLA}


def prepare(cat: Catalogue, args: argparse.Namespace) -> dict:
    """Shared front half of prompt and render: spec, route, aspect, refs, palette, prompt file."""
    spec = load_spec(Path(args.spec))
    route_ = route(cat, args.layout or spec.layout, args.style or spec.style)
    member = cat.member(route_.member)
    ratio, snapped_from = snap_aspect(cat, args.aspect or spec.aspect, member.aspect_default)
    user_refs = [Path(r) for r in args.ref] + spec.refs
    refs = select_refs(cat, member.name, route_.layout, user_refs=user_refs, style_refs=not args.no_style_refs)
    css = Path(args.palette_css).resolve() if args.palette_css else spec.palette_css
    palette = None
    if css:
        vars_ = _split_vars(args.palette_vars) or spec.palette_vars
        palette = extract_palette(css, vars=vars_ or None)
    prompt = assemble(cat, spec, route_, ratio, refs=refs, palette=palette, palette_source=css, strict=args.strict, aspect_snapped_from=snapped_from)
    prompt_file = write_prompt(Path(args.out_dir), prompt, slugify(spec.title))
    return {
        "status": "ok",
        "prompt_file": str(prompt_file),
        "member": member.name,
        "layout": route_.layout,
        "style": route_.style,
        "aspect_ratio": ratio,
        "language": spec.language,
        "refs": [str(r) for r in refs],
        "palette": [c.as_dict() for c in palette] if palette else None,
        "warnings": prompt.warnings,
    }


def cmd_render(cat: Catalogue, args: argparse.Namespace) -> dict:
    key, source = api_key(args.api_key)
    print(f"API key source: {source}", file=sys.stderr)
    prepared = prepare(cat, args)
    result = render(
        Path(prepared["prompt_file"]),
        Path(args.out_dir) / "infographic.png",
        prepared["aspect_ratio"],
        resolution=args.resolution,
        model=args.model,
        refs=[Path(r) for r in prepared["refs"]],
        retries=args.retries,
        dry_run=args.dry_run,
        api_key=key,
        prompt_warnings=prepared["warnings"],
    )
    result.update({k: prepared[k] for k in ("member", "layout", "style", "language", "palette")})
    return result


def dispatch(args: argparse.Namespace) -> dict:
    if args.command == "palette":
        colours = extract_palette(Path(args.css), vars=_split_vars(args.vars) or None)
        return {"status": "ok", "source": str(Path(args.css).resolve()), "colours": [c.as_dict() for c in colours], "paragraph": palette_paragraph(colours)}
    cat = load_catalogue(args.skill_root)
    if args.command == "list":
        return cmd_list(cat)
    if args.command == "route":
        return {"status": "ok", **route(cat, args.layout, args.style).as_dict()}
    if args.command == "refs":
        refs = select_refs(cat, args.member, args.layout, user_refs=[Path(r) for r in args.ref])
        return {"status": "ok", "member": args.member, "layout": args.layout, "refs": [str(r) for r in refs]}
    if args.command == "prompt":
        return prepare(cat, args)
    if args.command == "render":
        return cmd_render(cat, args)
    if args.command == "docs":
        return {"status": "ok", "written": [str(p) for p in render_docs(cat)]}
    if args.command == "check":
        violations = check(cat, allow_watermark=args.allow_watermark)
        return {"status": "ok" if not violations else "error", "violations": violations}
    if args.command == "add":
        return add_ref(cat, Path(args.image), Path(args.meta))
    raise UsageError(f"unknown command {args.command}")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = dispatch(args)
    except UsageError as err:
        print(json.dumps({"status": "error", "error": str(err)}))
        return 1
    except NotImplementedError as err:
        print(json.dumps({"status": "error", "error": f"not implemented: {err}"}))
        return 1
    print(json.dumps(result))
    if result.get("status") == "error":
        return exit_code(result) if "attempts" in result else 1
    return 0


def check(cat: Catalogue, allow_watermark: bool = False) -> list[str]:  # replaced in the check step
    raise NotImplementedError("check")


def add_ref(cat: Catalogue, image: Path, meta: Path) -> dict:  # replaced in the add step
    raise NotImplementedError("add")


if __name__ == "__main__":
    sys.exit(main())
