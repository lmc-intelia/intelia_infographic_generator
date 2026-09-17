"""Shared fixtures: import the single-file skill script as a module."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "skills" / "iig3d"
SCRIPT = SKILL / "scripts" / "iig3d.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


def load_module():
    spec = importlib.util.spec_from_file_location("iig3d", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["iig3d"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="session")
def iig3d():
    return load_module()


@pytest.fixture(scope="session")
def skill_root() -> Path:
    return SKILL


@pytest.fixture(scope="session")
def fixtures() -> Path:
    return FIXTURES


@pytest.fixture
def tmp_catalogue(tmp_path, iig3d):
    """A copy of the shipped catalogue in a temp skill root with a small JPEG for every ref."""
    import shutil

    from PIL import Image

    root = tmp_path / "skill"
    shutil.copytree(SKILL / "catalogue", root / "catalogue")
    for template in ("templates", "docs"):
        if (SKILL / template).exists():
            shutil.copytree(SKILL / template, root / template)
    cat = iig3d.load_catalogue(root)
    for name, member in cat.members.items():
        for ref in member.refs:
            target = root / "refs" / name / ref["file"]
            target.parent.mkdir(parents=True, exist_ok=True)
            Image.new("RGB", (64, 40), (200, 120, 40)).save(target, "JPEG")
    return iig3d.load_catalogue(root)
