"""R11: dry-run shape, PNG save, backup rename, retries, exit codes; live smoke gated."""

from __future__ import annotations

import os
import re

import pytest

from tests.conftest import png_bytes

KEYS = {"status", "path", "bytes", "model", "aspect_ratio", "resolution", "refs", "attempts", "elapsed_seconds", "prompt_file", "warnings", "logo"}


@pytest.fixture
def prompt_file(tmp_path):
    p = tmp_path / "prompts" / "01-infographic-x.md"
    p.parent.mkdir()
    p.write_text("---\nlayout: dashboard\n---\nCreate an infographic.\n")
    return p


def test_dry_run_shape_and_no_file(iig3d, tmp_path, prompt_file, fake_client):
    out = tmp_path / "infographic.png"
    result = iig3d.render(prompt_file, out, "16:9", dry_run=True, api_key="k", client_factory=fake_client)
    assert result["status"] == "dry-run"
    assert set(result) >= KEYS
    assert result["resolution"] == "2K" and result["model"] == iig3d.DEFAULT_MODEL
    assert not out.exists() and fake_client.calls == []


def test_saves_png_and_flattens_rgba(iig3d, tmp_path, prompt_file, fake_client):
    from PIL import Image

    fake_client.behaviour = [png_bytes("RGBA")]
    out = tmp_path / "out" / "infographic.png"
    result = iig3d.render(prompt_file, out, "16:9", api_key="k", client_factory=fake_client)
    assert result["status"] == "ok" and result["attempts"] == 1
    assert result["path"] == str(out.resolve()) and result["bytes"] == out.stat().st_size
    assert Image.open(out).mode == "RGB"
    call = fake_client.calls[0]
    assert call["model"] == iig3d.DEFAULT_MODEL
    assert call["config"].image_config.aspect_ratio == "16:9"
    assert call["config"].image_config.image_size == "2K"
    assert call["contents"][-1] == "Create an infographic."


def test_refs_passed_as_images_with_style_note(iig3d, tmp_path, prompt_file, fake_client, tmp_catalogue):
    from PIL import Image

    refs = iig3d.select_refs(tmp_catalogue, "3d-paper-tile", "hub-spoke")
    out = tmp_path / "infographic.png"
    result = iig3d.render(prompt_file, out, "1:1", refs=refs, api_key="k", client_factory=fake_client)
    contents = fake_client.calls[0]["contents"]
    assert all(isinstance(c, Image.Image) for c in contents[: len(refs)])
    assert contents[len(refs)].startswith("The images above are style references only")
    assert result["refs"] == len(refs)


def test_backup_rename_on_rerun(iig3d, tmp_path, prompt_file, fake_client):
    fake_client.behaviour = [png_bytes(), png_bytes()]
    out = tmp_path / "infographic.png"
    iig3d.render(prompt_file, out, "16:9", api_key="k", client_factory=fake_client)
    iig3d.render(prompt_file, out, "16:9", api_key="k", client_factory=fake_client)
    backups = [p.name for p in tmp_path.iterdir() if p.name.startswith("infographic-backup-")]
    assert len(backups) == 1 and re.fullmatch(r"infographic-backup-\d{8}-\d{6}\.png", backups[0])
    assert out.exists()


def test_retry_then_error(iig3d, tmp_path, prompt_file, fake_client, monkeypatch):
    monkeypatch.setattr(iig3d.time, "sleep", lambda s: None)
    fake_client.behaviour = [RuntimeError("boom"), RuntimeError("boom again")]
    out = tmp_path / "infographic.png"
    result = iig3d.render(prompt_file, out, "16:9", retries=1, api_key="k", client_factory=fake_client)
    assert result["status"] == "error" and "boom again" in result["error"]
    assert len(fake_client.calls) == 2 and iig3d.exit_code(result) == 2


def test_retry_then_success(iig3d, tmp_path, prompt_file, fake_client, monkeypatch):
    monkeypatch.setattr(iig3d.time, "sleep", lambda s: None)
    fake_client.behaviour = [RuntimeError("boom"), png_bytes()]
    result = iig3d.render(prompt_file, tmp_path / "i.png", "16:9", retries=1, api_key="k", client_factory=fake_client)
    assert result["status"] == "ok" and result["attempts"] == 2


def test_no_image_part_is_error(iig3d, tmp_path, prompt_file, fake_client, monkeypatch):
    monkeypatch.setattr(iig3d.time, "sleep", lambda s: None)
    fake_client.behaviour = [None, None]
    result = iig3d.render(prompt_file, tmp_path / "i.png", "16:9", retries=1, api_key="k", client_factory=fake_client)
    assert result["status"] == "error" and "no image part" in result["error"]


def test_exit_codes(iig3d):
    assert iig3d.exit_code({"status": "ok"}) == 0
    assert iig3d.exit_code({"status": "dry-run"}) == 0
    assert iig3d.exit_code({"status": "error"}) == 2


def test_bad_resolution_rejected(iig3d, tmp_path, prompt_file, fake_client):
    with pytest.raises(iig3d.UsageError):
        iig3d.render(prompt_file, tmp_path / "i.png", "16:9", resolution="8K", api_key="k", client_factory=fake_client)


@pytest.mark.skipif(not os.environ.get("IIG3D_LIVE"), reason="set IIG3D_LIVE=1 to call Gemini")
def test_live_smoke(iig3d, tmp_path, prompt_file):
    key, _ = iig3d.api_key(None)
    result = iig3d.render(prompt_file, tmp_path / "live.png", "16:9", resolution="1K", api_key=key)
    assert result["status"] == "ok"


def test_bad_ref_image_is_error_not_traceback(iig3d, tmp_path, prompt_file, fake_client, monkeypatch):
    """Review finding: failures before the API call must still yield the error record (exit 2)."""
    monkeypatch.setattr(iig3d.time, "sleep", lambda s: None)
    bad = tmp_path / "notes.txt"
    bad.write_text("not an image")
    result = iig3d.render(prompt_file, tmp_path / "i.png", "16:9", refs=[bad], retries=0, api_key="k", client_factory=fake_client)
    assert result["status"] == "error" and "notes.txt" in result["error"] and iig3d.exit_code(result) == 2


def test_client_factory_failure_is_error(iig3d, tmp_path, prompt_file):
    def boom(_key):
        raise RuntimeError("client refused")

    result = iig3d.render(prompt_file, tmp_path / "i.png", "16:9", retries=0, api_key="k", client_factory=boom)
    assert result["status"] == "error" and "client refused" in result["error"]


def test_quality_levels_are_one_model_and_its_image_sizes(iig3d):
    assert tuple(iig3d.QUALITY) == ("1K", "2K", "4K") == iig3d.RESOLUTIONS
    for level in iig3d.RESOLUTIONS:
        assert iig3d.QUALITY[level]["model"] == iig3d.DEFAULT_MODEL and iig3d.QUALITY[level]["image_size"] == level


def test_1k_uses_pro_model_with_image_size(iig3d, tmp_path, prompt_file, fake_client):
    fake_client.behaviour = [png_bytes("RGB")]
    result = iig3d.render(prompt_file, tmp_path / "d.png", "16:9", resolution="1K", api_key="k", client_factory=fake_client)
    assert result["status"] == "ok" and result["quality"] == "1K" and result["image_size"] == "1K"
    call = fake_client.calls[0]
    assert call["model"] == iig3d.DEFAULT_MODEL
    assert call["config"].image_config.aspect_ratio == "16:9" and call["config"].image_config.image_size == "1K"


def test_4k_uses_pro_model_with_image_size(iig3d, tmp_path, prompt_file, fake_client):
    fake_client.behaviour = [png_bytes("RGB")]
    result = iig3d.render(prompt_file, tmp_path / "p.png", "16:9", resolution="4K", api_key="k", client_factory=fake_client)
    assert result["model"] == iig3d.DEFAULT_MODEL and result["image_size"] == "4K"
    assert fake_client.calls[0]["config"].image_config.image_size == "4K"


def test_explicit_model_overrides_quality_model(iig3d, tmp_path, prompt_file, fake_client):
    result = iig3d.render(prompt_file, tmp_path / "m.png", "16:9", resolution="1K", model="custom-image", dry_run=True, api_key="k", client_factory=fake_client)
    assert result["model"] == "custom-image" and result["quality"] == "1K"


def test_logo_stamped_bottom_left_with_5px_padding(iig3d, tmp_path):
    from PIL import Image

    logo = tmp_path / "logo.png"
    Image.new("RGBA", (40, 20), (255, 0, 0, 255)).save(logo)
    canvas = Image.new("RGB", (400, 300), (255, 255, 255))
    out = iig3d.stamp_logo(canvas, logo, pad=5, height_fraction=0.10, shadow=False)
    assert out.mode == "RGB" and out.size == (400, 300)
    # 10 percent of 300 = 30 px high, aspect kept: 60 px wide; box (5, 265) to (64, 294)
    assert out.getpixel((5, 294)) == (255, 0, 0) and out.getpixel((64, 265)) == (255, 0, 0)
    assert out.getpixel((4, 294)) == (255, 255, 255) and out.getpixel((5, 295)) == (255, 255, 255)
    assert out.getpixel((65, 265)) == (255, 255, 255) and out.getpixel((5, 264)) == (255, 255, 255)


def test_bundled_logo_exists_and_is_transparent(iig3d):
    from PIL import Image

    assert iig3d.LOGO_PATH.is_file()
    with Image.open(iig3d.LOGO_PATH) as im:
        assert im.mode == "RGBA" and im.getextrema()[3][0] == 0


def test_render_stamps_bundled_logo_by_default(iig3d, tmp_path, prompt_file, fake_client):
    from PIL import Image

    fake_client.behaviour = [png_bytes("RGB", (400, 300))]
    out = tmp_path / "infographic.png"
    result = iig3d.render(prompt_file, out, "16:9", api_key="k", client_factory=fake_client)
    assert result["status"] == "ok" and result["logo"] == str(iig3d.LOGO_PATH.resolve())
    im = Image.open(out)
    from PIL import ImageChops

    box = im.crop((5, 300 - 5 - 18, 5 + 22, 295))  # 6 percent of 300 = 18 px high, logo aspect about 1.2
    assert ImageChops.difference(box, Image.new("RGB", box.size, (10, 20, 30))).getbbox() is not None  # logo pixels in the corner box
    assert im.getpixel((200, 150)) == (10, 20, 30) and im.getpixel((2, 298)) == (10, 20, 30)


def test_render_without_logo(iig3d, tmp_path, prompt_file, fake_client):
    from PIL import Image

    fake_client.behaviour = [png_bytes("RGB", (400, 300))]
    out = tmp_path / "plain.png"
    result = iig3d.render(prompt_file, out, "16:9", api_key="k", client_factory=fake_client, logo=None)
    assert result["logo"] is None and Image.open(out).getpixel((5, 294)) == (10, 20, 30)


def test_missing_logo_rejected(iig3d, tmp_path, prompt_file, fake_client):
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.render(prompt_file, tmp_path / "x.png", "16:9", api_key="k", client_factory=fake_client, logo=tmp_path / "nope.png")
    assert "logo not found" in str(err.value)


def test_resolve_logo(iig3d, monkeypatch, tmp_path):
    monkeypatch.delenv("IIG3D_LOGO", raising=False)
    assert iig3d.resolve_logo(None) == iig3d.LOGO_PATH
    assert iig3d.resolve_logo("none") is None and iig3d.resolve_logo("") is None
    assert iig3d.resolve_logo(str(tmp_path / "a.png")) == tmp_path / "a.png"
    monkeypatch.setenv("IIG3D_LOGO", "none")
    assert iig3d.resolve_logo(None) is None
    monkeypatch.setenv("IIG3D_LOGO", str(tmp_path / "b.png"))
    assert iig3d.resolve_logo(None) == tmp_path / "b.png"


def test_logo_drop_shadow_darkens_below_right_only(iig3d, tmp_path):
    from PIL import Image

    logo = tmp_path / "logo.png"
    Image.new("RGBA", (60, 60), (255, 0, 0, 255)).save(logo)
    canvas = Image.new("RGB", (400, 300), (255, 255, 255))
    plain = iig3d.stamp_logo(canvas, logo, pad=20, height_fraction=0.20, shadow=False)
    shaded = iig3d.stamp_logo(canvas, logo, pad=20, height_fraction=0.20)
    # logo box: (20, 220) to (79, 279); shadow falls a few px down and right of it
    assert shaded.getpixel((50, 250)) == (255, 0, 0) == plain.getpixel((50, 250))
    below = shaded.getpixel((50, 283))
    right = shaded.getpixel((83, 250))
    assert below[0] < 255 and right[0] < 255 and below == plain.getpixel((50, 283))[:0] + below
    assert plain.getpixel((50, 283)) == (255, 255, 255) and plain.getpixel((83, 250)) == (255, 255, 255)
    assert shaded.getpixel((10, 210)) == (255, 255, 255)  # far top-left of the logo stays untouched
    assert shaded.getpixel((300, 100)) == (255, 255, 255)
