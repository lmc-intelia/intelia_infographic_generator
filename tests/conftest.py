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
