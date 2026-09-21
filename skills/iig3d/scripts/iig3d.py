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
import base64
import colorsys
import json
import os
import re
import sys
import time
from dataclasses import asdict, dataclass, field, fields
from io import BytesIO
from pathlib import Path

import tomllib
import yaml

YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
YAML_DUMPER = getattr(yaml, "CSafeDumper", yaml.SafeDumper)

SKILL_ROOT = Path(__file__).resolve().parents[1]
SUBCOMMANDS = ["list", "route", "refs", "prompt", "render", "add", "docs", "check", "palette"]


class UsageError(Exception):
    """Bad input: exit code 1, message on stdout as JSON."""


# --- catalogue ---

MEMBER_PREFIX = "3d-"
MEMBER_NAME_RE = re.compile(r"^3d-[a-z0-9]+(?:-[a-z0-9]+)*$")


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

    def __getitem__(self, key: str):
        return self.raw[key]


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
    def family_yaml(self) -> Path:
        return self.root / "catalogue" / "family.yaml"

    def member_yaml(self, name: str) -> Path:
        return self.root / "catalogue" / "members" / f"{name}.yaml"

    def member(self, name: str) -> Member:
        try:
            return self.members[name]
        except KeyError:
            raise UsageError(f"unknown member {name!r}; valid: {', '.join(sorted(self.members))}") from None

    def ref_path(self, member: str, ref: dict) -> Path:
        return self.root / "refs" / member / ref["file"]

    def is_layout(self, name: str) -> bool:
        """A general routing layout or a member's own device name."""
        return name in self.routing or name in self.members

    def resolve_ref(self, token: str, style: str | None = None) -> tuple[Member, dict]:
        """A catalogue ref named by the user: `<member>/<id|file|stem>`, a `refs/<member>/<file>`
        path, or a bare id/file when `style` already names the member. Only YAML records match."""
        parts = [p for p in str(token).strip().replace("\\", "/").split("/") if p]
        if parts and parts[0] == "refs":
            parts = parts[1:]
        if len(parts) == 2:
            member_name, key = parts
        elif len(parts) == 1 and style in self.members:
            member_name, key = style, parts[0]
        elif len(parts) == 1:
            raise UsageError(f"pin {token!r} needs a member: use <member>/<ref>, e.g. 3d-capsule-hub/06, or set style to a 3d-* member")
        else:
            raise UsageError(f"pin {token!r} is not <member>/<ref>")
        member = self.member(member_name)
        for ref in member.refs:
            if key in (ref["id"], ref["file"], Path(ref["file"]).stem):
                return member, ref
        choices = ", ".join(f"{r['id']} ({r['file']})" for r in member.refs)
        raise UsageError(f"unknown ref {key!r} for {member_name}; valid: {choices}")

    def pin_token(self, member: str, ref: dict) -> str:
        return f"{member}/{ref['id']}"

    @property
    def negative_tail(self) -> str:
        """Last sentence of the family negative list; a fragment that ends with it already carries the list."""
        return self.family["negative_list"].split(". ")[-1]

    @property
    def flag_values(self) -> list[str]:
        return self.schema["member"]["refs"]["items"]["keys"]["flags"]["items"]["values"]


def read_yaml(path: Path) -> dict:
    try:
        with path.open(encoding="utf-8") as handle:
            return yaml.load(handle, Loader=YAML_LOADER) or {}  # noqa: S506 # nosec B506 - SafeLoader or CSafeLoader only
    except yaml.YAMLError as err:
        raise UsageError(f"{path}: not valid YAML: {str(err).splitlines()[0]}") from err


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        yaml.dump(data, handle, Dumper=YAML_DUMPER, sort_keys=False, allow_unicode=True, width=120)


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
        return asdict(self)


def split_style(cat: Catalogue, layout: str | None, style: str | None, pin: str | None = None) -> tuple[str | None, str | None]:
    """(style, pin) after reading a ref name out of `style`: with `layout` naming a member,
    `style: 06` or `style: ref-06-x.jpg` means that member's ref; `style: 3d-x/06` works with
    any layout. A member name or the umbrella pass through; an explicit pin is left alone."""
    if pin or style in (None, UMBRELLA) or style in cat.members:
        return style, pin
    if "/" in style:
        return None, style
    if layout in cat.members:
        return None, f"{layout}/{style}"
    raise UsageError(f"unknown style {style!r}; valid: {UMBRELLA}, a 3d-* member, or a ref of the member named by layout (e.g. layout: 3d-capsule-hub, style: 06)")


def route(cat: Catalogue, layout: str | None, style: str | None, pinned_member: str | None = None) -> Route:
    """Resolve (layout, style) to a family member.

    Explicit 3d-* style wins; a 3d-* layout names its own member; otherwise the family routing
    table maps a general layout to its primary member. Style omitted or `industrial-3d` both
    mean "route by layout". A pinned catalogue ref names its member: it becomes the style when
    style is omitted or the umbrella, the default layout, and must agree with an explicit style.
    """
    if pinned_member:
        if style not in (None, UMBRELLA, pinned_member):
            raise UsageError(f"style {style} conflicts with pinned ref member {pinned_member}")
        style = pinned_member
        layout = layout or pinned_member
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
        raise UsageError(f"unknown layout {layout!r}; valid: {', '.join(cat.routing)} or a 3d-* member name")
    row = cat.routing[layout]
    return Route(row["primary"], layout, list(row["alternates"]), f"routing table: {layout} -> {row['primary']}")


# --- spec ---


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
    pin: str | None = None
    path: Path | None = None


SPEC_KEYS = {f.name for f in fields(Spec)} - {"path"}
ITEM_KEYS = {f.name for f in fields(Item)}


def _str(value) -> str:
    return "" if value is None else str(value)


def _opt_str(value) -> str | None:
    return None if value is None else str(value)


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
                value=_opt_str(entry.get("value")),
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
        aspect=_opt_str(raw.get("aspect")),
        palette_css=(base / css).resolve() if css else None,
        palette_vars=[str(v) for v in raw.get("palette_vars") or []],
        stats=[dict(s) for s in raw.get("stats") or []],
        notes=_str(raw.get("notes")),
        refs=[(base / r).resolve() for r in raw.get("refs") or []],
        pin=_opt_str(raw.get("pin")),
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


def _pairing(member: Member, layout: str) -> list[str]:
    """Ref ids paired with the layout; the member's first pairing when the layout has none."""
    return member.pairings.get(layout) or next(iter(member.pairings.values()), [])


def pick_style_refs(cat: Catalogue, member: Member, layout: str) -> list[dict]:
    """Pairing refs for the layout (2 to 3), padded from the member pool when short, with the
    flag rules applied: never two watermarks, never only low-res refs, clean refs first."""
    low, high = cat.family["ref_rules"]["per_render"]
    pairing = _pairing(member, layout)
    by_id = {r["id"]: r for r in member.refs}
    pool = [by_id[rid] for rid in pairing if rid in by_id]
    pool += [r for r in member.refs if r not in pool]
    cut = min(high, len(pairing))
    head, rest = pool[:cut], pool[cut:]
    rest.sort(key=lambda r: ("clean" not in r["flags"], "low-res" in r["flags"]))
    picked: list[dict] = []
    seen_watermark = False

    def take(ref: dict) -> None:
        nonlocal seen_watermark
        watermark = "watermark" in ref["flags"]
        if watermark and seen_watermark:
            return
        seen_watermark = seen_watermark or watermark
        picked.append(ref)

    for ref in head:
        take(ref)
    while len(picked) < low and rest:
        take(rest.pop(0))
    if picked and all("low-res" in r["flags"] for r in picked):
        extra = next((r for r in rest if "low-res" not in r["flags"] and not ("watermark" in r["flags"] and seen_watermark)), None)
        if extra:
            picked.append(extra)
    picked.sort(key=lambda r: "clean" not in r["flags"])
    return picked


def ref_rule_violations(refs: list[dict]) -> list[str]:
    """The two selection invariants, stated once for the selector and the checker."""
    problems = []
    if sum("watermark" in r["flags"] for r in refs) > 1:
        problems.append("two watermarked refs selected")
    if refs and all("low-res" in r["flags"] for r in refs):
        problems.append("only low-res refs selected")
    return problems


def pick_pinned_refs(cat: Catalogue, member: Member, layout: str, pinned: dict, style_refs: bool = True) -> list[dict]:
    """The pinned ref first, then the layout's style refs as company up to per_render high,
    never a second watermark. Style refs off: the pinned ref alone."""
    picked = [pinned]
    if not style_refs:
        return picked
    _, high = cat.family["ref_rules"]["per_render"]
    for ref in pick_style_refs(cat, member, layout):
        if len(picked) >= high:
            break
        if ref["id"] == pinned["id"]:
            continue
        if "watermark" in ref["flags"] and any("watermark" in r["flags"] for r in picked):
            continue
        picked.append(ref)
    return picked


def select_refs(
    cat: Catalogue,
    member_name: str,
    layout: str,
    user_refs: list[Path] | None = None,
    style_refs: bool = True,
    pinned: dict | None = None,
) -> list[Path]:
    """Style refs as paths (see pick_style_refs), user refs appended, capped by ref_rules.max_total.
    A pinned catalogue ref (see Catalogue.resolve_ref) always comes first."""
    member = cat.member(member_name)
    paths: list[Path] = []
    if pinned is not None:
        catalogue_refs = pick_pinned_refs(cat, member, layout, pinned, style_refs=style_refs)
    elif style_refs:
        catalogue_refs = pick_style_refs(cat, member, layout)
    else:
        catalogue_refs = []
    for ref in catalogue_refs:
        path = cat.ref_path(member.name, ref)
        if not path.is_file():
            raise UsageError(f"reference image missing: {path}")
        paths.append(path)
    for extra_path in user_refs or []:
        extra_path = Path(extra_path)
        if not extra_path.is_file():
            raise UsageError(f"reference image not found: {extra_path}")
        paths.append(extra_path)
    return paths[: cat.family["ref_rules"]["max_total"]]


# --- palette ---

PALETTE_MIN, PALETTE_MAX = 3, 8
CSS_VAR_RE = re.compile(r"--([A-Za-z0-9_-]+)\s*:\s*([^;}]+)")
COLOUR_RE = re.compile(r"#[0-9A-Fa-f]{8}\b|#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3,4}\b|rgba?\([^)]*\)|hsla?\([^)]*\)")


@dataclass(frozen=True)
class Colour:
    name: str
    hex: str

    def as_dict(self) -> dict:
        return asdict(self)


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
        colours = list({c.hex: c for c in chosen}.values())[:PALETTE_MAX]
    else:
        known = {c.hex for c in named}
        literals = [h for h in map(normalise_colour, COLOUR_RE.findall(CSS_VAR_RE.sub("", text))) if h and h not in known]
        named += [Colour(f"colour-{len(named) + i}", h) for i, h in enumerate(literals, 1)]
        seen: set[str] = set()
        colours = []
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


def _table(headers: list[str], rows: list[list[str]]) -> str:
    line = "| " + " | ".join(headers) + " |"
    sep = "|" + "|".join("-" * (len(h) + 2) for h in headers) + "|"
    body = "\n".join("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join([line, sep, body])


def layout_sections(member: Member) -> list[tuple[str, str]]:
    """(heading, body) pairs of the member's device layout, shared by the prompt and the docs."""
    layout = member["layout"]
    variants = [[f"**{v['name']}**", v["focus"], v["emphasis"]] for v in layout["variants"]]
    return [
        ("Structure", _bullets(layout["structure"])),
        ("Variants", _table(["Variant", "Focus", "Visual Emphasis"], variants)),
        ("Best For", _bullets(member["best_for"])),
        ("Visual Elements", _bullets(layout["visual_elements"])),
        ("Text Placement", _bullets(layout["text_placement"])),
    ]


def render_layout_block(member: Member) -> str:
    """The member's device layout as the markdown block the Layout Guidelines slot expects."""
    parts = [f"# {member.name}", member["device"] + "."]
    parts += [f"## {heading}\n\n{body}" for heading, body in layout_sections(member)]
    return "\n\n".join(parts)


def has_negative_list(fragment: str, cat: Catalogue) -> bool:
    return fragment.strip().endswith(cat.negative_tail)


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


def reference_composition(pinned: dict) -> str:
    """The Reference Composition section: reproduce reference image 1, swap in the content."""
    lines = [
        "## Reference Composition",
        "",
        f"Reference image 1 is the composition to reproduce. It shows: {pinned['shows'].strip().rstrip('.')}.",
    ]
    if pinned.get("variant"):
        lines.append(f"It is the **{pinned['variant']}** variant of this device; follow that variant's emphasis.")
    if pinned.get("item_count"):
        lines.append(f"It holds {pinned['item_count']} items; keep the same slots, filled in order from the content below.")
    lines += [
        "Match its structure, element placement, connector style, depth, lighting and text positions exactly.",
        "Replace every piece of its text with the content below; add or drop nothing else.",
        "Any further reference images are style support only, not compositions to copy.",
    ]
    return "\n".join(lines)


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
    pinned: dict | None = None,
) -> Prompt:
    """Fill templates/base-prompt.md; warnings for text budget and item range; strict raises.
    A pinned ref adds the Reference Composition section and is reference image 1."""
    member = cat.member(route_.member)
    template = (cat.root / TEMPLATE_PATH).read_text(encoding="utf-8")
    style_block = member.prompt_fragment.strip()
    if not has_negative_list(style_block, cat):
        style_block += "\n\n" + cat.family["negative_list"]
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
        "{{REFERENCE_COMPOSITION}}": reference_composition(pinned) if pinned else "",
        "{{CONTENT}}": content_block(spec),
        "{{TEXT_LABELS}}": "\n".join(f'"{label}"' for label in labels),
    }
    text = template
    for slot, value in slots.items():
        text = text.replace(slot, value)
    text = re.sub(r"\n{3,}", "\n\n", text)
    warnings: list[str] = []
    if pinned:
        if "low-res" in pinned["flags"]:
            warnings.append(f"pinned ref {pinned['file']} is low-res; expect a soft composition guide")
        if "watermark" in pinned["flags"]:
            warnings.append(f"pinned ref {pinned['file']} carries a watermark; check the render for stray marks")
        expected = pinned.get("item_count")
        if expected and len(spec.items) != expected:
            warnings.append(f"{len(spec.items)} items but pinned ref {pinned['file']} shows {expected}; match the count or expect the model to improvise")
    orient = orientation(cat, ratio)
    budget = cat.family["text_budget"][orient]
    words = word_count(labels + [item.detail for item in spec.items] + [str(s.get("caption", "")) for s in spec.stats])
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
        "references": [{"ref_id": f"{index:02d}", "filename": Path(ref).name, "usage": "replicate" if pinned and index == 1 else "direct"} for index, ref in enumerate(refs or [], 1)],
    }
    if pinned:
        frontmatter["pinned"] = {"ref": pinned["file"], "variant": pinned.get("variant")}
    if palette:
        frontmatter["palette"] = {"source": str(palette_source), "colours": [c.as_dict() for c in palette]}
    return Prompt(text=text.rstrip() + "\n", frontmatter=frontmatter, warnings=warnings)


def write_prompt(out_dir: Path, prompt: Prompt, slug: str) -> Path:
    """prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites."""
    prompts_dir = Path(out_dir) / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    taken = [int(m.group(1)) for f in prompts_dir.iterdir() if (m := re.match(r"^(\d+)-", f.name))]
    number = max(taken, default=0) + 1
    path = prompts_dir / f"{number:02d}-infographic-{slug}.md"
    header = yaml.dump(prompt.frontmatter, Dumper=YAML_DUMPER, sort_keys=False, allow_unicode=True).rstrip()
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
EXIT_CODES = {"ok": 0, "dry-run": 0, "violations": 1, "error": 2}


def exit_code(result: dict) -> int:
    return EXIT_CODES.get(result.get("status", "error"), 2)


def to_rgb(image, background=(255, 255, 255)):
    """Flatten any PIL mode to RGB; alpha composites onto `background`."""
    from PIL import Image as PILImage

    if image.mode == "RGB":
        return image
    if "A" in image.getbands():
        image = image.convert("RGBA")
        flat = PILImage.new("RGB", image.size, background)
        flat.paste(image, mask=image.getchannel("A"))
        return flat
    return image.convert("RGB")


def _image_from_response(response):
    """First inline image part of a Gemini response as an RGB PIL image; None when absent."""
    from PIL import Image as PILImage

    for part in response.parts or []:
        if getattr(part, "text", None):
            print(f"Model text: {part.text.strip()[:300]}", file=sys.stderr)
        elif getattr(part, "inline_data", None) is not None:
            data = part.inline_data.data
            if isinstance(data, str):
                data = base64.b64decode(data)
            return to_rgb(PILImage.open(BytesIO(data)))
    return None


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

    started = time.time()
    last_error: Exception | None = None

    def failure(attempts: int) -> dict:
        return {"status": "error", **base, "attempts": attempts, "elapsed_seconds": round(time.time() - started, 1), "error": str(last_error)}

    try:
        from google.genai import types
        from PIL import Image as PILImage

        contents: list = []
        for ref in ref_paths:
            try:
                contents.append(PILImage.open(ref))
            except Exception as err:
                raise RuntimeError(f"reference image {ref.name} is not a readable image: {err}") from err
        if contents:
            contents.append(STYLE_NOTE)
        contents.append(prompt)
        config = types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(image_size=resolution, aspect_ratio=ratio),
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
        )
        client = (client_factory or _genai_client)(api_key)
    except Exception as err:
        last_error = err
        print(f"Setup failed: {err}", file=sys.stderr)
        return failure(0)
    for attempt in range(1, retries + 2):
        try:
            print(f"[{attempt}] {model} {ratio} {resolution} refs={len(ref_paths)}", file=sys.stderr)
            response = client.models.generate_content(model=model, contents=contents, config=config)
            image = _image_from_response(response)
            if image is None:
                raise RuntimeError("no image part in response (content may have been refused)")
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
    return failure(retries + 1)


# --- add ---

META_KEYS = {"member", "new_member", "shows", "flags", "pairings", "slug", "file", "variant", "item_count"}


def normalise_image(src: Path, dest: Path, max_edge: int = 1600, quality: int = 88) -> Path:
    """Copy `src` to `dest` as an RGB JPEG no larger than `max_edge` on its long side."""
    from PIL import Image as PILImage

    with PILImage.open(src) as image:
        image = to_rgb(image)
        width, height = image.size
        scale = max_edge / max(width, height)
        if scale < 1:
            image = image.resize((round(width * scale), round(height * scale)), PILImage.LANCZOS)
        dest.parent.mkdir(parents=True, exist_ok=True)
        image.save(str(dest), "JPEG", quality=quality, optimize=True)
    return dest


def _load_meta(meta_path: Path, cat: Catalogue) -> dict:
    meta = read_yaml(meta_path)
    if not isinstance(meta, dict):
        raise UsageError(f"{meta_path}: meta must be a mapping")
    unknown = sorted(set(meta) - META_KEYS)
    if unknown:
        raise UsageError(f"{meta_path}: unknown key(s) {', '.join(unknown)}")
    for key in ("shows", "flags"):
        if not meta.get(key):
            raise UsageError(f"{meta_path}: missing {key}")
    if bool(meta.get("member")) == bool(meta.get("new_member")):
        raise UsageError(f"{meta_path}: give exactly one of member or new_member")
    if not isinstance(meta["flags"], list) or not set(meta["flags"]) <= set(cat.flag_values):
        raise UsageError(f"{meta_path}: flags must be a list from {cat.flag_values}")
    pairings = meta.get("pairings") or []
    if not isinstance(pairings, list):
        raise UsageError(f"{meta_path}: pairings must be a list of layout names")
    new_name = (meta.get("new_member") or {}).get("name", "")
    bad = [layout for layout in pairings if not cat.is_layout(layout) and layout != new_name]
    if bad:
        raise UsageError(f"{meta_path}: unknown pairing layout(s) {', '.join(bad)}")
    meta["pairings"] = pairings
    if "item_count" in meta and (not isinstance(meta["item_count"], int) or isinstance(meta["item_count"], bool) or meta["item_count"] < 1):
        raise UsageError(f"{meta_path}: item_count must be a positive integer")
    if "variant" in meta and not isinstance(meta["variant"], str):
        raise UsageError(f"{meta_path}: variant must be a variant name from the member's layout.variants")
    return meta


def _check_variant(meta_path: Path, record: dict, variant: str | None) -> None:
    if variant is None:
        return
    names = [v["name"] for v in record["layout"]["variants"]]
    if variant not in names:
        raise UsageError(f"{meta_path}: unknown variant {variant!r} for {record['name']}; valid: {', '.join(names)}")


def _new_member_record(cat: Catalogue, block: dict, meta_path: Path) -> tuple[dict, list[str]]:
    block = dict(block)
    routing_rows = block.pop("routing", []) or []
    name = str(block.get("name", ""))
    if not MEMBER_NAME_RE.match(name):
        raise UsageError(f"{meta_path}: new_member.name must match {MEMBER_NAME_RE.pattern} (a path-safe slug), got {name!r}")
    if name in cat.members:
        raise UsageError(f"{meta_path}: member {name} already exists; use member: {name}")
    bad_rows = [row for row in routing_rows if row not in cat.routing]
    if bad_rows:
        raise UsageError(f"{meta_path}: unknown routing layout(s) {', '.join(bad_rows)}")
    block.setdefault("refs", [])
    block.setdefault("pairings", {})
    block.setdefault("alternates", [])
    block.setdefault("source", {"origin": f"user-added via iig3d.py add ({meta_path.name})", "added": time.strftime("%Y-%m-%d")})
    problems = validate_member(block, cat.schema)
    if problems:
        raise UsageError(f"{meta_path}: new_member invalid: " + "; ".join(problems))
    return block, routing_rows


def add_ref(cat: Catalogue, image: Path, meta_path: Path) -> dict:
    """Normalise an image into refs/<member>/, register it in the member YAML (or create the member),
    regenerate docs and report. Vendored entries are only ever extended, never edited, except a
    `file:` replacement for an entry whose image is missing on disk (R21 regeneration)."""
    image, meta_path = Path(image), Path(meta_path)
    if not image.is_file():
        raise UsageError(f"image not found: {image}")
    meta = _load_meta(meta_path, cat)
    routing_rows: list[str] = []
    if meta.get("new_member"):
        record, routing_rows = _new_member_record(cat, meta["new_member"], meta_path)
        name = record["name"]
    else:
        name = meta["member"]
        record = dict(cat.member(name).raw)
    refs = list(record["refs"])
    forced = meta.get("file")
    existing = next((r for r in refs if r["file"] == forced), None) if forced else None
    if forced and existing is None:
        raise UsageError(f"{meta_path}: file {forced} is not a catalogue entry of {name}; omit file to add a new ref")
    if existing is None:
        ref_id = f"{max((int(r['id']) for r in refs), default=0) + 1:02d}"
        file_name = f"ref-{ref_id}-{slugify(meta.get('slug') or image.stem)}.jpg"
    else:
        ref_id, file_name = existing["id"], existing["file"]
    source = {"path": str(image), "added": time.strftime("%Y-%m-%d"), "user_added": True}
    if existing is not None:
        source["regenerated"] = True
        previous = (existing.get("source") or {}).get("path")
        if previous and previous != str(image):
            source["derived_from"] = previous
    _check_variant(meta_path, record, meta.get("variant"))
    entry = {**(existing or {}), "id": ref_id, "file": file_name, "shows": meta["shows"], "flags": list(meta["flags"])}
    entry.pop("source", None)
    for key in ("variant", "item_count"):
        entry.pop(key, None)
        if meta.get(key) is not None:
            entry[key] = meta[key]
    entry["source"] = source
    dest = cat.ref_path(name, entry)
    if dest.exists():
        raise UsageError(f"{meta_path}: {file_name} already exists on disk; add never overwrites a vendored ref")
    if existing is None:
        refs.append(entry)
    else:
        refs[refs.index(existing)] = entry
    pairings = {k: list(v) for k, v in record["pairings"].items()}
    for layout in meta["pairings"]:
        pairings.setdefault(layout, [])
        if ref_id not in pairings[layout]:
            pairings[layout].append(ref_id)
    record["refs"], record["pairings"] = refs, pairings
    normalise_image(image, dest, max_edge=cat.family["ref_rules"]["max_long_edge_px"])
    member_yaml = cat.member_yaml(name)
    write_yaml(member_yaml, record)
    if routing_rows:
        family = read_yaml(cat.family_yaml)
        for row in routing_rows:
            alternates = family["routing"][row].setdefault("alternates", [])
            if name not in alternates:
                alternates.append(name)
        write_yaml(cat.family_yaml, family)
    fresh = load_catalogue(cat.root)
    docs = render_docs(fresh)
    # Report the new ref's own watermark (R21) and every other rule, but not watermarks the user
    # accepted on earlier refs; those are `check --allow-watermark` business.
    problems = [p for p in check(fresh) if "carries the watermark flag" not in p or file_name in p]
    return {
        "status": "ok" if not problems else "violations",
        "member": name,
        "ref_id": ref_id,
        "ref_file": str(dest),
        "pin": fresh.pin_token(name, entry),
        "yaml": str(member_yaml),
        "docs": [str(d) for d in docs],
        "check": problems,
    }


# --- docs ---

GENERATED_NOTE = "<!-- Generated by `iig3d.py docs` from catalogue/*.yaml. Do not edit by hand. -->"


def member_markdown(member: Member) -> str:
    style = member["style"]
    refs_rows = [[f"`{member.name}/{r['id']}`", f"`{r['file']}`", r["shows"].replace("|", "\\|"), r.get("variant") or "-", ", ".join(r["flags"])] for r in member.refs]
    pairings = [f"- `{layout_name}`: refs {', '.join(ids)}" for layout_name, ids in member.pairings.items()]
    layout = "\n\n".join(f"### {heading}\n\n{body}" for heading, body in layout_sections(member) if heading != "Best For")
    parts = [
        f"# {member.name}",
        GENERATED_NOTE,
        f"Member of the 3D corporate family. {member['device']}. Backdrop: {member['backdrop']}. Items: {member.items['min']} to {member.items['max']}. Default aspect: {member.aspect_default}.",
        "## Reference images\n\n" + _table(["Pin", "File", "Shows", "Variant", "Flags"], refs_rows) + "\n\nPin one with `pin: <Pin>` in the spec (or `--pin`) to reproduce its composition with your content.",
        "## Colour palette\n\n" + _bullets(style["palette"]),
        "## Visual elements\n\n" + _bullets(style["visual_elements"]),
        "## Typography\n\n" + _bullets(style["typography"]),
        "## Composition rules\n\n" + _bullets(style["composition"]),
        "## Layout\n\n" + layout,
        "## Prompt fragment\n\n```\n" + member.prompt_fragment.strip() + "\n```",
        "## Best for\n\n" + _bullets(member["best_for"]),
        "## Recommended pairings\n\n" + "\n".join(pairings) + "\n\nAlternates: " + ", ".join(f"`{a}`" for a in member.alternates),
        f"Source: {member['source']['origin']} (added {member['source']['added']}).",
    ]
    return "\n\n".join(parts) + "\n"


def catalogue_markdown(cat: Catalogue) -> str:
    family = cat.family
    members = [[f"`{m.name}`", m["device"], m["backdrop"], f"{m.items['min']}-{m.items['max']}", str(len(m.refs))] for m in cat.members.values()]
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
        docs[cat.root / "docs" / "members" / f"{member.name}.md"] = member_markdown(member)
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


def build_parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--skill-root", default=None, help="skill directory (default: this script's parent)")
    prepare_args = argparse.ArgumentParser(add_help=False)
    prepare_args.add_argument("--spec", required=True, help="YAML content spec")
    prepare_args.add_argument("--out-dir", required=True, help="output directory (prompts/ and infographic.png)")
    prepare_args.add_argument("--layout", default=None)
    prepare_args.add_argument("--style", default=None, help="3d-* member, industrial-3d, or a ref id/file of the member named by --layout")
    prepare_args.add_argument("--aspect", default=None, help="landscape | portrait | square | W:H")
    prepare_args.add_argument("--palette-css", default=None, help="CSS file whose colours replace the item colours")
    prepare_args.add_argument("--palette-vars", default=None, help="comma-separated custom properties to use, in order")
    prepare_args.add_argument("--ref", action="append", default=[], help="user reference image (repeatable)")
    prepare_args.add_argument("--pin", default=None, help="catalogue ref to reproduce: <member>/<id|file>, e.g. 3d-capsule-hub/06")
    prepare_args.add_argument("--no-style-refs", action="store_true", help="do not pass the member's bundled refs")
    prepare_args.add_argument("--strict", action="store_true", help="turn prompt warnings into exit 1")

    parser = argparse.ArgumentParser(prog="iig3d", description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", parents=[common], help="members and layouts")
    p_route = sub.add_parser("route", parents=[common], help="resolve layout and style to a member")
    p_route.add_argument("--layout", default=None)
    p_route.add_argument("--style", default=None, help="3d-* member, industrial-3d, or a ref of the --layout member")
    p_refs = sub.add_parser("refs", parents=[common], help="reference images for a member and layout")
    p_refs.add_argument("--member", required=True)
    p_refs.add_argument("--layout", default=None, help="default: the member's own device layout")
    p_refs.add_argument("--ref", action="append", default=[])
    p_refs.add_argument("--pin", default=None, help="catalogue ref to put first: <member>/<id|file> or <id|file>")
    sub.add_parser("prompt", parents=[common, prepare_args], help="assemble and persist the prompt file")
    p_render = sub.add_parser("render", parents=[common, prepare_args], help="assemble the prompt and render with Nano Banana Pro")
    p_render.add_argument("--dry-run", action="store_true")
    p_render.add_argument("--resolution", default="2K", choices=RESOLUTIONS)
    p_render.add_argument("--model", default=None)
    p_render.add_argument("--retries", type=int, default=1)
    p_render.add_argument("--api-key", default=None)
    p_render.add_argument("--no-confirm", action="store_true", help="accepted for parity with SKILL.md; no effect here")
    p_add = sub.add_parser("add", parents=[common], help="add a reference image to the catalogue")
    p_add.add_argument("--image", required=True)
    p_add.add_argument("--meta", required=True)
    sub.add_parser("docs", parents=[common], help="regenerate catalogue markdown")
    p_check = sub.add_parser("check", parents=[common], help="validate the catalogue, refs and docs")
    p_check.add_argument("--allow-watermark", action="store_true")
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
            "device": m["device"],
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
    layout = args.layout or spec.layout
    style, pin = split_style(cat, layout, args.style or spec.style, args.pin or spec.pin)
    pinned_member, pinned = cat.resolve_ref(pin, style) if pin else (None, None)
    route_ = route(cat, layout, style, pinned_member=pinned_member.name if pinned_member else None)
    member = cat.member(route_.member)
    ratio, snapped_from = snap_aspect(cat, args.aspect or spec.aspect, member.aspect_default)
    user_refs = [Path(r) for r in args.ref] + spec.refs
    refs = select_refs(cat, member.name, route_.layout, user_refs=user_refs, style_refs=not args.no_style_refs, pinned=pinned)
    css = Path(args.palette_css).resolve() if args.palette_css else spec.palette_css
    palette = None
    if css:
        vars_ = _split_vars(args.palette_vars) or spec.palette_vars
        palette = extract_palette(css, vars=vars_ or None)
    prompt = assemble(cat, spec, route_, ratio, refs=refs, palette=palette, palette_source=css, strict=args.strict, aspect_snapped_from=snapped_from, pinned=pinned)
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
        "pin": cat.pin_token(member.name, pinned) if pinned else None,
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


def cmd_route(cat: Catalogue, args: argparse.Namespace) -> dict:
    style, pin = split_style(cat, args.layout, args.style)
    pinned_member, pinned = cat.resolve_ref(pin, style) if pin else (None, None)
    route_ = route(cat, args.layout, style, pinned_member=pinned_member.name if pinned_member else None)
    return {"status": "ok", **route_.as_dict(), "pin": cat.pin_token(pinned_member.name, pinned) if pinned else None}


def cmd_refs(cat: Catalogue, args: argparse.Namespace) -> dict:
    """The refs a render would pass, plus every catalogue ref of the member with its pin token."""
    member = cat.member(args.member)
    layout = args.layout or member.name
    pinned = cat.resolve_ref(args.pin, member.name)[1] if args.pin else None
    return {
        "status": "ok",
        "member": member.name,
        "layout": layout,
        "pin": cat.pin_token(member.name, pinned) if pinned else None,
        "refs": [str(r) for r in select_refs(cat, member.name, layout, user_refs=[Path(r) for r in args.ref], pinned=pinned)],
        "available": [{"pin": cat.pin_token(member.name, r), "file": r["file"], "shows": r["shows"], "variant": r.get("variant"), "item_count": r.get("item_count"), "flags": r["flags"]} for r in member.refs],
    }


def cmd_palette(args: argparse.Namespace) -> dict:
    colours = extract_palette(Path(args.css), vars=_split_vars(args.vars) or None)
    return {"status": "ok", "source": str(Path(args.css).resolve()), "colours": [c.as_dict() for c in colours], "paragraph": palette_paragraph(colours)}


def cmd_check(cat: Catalogue, args: argparse.Namespace) -> dict:
    violations = check(cat, allow_watermark=args.allow_watermark)
    return {"status": "ok" if not violations else "violations", "violations": violations}


HANDLERS = {
    "list": lambda cat, args: cmd_list(cat),
    "route": cmd_route,
    "refs": cmd_refs,
    "prompt": prepare,
    "render": cmd_render,
    "add": lambda cat, args: add_ref(cat, Path(args.image), Path(args.meta)),
    "docs": lambda cat, args: {"status": "ok", "written": [str(p) for p in render_docs(cat)]},
    "check": cmd_check,
}


def dispatch(args: argparse.Namespace) -> dict:
    if args.command == "palette":
        return cmd_palette(args)
    return HANDLERS[args.command](load_catalogue(args.skill_root), args)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = dispatch(args)
    except UsageError as err:
        print(json.dumps({"status": "error", "error": str(err)}))
        return 1
    print(json.dumps(result))
    return exit_code(result)


# --- check ---


PEP723_BLOCK_RE = re.compile(r"^# /// script\n(.*?)^# ///$", re.MULTILINE | re.DOTALL)


def pep723_dependencies(script: Path) -> list[str]:
    """Dependencies from the script's inline metadata block, parsed as TOML per PEP 723."""
    match = PEP723_BLOCK_RE.search(script.read_text(encoding="utf-8"))
    if not match:
        return []
    toml = "\n".join(line[2:] if line.startswith("# ") else line[1:] for line in match.group(1).splitlines())
    return tomllib.loads(toml).get("dependencies", [])


def dependency_parity(skill_root: Path) -> list[str]:
    """The PEP 723 header and the repository pyproject.toml must list the same runtime packages."""
    script = Path(skill_root) / "scripts" / "iig3d.py"
    pyproject = Path(skill_root).parents[1] / "pyproject.toml"
    if not script.exists() or not pyproject.exists():
        return []
    inline = sorted(pep723_dependencies(script))
    declared = sorted(tomllib.loads(pyproject.read_text(encoding="utf-8"))["project"]["dependencies"])
    return [] if inline == declared else [f"dependency drift: script {inline} vs pyproject {declared}"]


def check(cat: Catalogue, allow_watermark: bool = False) -> list[str]:
    """Every catalogue rule in one pass; empty list means clean."""
    from PIL import Image as PILImage

    problems: list[str] = []
    max_edge = cat.family["ref_rules"]["max_long_edge_px"]
    for layout, row in cat.routing.items():
        for name in [row["primary"], *row["alternates"]]:
            if name not in cat.members:
                problems.append(f"routing {layout}: unknown member {name}")
    for name, member in cat.members.items():
        if not has_negative_list(member.prompt_fragment, cat):
            problems.append(f"{name}: prompt fragment does not end with the family negative list")
        if member.items["min"] > member.items["max"]:
            problems.append(f"{name}: items min {member.items['min']} > max {member.items['max']}")
        ids = set()
        for ref in member.refs:
            ids.add(ref["id"])
            if "watermark" in ref["flags"]:
                user_added = bool(ref.get("source", {}).get("user_added"))
                if not (allow_watermark and user_added):
                    kind = "user-added ref" if user_added else "vendored ref"
                    hint = "; pass --allow-watermark to accept it" if user_added else ""
                    problems.append(f"{name}/{ref['file']}: {kind} carries the watermark flag{hint}")
            path = cat.ref_path(name, ref)
            if not path.is_file():
                problems.append(f"{name}/{ref['file']}: missing on disk")
                continue
            try:
                with PILImage.open(path) as image:
                    if image.format != "JPEG":
                        problems.append(f"{name}/{ref['file']}: not JPEG ({image.format})")
                    if max(image.size) > max_edge:
                        problems.append(f"{name}/{ref['file']}: long edge {max(image.size)} px over {max_edge}")
            except OSError as err:
                problems.append(f"{name}/{ref['file']}: unreadable ({err})")
        for alt in member.alternates:
            if alt not in cat.members or alt == name:
                problems.append(f"{name}: bad alternate {alt}")
        for layout, ref_ids in member.pairings.items():
            if not cat.is_layout(layout):
                problems.append(f"{name}: pairing for unknown layout {layout}")
            for rid in ref_ids:
                if rid not in ids:
                    problems.append(f"{name}: pairing {layout} names unknown ref {rid}")
    problems += stale_docs(cat)
    problems += dependency_parity(cat.root)
    problems += _dry_assembly(cat)
    return problems


def _dry_assembly(cat: Catalogue) -> list[str]:
    """Assemble a prompt for every member x pairing layout; report ref-rule violations."""
    problems: list[str] = []
    spec = Spec(title="CHECK", items=[Item(label=f"ITEM {i}") for i in range(1, 6)])
    for name, member in cat.members.items():
        for layout in list(member.pairings) or [name]:
            try:
                problems += [f"{name}/{layout}: {p}" for p in ref_rule_violations(pick_style_refs(cat, member, layout))]
                refs = select_refs(cat, name, layout)
                assemble(cat, spec, route(cat, layout, name), cat.family["aspect_map"][member.aspect_default], refs=refs)
            except UsageError as err:
                problems.append(f"{name}/{layout}: {err}")
    return problems


if __name__ == "__main__":
    sys.exit(main())
