"""Typography schema: family fonts per role, spec overrides, one Typography section in the prompt."""

from __future__ import annotations

import pytest


@pytest.fixture(scope="module")
def cat(iig3d, skill_root):
    return iig3d.load_catalogue(skill_root)


def test_family_declares_title_and_body(iig3d, cat):
    fonts = iig3d.resolve_fonts(cat)
    assert {"title", "body"} <= set(fonts)
    assert fonts["title"]["family"] and fonts["body"]["family"]
    assert fonts["title"]["case"] == "upper" and fonts["body"]["weight"] == "light"


def test_parse_fonts_shapes(iig3d):
    assert iig3d.parse_fonts(None, "x") == {}
    assert iig3d.parse_fonts({"title": "Inter"}, "x") == {"title": {"family": "Inter"}}
    assert iig3d.parse_fonts({"body": {"family": "Inter", "weight": "regular"}}, "x") == {"body": {"family": "Inter", "weight": "regular"}}
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.parse_fonts({"footer": "Inter"}, "spec: fonts")
    assert "unknown role 'footer'" in str(err.value)
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.parse_fonts({"title": {"typeface": "Inter"}}, "spec: fonts")
    assert "unknown field(s) typeface" in str(err.value)
    with pytest.raises(iig3d.UsageError):
        iig3d.parse_fonts(["Inter"], "spec: fonts")


def test_spec_overrides_merge_per_field(iig3d, cat, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: T\nfonts:\n  title: {family: Inter, weight: extrabold}\n  body: Inter\nitems:\n  - label: A\n")
    spec = iig3d.load_spec(path)
    fonts = iig3d.resolve_fonts(cat, spec.fonts)
    assert fonts["title"]["family"] == "Inter" and fonts["title"]["weight"] == "extrabold" and fonts["title"]["case"] == "upper"
    assert fonts["body"]["family"] == "Inter" and fonts["body"]["weight"] == "light"
    assert "fallback" not in fonts["title"] and "fallback" not in fonts["body"]
    assert fonts["label"]["family"] == "Montserrat"


def test_prompt_has_typography_section(iig3d, cat, fixtures):
    spec = iig3d.load_spec(fixtures / "spec-pipeline.yaml")
    prompt = iig3d.assemble(cat, spec, iig3d.route(cat, "linear-progression", "3d-disc-timeline"), "16:9")
    text = prompt.text
    assert text.index("## Text Requirements") < text.index("## Typography") < text.index("## Layout Guidelines")
    section = text.split("## Typography", 1)[1].split("## ", 1)[0]
    assert "- **Title**: Montserrat (or Poppins or Gotham), bold, all caps, wide letter-spacing" in section
    assert "- **Body**: Montserrat (or Poppins), light, sentence case" in section
    assert "no other typeface appears" in section
    assert prompt.frontmatter["fonts"]["title"]["family"] == "Montserrat"


def test_font_line_formatting(iig3d):
    line = iig3d.font_line("title", {"family": "Inter", "weight": "bold", "case": "none", "tracking": "normal", "colour": "white"})
    assert line == "- **Title**: Inter, bold, colour: white"
    assert iig3d.typography_block({}) == ""
