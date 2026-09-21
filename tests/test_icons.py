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
    assert prompt.frontmatter["icons"] == [{"item": 1, "icon": "lucide:compass", "via": "spec"}, {"item": 2, "icon": "lucide:hammer", "via": "spec"}, {"item": 3, "icon": "lucide:rocket", "via": "spec"}]


def test_no_pack_means_no_sheet(iig3d, tmp_catalogue, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: T\nitems:\n  - {label: A, icon: rocket}\n")
    spec = iig3d.load_spec(path)
    assert iig3d.build_icon_sheet(tmp_catalogue, spec, tmp_path / "sheet.png", fetch=False) is None
    prompt = iig3d.assemble(tmp_catalogue, spec, iig3d.route(tmp_catalogue, "dashboard", None), "16:9")
    assert "Icon Set" not in prompt.text and "[icon: rocket]" in prompt.text and "icons" not in prompt.frontmatter


@pytest.fixture
def offline_cat(iig3d, tmp_catalogue):
    import shutil

    from tests.conftest import SKILL

    shutil.copytree(SKILL / "icons", tmp_catalogue.root / "icons", dirs_exist_ok=True)
    return tmp_catalogue


def test_suggest_from_synonyms_offline(iig3d, offline_cat):
    assert iig3d.suggest_icon(offline_cat, "lucide", "LAUNCH", "Release to customers", fetch=False) == ("rocket", "synonym:launch")
    assert iig3d.suggest_icon(offline_cat, "lucide", "PLAN", fetch=False) == ("compass", "synonym:plan")
    # label has no synonym, detail does
    assert iig3d.suggest_icon(offline_cat, "lucide", "STEP TWO", "measure outcomes", fetch=False) == ("chart-line", "synonym:measure")
    # synonym exists but glyph not vendored and fetching off: skipped, nothing else fits
    assert "wallet.svg" not in {p.name for p in (offline_cat.root / "icons" / "lucide").iterdir()}
    assert iig3d.suggest_icon(offline_cat, "lucide", "BUDGET", fetch=False) is None
    assert iig3d.suggest_icon(offline_cat, "lucide", "AUDIT", fetch=False) is None


def test_suggest_falls_back_to_search(iig3d, offline_cat, monkeypatch):
    calls = []

    def fake_search(pack, query, fetch=True, limit=8):
        calls.append(query)
        return ["umbrella"] if query == "umbrella" else []

    monkeypatch.setattr(iig3d, "search_icons", fake_search)
    assert iig3d.suggest_icon(offline_cat, "lucide", "UMBRELLA", "", fetch=True) == ("umbrella", "search:umbrella")
    assert calls[0] == "umbrella"


def test_resolve_icons_mixes_spec_and_suggestions(iig3d, offline_cat, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text(
        "title: T\nicon_pack: lucide\nitems:\n"
        "  - {label: PLAN, icon: compass}\n"  # named, exists
        "  - {label: LAUNCH, detail: Release}\n"  # suggested from label
        "  - {label: TALK, icon: a speech bubble}\n"  # free-text hint, untouched
        "  - {label: ZZZ}\n"  # nothing fits offline
    )
    spec = iig3d.load_spec(path)
    icons = iig3d.resolve_icons(offline_cat, spec, fetch=False)
    assert [(i["index"], i["name"], i["via"]) for i in icons] == [(1, "compass", "spec"), (2, "rocket", "synonym:launch")]


def test_resolve_named_missing_icon_falls_back_then_fails(iig3d, offline_cat, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: T\nicon_pack: lucide\nitems:\n  - {label: LAUNCH, icon: blast-off}\n  - {label: ZZZ, icon: no-such-thing}\n")
    spec = iig3d.load_spec(path)
    spec.items = spec.items[:1]
    icons = iig3d.resolve_icons(offline_cat, spec, fetch=False)
    assert icons[0]["name"] == "rocket" and icons[0]["via"].startswith("fallback for blast-off via synonym:launch")
    spec = iig3d.load_spec(path)
    spec.items = spec.items[1:]
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.resolve_icons(offline_cat, spec, fetch=False)
    assert "no-such-thing" in str(err.value) and "ZZZ" in str(err.value)


def test_no_pack_no_prefix_means_no_resolution(iig3d, offline_cat, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: T\nitems:\n  - {label: LAUNCH}\n  - {label: PLAN, icon: compass}\n")
    assert iig3d.resolve_icons(offline_cat, iig3d.load_spec(path), fetch=False) == []
