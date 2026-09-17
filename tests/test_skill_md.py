"""R1, R12: SKILL.md is short, triggers correctly, lists every subcommand, states the gates."""

from __future__ import annotations

import re

import yaml


def frontmatter(text: str) -> dict:
    assert text.startswith("---\n")
    return yaml.safe_load(text.split("---\n")[1])


def test_frontmatter_and_length(skill_root, iig3d):
    text = (skill_root / "SKILL.md").read_text()
    meta = frontmatter(text)
    assert meta["name"] == "iig3d"
    for phrase in ("3d infographic", "industrial 3d", "iig3d"):
        assert phrase in meta["description"].lower(), phrase
    assert len(text.splitlines()) <= 80


def test_commands_table_and_rules(skill_root, iig3d):
    text = (skill_root / "SKILL.md").read_text()
    for command in iig3d.SUBCOMMANDS:
        assert re.search(rf"`[^`]*iig3d\.py {command}\b", text), command
    assert "Confirm member, layout, aspect and language once before render" in text
    assert "Load a CSS file for brand colours?" in text
    assert "--no-confirm" in text and "./.env" in text and "GEMINI_API_KEY" in text
    assert "never emit svg" in text.lower() or "never substitute svg" in text.lower()
    assert "never paint over rendered text" in text.lower()
    assert "meta.yaml" in text and "add" in text


def test_spec_example_loads(skill_root, iig3d):
    spec = iig3d.load_spec(skill_root / "templates" / "spec.example.yaml")
    assert spec.title and len(spec.items) == 5
    meta = yaml.safe_load((skill_root / "templates" / "meta.example.yaml").read_text())
    assert {"member", "shows", "flags", "pairings"} <= set(meta)
