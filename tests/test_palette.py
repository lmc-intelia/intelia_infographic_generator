"""R20: brand colours extracted from a CSS file replace item colours only."""

from __future__ import annotations

import pytest


@pytest.fixture(scope="module")
def cat(iig3d, skill_root):
    return iig3d.load_catalogue(skill_root)


def test_extraction_order_and_normalisation(iig3d, fixtures):
    colours = iig3d.extract_palette(fixtures / "brand.css")
    assert [c.name for c in colours][:3] == ["brand-primary", "brand-secondary", "brand-accent"]
    assert colours[0].hex == "#1F3A5F"
    assert colours[1].hex == "#1FB5C8"
    assert colours[2].hex.startswith("#F")
    assert len(colours) == 8
    assert all(len(c.hex) == 7 and c.hex.upper() == c.hex for c in colours)


def test_neutrals_and_duplicates_dropped(iig3d, fixtures):
    hexes = [c.hex for c in iig3d.extract_palette(fixtures / "brand.css")]
    names = [c.name for c in iig3d.extract_palette(fixtures / "brand.css")]
    assert "#9AA3AE" not in hexes and "#FFFFFF" not in hexes and "#111111" not in hexes
    assert "brand-primary-dup" not in names
    assert hexes.count("#1F3A5F") == 1


def test_bare_literals_used_after_custom_properties(iig3d, tmp_path):
    css = tmp_path / "a.css"
    css.write_text(":root{--a:#E2312A;--b:#2456C4;} .x{color:#8CC63F} .y{background:rgb(245,133,31)}")
    colours = iig3d.extract_palette(css)
    assert [c.name for c in colours] == ["a", "b", "colour-3", "colour-4"]
    assert colours[3].hex == "#F5851F"


def test_vars_restricts_and_orders(iig3d, fixtures):
    colours = iig3d.extract_palette(fixtures / "brand.css", vars=["--brand-lime", "brand-primary", "--brand-red"])
    assert [c.name for c in colours] == ["brand-lime", "brand-primary", "brand-red"]


def test_unknown_var_named(iig3d, fixtures):
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.extract_palette(fixtures / "brand.css", vars=["--brand-lime", "--nope", "--brand-red"])
    assert "--nope" in str(err.value)


def test_fewer_than_three_fails_naming_file(iig3d, tmp_path):
    css = tmp_path / "thin.css"
    css.write_text(":root{--a:#E2312A;--b:#ccc;}")
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.extract_palette(css)
    assert "thin.css" in str(err.value)


def test_missing_file_named(iig3d, tmp_path):
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.extract_palette(tmp_path / "gone.css")
    assert "gone.css" in str(err.value)


def test_paragraph(iig3d, fixtures):
    colours = iig3d.extract_palette(fixtures / "brand.css", vars=["--brand-primary", "--brand-secondary", "--brand-accent"])
    text = iig3d.palette_paragraph(colours)
    assert text.startswith("Project palette override: cycle item colours in this order: brand-primary #1F3A5F, brand-secondary #1FB5C8, brand-accent")
    assert text.endswith("never repeat a colour on adjacent items; keep the family backdrop, neutrals, shadows and typography unchanged.")


def test_colour_helpers(iig3d):
    assert iig3d.normalise_colour("#abc") == "#AABBCC"
    assert iig3d.normalise_colour("rgb(255, 0, 0)") == "#FF0000"
    assert iig3d.normalise_colour("hsl(0 100% 50%)") == "#FF0000"
    assert iig3d.normalise_colour("#12345680") == "#123456"
    assert iig3d.is_neutral("#9AA3AE") and iig3d.is_neutral("#FFFFFF") and iig3d.is_neutral("#050505")
    assert not iig3d.is_neutral("#1FB5C8")
