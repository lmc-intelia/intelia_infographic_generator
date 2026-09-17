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

SUBCOMMANDS = ["list", "route", "refs", "prompt", "render", "add", "docs", "check", "palette"]


class UsageError(Exception):
    """Bad input: exit code 1, message on stdout as JSON."""


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
