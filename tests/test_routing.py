"""R4: industrial-3d routes by layout; a named member skips the table; unknown names fail."""

from __future__ import annotations

import pytest

from tests.test_catalogue import MEMBERS

LAYOUTS = [
    "linear-progression",
    "winding-roadmap",
    "circular-flow",
    "hub-spoke",
    "tree-branching",
    "hierarchical-layers",
    "funnel",
    "bridge",
    "dashboard",
    "bento-grid",
    "periodic-table",
    "comparison-matrix",
    "binary-comparison",
    "isometric-map",
    "structural-breakdown",
    "dense-modules",
    "iceberg",
    "jigsaw",
    "venn-diagram",
    "comic-strip",
    "story-mountain",
]


@pytest.fixture(scope="module")
def cat(iig3d, skill_root):
    return iig3d.load_catalogue(skill_root)


@pytest.mark.parametrize("layout", LAYOUTS)
@pytest.mark.parametrize("style", [None, "industrial-3d"])
def test_general_layout_routes_to_primary(iig3d, cat, layout, style):
    route = iig3d.route(cat, layout, style)
    row = cat.routing[layout]
    assert route.member == row["primary"]
    assert route.alternates == row["alternates"]
    assert route.layout == layout
    assert "routing table" in route.reason


@pytest.mark.parametrize("member", MEMBERS)
def test_device_layout_returns_member(iig3d, cat, member):
    route = iig3d.route(cat, member, None)
    assert route.member == member
    assert route.alternates == cat.member(member).alternates
    assert route.layout == member


@pytest.mark.parametrize("member", MEMBERS)
def test_explicit_member_style_skips_table(iig3d, cat, member):
    route = iig3d.route(cat, "dashboard", member)
    assert route.member == member
    assert route.layout == "dashboard"
    assert "explicit" in route.reason


def test_layout_defaults_to_member_device(iig3d, cat):
    route = iig3d.route(cat, None, "3d-glass-layer")
    assert route.member == "3d-glass-layer"
    assert route.layout == "3d-glass-layer"


def test_no_layout_no_style_defaults_to_bento_grid(iig3d, cat):
    route = iig3d.route(cat, None, None)
    assert route.layout == "bento-grid"
    assert route.member == "3d-paper-tile"


def test_unknown_layout_lists_valid_names(iig3d, cat):
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.route(cat, "spiral", None)
    assert "spiral" in str(err.value) and "linear-progression" in str(err.value)


def test_unknown_style_lists_valid_names(iig3d, cat):
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.route(cat, "dashboard", "claymation")
    assert "claymation" in str(err.value) and "3d-paper-tile" in str(err.value)


def test_pinned_member_sets_style_and_default_layout(iig3d, cat):
    route = iig3d.route(cat, None, None, pinned_member="3d-capsule-hub")
    assert route.member == "3d-capsule-hub" and route.layout == "3d-capsule-hub" and route.style == "3d-capsule-hub"
    route = iig3d.route(cat, "hub-spoke", "industrial-3d", pinned_member="3d-paper-tile")
    assert route.member == "3d-paper-tile" and route.layout == "hub-spoke"


def test_pinned_member_conflicts_with_explicit_style(iig3d, cat):
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.route(cat, None, "3d-slab-stack", pinned_member="3d-capsule-hub")
    assert "conflicts" in str(err.value)
