"""Icon sheet: pack:name icons rasterised onto one labelled reference image the model copies from."""

from __future__ import annotations

import pytest
from PIL import Image


@pytest.fixture
def icon_spec(iig3d, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text(
        "title: T\nicon_pack: lucide\nlayout: 3d-disc-timeline\nitems:\n"
        "  - {label: PLAN, icon: compass}\n  - {label: BUILD, icon: hammer}\n  - {label: SHIP, icon: lucide:rocket}\n  - {label: FREE, icon: a spinning top}\n  - {label: NONE}\n"
    )
    return iig3d.load_spec(path)


def test_parse_icon_forms(iig3d):
    assert iig3d.parse_icon("rocket", "lucide") == ("lucide", "rocket")
    assert iig3d.parse_icon("tabler:rocket", "lucide") == ("tabler", "rocket")
    assert iig3d.parse_icon("rocket", None) is None
    assert iig3d.parse_icon(None, "lucide") is None
    with pytest.raises(iig3d.UsageError):
        iig3d.parse_icon("Lucide:Rocket Ship", None)
    with pytest.raises(iig3d.UsageError):
        iig3d.parse_icon("../etc:passwd", None)
    assert iig3d.parse_icon("a spinning top", "lucide") is None


def test_spec_icons_resolve_only_pack_icons(iig3d, icon_spec):
    icons = iig3d.spec_icons(icon_spec)
    assert [(i["index"], i["pack"], i["name"]) for i in icons] == [(1, "lucide", "compass"), (2, "lucide", "hammer"), (3, "lucide", "rocket")]


def test_vendored_icon_renders_offline(iig3d, skill_root):
    cat = iig3d.load_catalogue(skill_root)
    svg = iig3d.icon_svg(cat, "lucide", "rocket", fetch=False)
    assert svg.name == "rocket.svg"
    glyph = iig3d.render_icon(svg, 64)
    assert glyph.size == (64, 64) and glyph.getbbox() is not None


def test_missing_icon_without_fetch_names_it(iig3d, skill_root):
    cat = iig3d.load_catalogue(skill_root)
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.icon_svg(cat, "lucide", "no-such-glyph-xyz", fetch=False)
    assert "lucide:no-such-glyph-xyz" in str(err.value) and "fetching is off" in str(err.value)


def test_sheet_layout_and_prompt(iig3d, tmp_catalogue, icon_spec, tmp_path):
    import shutil

    from tests.conftest import SKILL

    shutil.copytree(SKILL / "icons", tmp_catalogue.root / "icons", dirs_exist_ok=True)
    sheet, icons = iig3d.build_icon_sheet(tmp_catalogue, icon_spec, tmp_path / "out" / "icon-sheet.png", fetch=False)
    image = Image.open(sheet)
    assert image.size == (3 * 320, 400) and len(icons) == 3
    route_ = iig3d.route(tmp_catalogue, "3d-disc-timeline", None)
    refs = iig3d.select_refs(tmp_catalogue, "3d-disc-timeline", route_.layout, icon_sheet=sheet)
    assert refs[-1] == sheet and len(refs) <= 6
    prompt = iig3d.assemble(tmp_catalogue, icon_spec, route_, "16:9", refs=refs, icon_sheet=sheet, icons=icons)
    body = prompt.text
    position = refs.index(sheet) + 1
    assert f"Reference image {position} is an icon sheet" in body
    assert "glyph 03 on item 03 (lucide:rocket)" in body
    assert '3. "SHIP" [icon: sheet glyph 03, lucide:rocket]' in body and '4. "FREE" [icon: a spinning top]' in body
    assert body.index("## Icon Set") < body.index("## Layout Guidelines")
    assert prompt.frontmatter["references"][position - 1] == {"ref_id": f"{position:02d}", "filename": "icon-sheet.png", "usage": "icons"}
    assert prompt.frontmatter["icons"] == [{"item": 1, "icon": "lucide:compass"}, {"item": 2, "icon": "lucide:hammer"}, {"item": 3, "icon": "lucide:rocket"}]


def test_no_pack_means_no_sheet(iig3d, tmp_catalogue, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: T\nitems:\n  - {label: A, icon: rocket}\n")
    spec = iig3d.load_spec(path)
    assert iig3d.build_icon_sheet(tmp_catalogue, spec, tmp_path / "sheet.png", fetch=False) is None
    prompt = iig3d.assemble(tmp_catalogue, spec, iig3d.route(tmp_catalogue, "dashboard", None), "16:9")
    assert "Icon Set" not in prompt.text and "[icon: rocket]" in prompt.text and "icons" not in prompt.frontmatter
