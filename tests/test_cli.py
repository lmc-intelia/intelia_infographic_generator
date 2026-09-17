"""R1, R11, R16: the script imports as a module and exposes the subcommand table."""

from __future__ import annotations

SUBCOMMANDS = ["list", "route", "refs", "prompt", "render", "add", "docs", "check", "palette"]


def test_module_imports_and_has_main(iig3d):
    assert callable(iig3d.main)
    assert iig3d.SUBCOMMANDS == SUBCOMMANDS
