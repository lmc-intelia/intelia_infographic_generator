"""R3, R15: the YAML catalogue is complete, internally consistent and schema-valid."""

from __future__ import annotations

import pytest

MEMBERS = [
    "3d-slab-stack",
    "3d-arrow-ribbon",
    "3d-disc-timeline",
    "3d-paper-tile",
    "3d-gradient-pedestal",
    "3d-capsule-hub",
    "3d-isometric-light",
    "3d-isometric-dark",
    "3d-target-callout",
    "3d-hex-cluster",
    "3d-cylinder-column",
    "3d-glass-layer",
]
MEMBER_KEYS = {
    "name",
    "device",
    "backdrop",
    "items",
    "aspect_default",
    "layout",
    "style",
    "prompt_fragment",
    "best_for",
    "refs",
    "pairings",
    "alternates",
    "source",
}
FLAGS = {"clean", "watermark", "low-res"}


@pytest.fixture(scope="module")
def cat(iig3d, skill_root):
    return iig3d.load_catalogue(skill_root)


def test_twelve_members(cat):
    assert sorted(cat.members) == sorted(MEMBERS)


@pytest.mark.parametrize("name", MEMBERS)
def test_member_keys(cat, name):
    member = cat.member(name)
    assert set(member.raw) >= MEMBER_KEYS
    assert member.items["min"] <= member.items["max"]
    assert member.aspect_default in {"landscape", "portrait", "square"}


@pytest.mark.parametrize("name", MEMBERS)
def test_fragment_ends_with_negative_list(cat, name):
    fragment = cat.member(name).prompt_fragment.strip()
    assert fragment.endswith("Clean premium business-template 3D.")


def test_routing_rows(cat):
    assert len(cat.routing) == 21
    for layout, row in cat.routing.items():
        assert row["primary"] in cat.members, layout
        for alt in row["alternates"]:
            assert alt in cat.members, (layout, alt)


@pytest.mark.parametrize("name", MEMBERS)
def test_pairings_resolve(cat, name):
    member = cat.member(name)
    ref_ids = {r["id"] for r in member.refs}
    for layout, ids in member.pairings.items():
        assert layout in cat.routing or layout in cat.members, (name, layout)
        assert ids, (name, layout)
        for rid in ids:
            assert rid in ref_ids, (name, layout, rid)


@pytest.mark.parametrize("name", MEMBERS)
def test_ref_flags(cat, name):
    for ref in cat.member(name).refs:
        assert ref["flags"], ref["file"]
        assert set(ref["flags"]) <= FLAGS, ref["file"]
        assert ref["file"].startswith(f"ref-{ref['id']}-") and ref["file"].endswith(".jpg")


@pytest.mark.parametrize("name", MEMBERS)
def test_alternates_exist(cat, name):
    for alt in cat.member(name).alternates:
        assert alt in cat.members and alt != name


def test_family_constants(cat):
    assert cat.family["negative_list"].endswith("Clean premium business-template 3D.")
    assert set(cat.family["aspect_map"]) == {"landscape", "portrait", "square"}
    assert cat.family["supported_ratios"] == ["1:1", "3:2", "2:3", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"]
    assert cat.family["text_budget"] == {"landscape": 120, "portrait": 160}
    assert len(cat.family["palette"]["items"]) == 8


def test_schema_rejects_missing_fragment(iig3d, cat):
    broken = dict(cat.member("3d-slab-stack").raw)
    del broken["prompt_fragment"]
    problems = iig3d.validate_member(broken, cat.schema)
    assert any("prompt_fragment" in p for p in problems)
    assert iig3d.validate_member(cat.member("3d-slab-stack").raw, cat.schema) == []


# --- R15, R21: shipped refs on disk, no vendored watermark, check() clean ---


@pytest.mark.parametrize("name", MEMBERS)
def test_ref_files_on_disk(cat, name):
    from PIL import Image

    for ref in cat.member(name).refs:
        path = cat.ref_path(name, ref)
        assert path.is_file(), path
        with Image.open(path) as image:
            assert image.format == "JPEG", path
            assert max(image.size) <= 1600, (path, image.size)


@pytest.mark.parametrize("name", MEMBERS)
def test_no_vendored_watermark(cat, name):
    for ref in cat.member(name).refs:
        if "watermark" in ref["flags"]:
            assert ref.get("source", {}).get("user_added") is True, ref["file"]


def test_check_clean(iig3d, cat):
    assert iig3d.check(cat) == []


def test_check_reports_seeded_violations(iig3d, tmp_catalogue):
    iig3d.render_docs(tmp_catalogue)
    assert iig3d.check(tmp_catalogue) == []
    hex_yaml = tmp_catalogue.root / "catalogue" / "members" / "3d-hex-cluster.yaml"
    hex_yaml.write_text(hex_yaml.read_text().replace("flags:\n    - clean", "flags:\n    - watermark", 1).replace("flags: [clean]", "flags: [watermark]", 1))
    seeded = iig3d.load_catalogue(tmp_catalogue.root)
    assert "watermark" in seeded.member("3d-hex-cluster").refs[0]["flags"]
    iig3d.render_docs(seeded)
    violations = iig3d.check(seeded)
    assert any("watermark" in v for v in violations)
    # --allow-watermark relaxes the rule for user-added refs only; a vendored watermark always fails
    assert any("watermark" in v for v in iig3d.check(seeded, allow_watermark=True))
    seeded.member("3d-hex-cluster").refs[0]["source"] = {"origin": "x", "added": "2026-09-17", "user_added": True}
    iig3d.render_docs(seeded)
    assert any("watermark" in v for v in iig3d.check(seeded))
    assert iig3d.check(seeded, allow_watermark=True) == []
    (tmp_catalogue.root / "refs" / "3d-hex-cluster" / "ref-01-honeycomb-hub.jpg").unlink()
    member_yaml = tmp_catalogue.root / "catalogue" / "members" / "3d-slab-stack.yaml"
    member_yaml.write_text(member_yaml.read_text().replace("Clean premium business-template 3D.", "Done.", 1))
    cat = iig3d.load_catalogue(tmp_catalogue.root)
    violations = iig3d.check(cat, allow_watermark=True)
    assert any("ref-01-honeycomb-hub.jpg" in v and "missing" in v for v in violations)
    assert any("3d-slab-stack" in v and "negative list" in v for v in violations)
    assert any(v.startswith("docs stale") for v in violations)


def test_check_dependency_parity(iig3d, skill_root):
    assert iig3d.dependency_parity(skill_root) == []
