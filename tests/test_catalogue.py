"""R3, R15: the YAML catalogue is complete, internally consistent and schema-valid."""

from __future__ import annotations

import pytest

MEMBERS = [
    "3d-slab-stack", "3d-arrow-ribbon", "3d-disc-timeline", "3d-paper-tile",
    "3d-gradient-pedestal", "3d-capsule-hub", "3d-isometric-light", "3d-isometric-dark",
    "3d-target-callout", "3d-hex-cluster", "3d-cylinder-column", "3d-glass-layer",
]
MEMBER_KEYS = {
    "name", "device", "backdrop", "items", "aspect_default", "layout", "style",
    "prompt_fragment", "best_for", "refs", "pairings", "alternates", "source",
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
    assert MEMBER_KEYS <= set(member.raw)
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
