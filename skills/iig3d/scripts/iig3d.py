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
import json
import re
import sys
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

    def as_dict(self) -> dict:
        return {"member": self.member, "layout": self.layout, "alternates": list(self.alternates), "reason": self.reason}


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
        return Route(style, layout or style, list(member.alternates), f"explicit member style {style}")
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


# --- cli ---


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="iig3d", description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    for name in SUBCOMMANDS:
        sub.add_parser(name)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        raise NotImplementedError(args.command)
    except UsageError as err:
        print(json.dumps({"status": "error", "error": str(err)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
