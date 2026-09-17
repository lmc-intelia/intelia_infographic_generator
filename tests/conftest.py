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


class FakeInline:
    def __init__(self, data: bytes):
        self.data = data


class FakePart:
    def __init__(self, text=None, data: bytes | None = None):
        self.text = text
        self.inline_data = FakeInline(data) if data is not None else None


class FakeResponse:
    def __init__(self, parts):
        self.parts = parts


class FakeModels:
    """Records generate_content calls; behaviour is a list consumed per call: bytes, Exception, or None."""

    def __init__(self, behaviour):
        self.behaviour = list(behaviour)
        self.calls = []

    def generate_content(self, model, contents, config):
        self.calls.append({"model": model, "contents": contents, "config": config})
        step = self.behaviour.pop(0) if self.behaviour else None
        if isinstance(step, Exception):
            raise step
        if step is None:
            return FakeResponse([FakePart(text="refused")])
        return FakeResponse([FakePart(text="ok"), FakePart(data=step)])


class FakeClient:
    def __init__(self, behaviour):
        self.models = FakeModels(behaviour)


def png_bytes(mode: str = "RGB", size=(16, 12)) -> bytes:
    import io

    from PIL import Image

    buf = io.BytesIO()
    Image.new(mode, size, (10, 20, 30, 128) if mode == "RGBA" else (10, 20, 30)).save(buf, "PNG")
    return buf.getvalue()


@pytest.fixture
def fake_client():
    """Return a factory(api_key) -> FakeClient with the given behaviour list; exposes the last client."""

    class Factory:
        def __init__(self):
            self.behaviour = [png_bytes()]
            self.clients = []

        def __call__(self, api_key):
            client = FakeClient(self.behaviour)
            self.clients.append(client)
            return client

        @property
        def calls(self):
            return [c for client in self.clients for c in client.models.calls]

    return Factory()
