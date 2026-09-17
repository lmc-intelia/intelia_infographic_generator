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
