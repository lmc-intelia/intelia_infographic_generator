"""R1, R11, R16: the script imports as a module and exposes the subcommand table."""

from __future__ import annotations

import json

import pytest

SUBCOMMANDS = ["list", "route", "refs", "prompt", "render", "add", "docs", "check", "palette"]


def test_module_imports_and_has_main(iig3d):
    assert callable(iig3d.main)
    assert iig3d.SUBCOMMANDS == SUBCOMMANDS


def run(iig3d, capsys, argv):
    code = iig3d.main(argv)
    out, _err = capsys.readouterr()
    lines = [line for line in out.splitlines() if line.strip()]
    assert len(lines) == 1, out
    return code, json.loads(lines[0])


def test_list_counts(iig3d, capsys):
    code, data = run(iig3d, capsys, ["list"])
    assert code == 0
    assert len(data["members"]) == 12 and len(data["layouts"]) == 21
    member = data["members"][0]
    assert set(member) >= {"name", "device", "items", "aspect_default", "refs"}
    assert data["layouts"][0]["primary"] in {m["name"] for m in data["members"]}


def test_route_shape(iig3d, capsys):
    code, data = run(iig3d, capsys, ["route", "--layout", "hierarchical-layers"])
    assert code == 0 and data["member"] == "3d-slab-stack"
    assert data["alternates"] == ["3d-glass-layer", "3d-isometric-light", "3d-cylinder-column"]


def test_refs_shape(iig3d, capsys, tmp_catalogue):
    code, data = run(iig3d, capsys, ["refs", "--member", "3d-paper-tile", "--layout", "hub-spoke", "--skill-root", str(tmp_catalogue.root)])
    assert code == 0 and [r.rsplit("/", 1)[-1] for r in data["refs"]] == ["ref-02-semicircle-tabs.jpg", "ref-03-hexagon-tree.jpg"]


def test_palette_shape(iig3d, capsys, fixtures):
    code, data = run(iig3d, capsys, ["palette", "--css", str(fixtures / "brand.css")])
    assert code == 0 and len(data["colours"]) == 8 and data["colours"][0] == {"name": "brand-primary", "hex": "#1F3A5F"}


def test_prompt_writes_file(iig3d, capsys, fixtures, tmp_path, tmp_catalogue):
    code, data = run(iig3d, capsys, ["prompt", "--spec", str(fixtures / "spec-pipeline.yaml"), "--out-dir", str(tmp_path), "--skill-root", str(tmp_catalogue.root)])
    assert code == 0 and data["status"] == "ok"
    assert data["prompt_file"].endswith("prompts/01-infographic-openwiki-refresh-pipeline.md")
    assert data["member"] == "3d-disc-timeline" and data["aspect_ratio"] == "16:9" and data["warnings"] == []
    assert len(data["refs"]) == 2


def test_render_dry_run(iig3d, capsys, fixtures, tmp_path, tmp_catalogue, monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "k")
    code, data = run(
        iig3d,
        capsys,
        ["render", "--spec", str(fixtures / "spec-pipeline.yaml"), "--out-dir", str(tmp_path), "--dry-run", "--skill-root", str(tmp_catalogue.root), "--no-confirm"],
    )
    assert code == 0 and data["status"] == "dry-run"
    assert data["prompt_file"].endswith("01-infographic-openwiki-refresh-pipeline.md")
    assert (tmp_path / "prompts" / "01-infographic-openwiki-refresh-pipeline.md").exists()
    assert data["refs"] == 2 and data["member"] == "3d-disc-timeline"


def test_render_without_key_exits_1(iig3d, capsys, fixtures, tmp_path, tmp_catalogue, monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    monkeypatch.chdir(tmp_path)
    code, data = run(iig3d, capsys, ["render", "--spec", str(fixtures / "spec-pipeline.yaml"), "--out-dir", "out", "--dry-run", "--skill-root", str(tmp_catalogue.root)])
    assert code == 1 and data["status"] == "error"
    assert data["error"] == f"no API key: expected GEMINI_API_KEY in {tmp_path / '.env'} or the environment"


def test_render_with_fake_client(iig3d, capsys, fixtures, tmp_path, tmp_catalogue, fake_client, monkeypatch):
    monkeypatch.setattr(iig3d, "_genai_client", fake_client)
    code, data = run(
        iig3d,
        capsys,
        ["render", "--spec", str(fixtures / "spec-pipeline.yaml"), "--out-dir", str(tmp_path), "--api-key", "k", "--skill-root", str(tmp_catalogue.root), "--palette-css", str(fixtures / "brand.css")],
    )
    assert code == 0 and data["status"] == "ok"
    assert (tmp_path / "infographic.png").exists()
    assert "Project palette override" in (tmp_path / "prompts" / "01-infographic-openwiki-refresh-pipeline.md").read_text()


def test_usage_error_is_json_exit_1(iig3d, capsys):
    code, data = run(iig3d, capsys, ["route", "--layout", "spiral"])
    assert code == 1 and data["status"] == "error" and "spiral" in data["error"]


def test_render_requires_out_dir(iig3d, capsys, fixtures):
    with pytest.raises(SystemExit):
        iig3d.main(["render", "--spec", str(fixtures / "spec-pipeline.yaml")])
    capsys.readouterr()


@pytest.mark.parametrize("argv", [["docs"], ["check"], ["add", "--image", "x.jpg", "--meta", "m.yaml"]])
def test_remaining_commands_print_one_json(iig3d, capsys, argv):
    code, data = run(iig3d, capsys, argv)
    assert "status" in data and code in (0, 1)


def test_refs_lists_pins_and_layout_optional(iig3d, capsys, tmp_catalogue):
    code, data = run(iig3d, capsys, ["refs", "--member", "3d-capsule-hub", "--skill-root", str(tmp_catalogue.root)])
    assert code == 0 and data["layout"] == "3d-capsule-hub" and data["pin"] is None
    pins = [a["pin"] for a in data["available"]]
    assert pins == [f"3d-capsule-hub/{i:02d}" for i in range(1, 7)]
    assert {"pin", "file", "shows", "variant", "item_count", "flags"} <= set(data["available"][0])


def test_refs_with_pin(iig3d, capsys, tmp_catalogue):
    code, data = run(iig3d, capsys, ["refs", "--member", "3d-capsule-hub", "--layout", "hub-spoke", "--pin", "06", "--skill-root", str(tmp_catalogue.root)])
    assert code == 0 and data["pin"] == "3d-capsule-hub/06"
    assert data["refs"][0].endswith("ref-06-capsule-hierarchy.jpg")


def test_prompt_with_pin_flag(iig3d, capsys, fixtures, tmp_path, tmp_catalogue):
    args = ["prompt", "--spec", str(fixtures / "spec-pipeline.yaml"), "--out-dir", str(tmp_path), "--skill-root", str(tmp_catalogue.root)]
    code, data = run(iig3d, capsys, [*args, "--pin", "3d-disc-timeline/03"])
    assert code == 0 and data["pin"] == "3d-disc-timeline/03" and data["member"] == "3d-disc-timeline"
    assert data["refs"][0].endswith("ref-03-disc-chain-track.jpg")
    text = (tmp_path / "prompts" / "01-infographic-openwiki-refresh-pipeline.md").read_text()
    assert "## Reference Composition" in text and "usage: replicate" in text


def test_prompt_pin_conflicting_style_exits_1(iig3d, capsys, fixtures, tmp_path, tmp_catalogue):
    args = ["prompt", "--spec", str(fixtures / "spec-pipeline.yaml"), "--out-dir", str(tmp_path), "--skill-root", str(tmp_catalogue.root)]
    code, data = run(iig3d, capsys, [*args, "--pin", "3d-capsule-hub/06"])  # spec style is 3d-disc-timeline
    assert code == 1 and "conflicts" in data["error"]
