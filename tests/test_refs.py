"""R5: pick 2 to 3 refs per render honouring pairing order and the flag rules; cap 6."""

from __future__ import annotations

import pytest


def names(paths):
    return [p.name for p in paths]


@pytest.fixture
def flagged(tmp_catalogue):
    """The shipped catalogue carries no watermark flags any more; restore the source flags in memory
    so the selection rules are pinned (review finding on R5)."""
    disc = {r["id"]: r for r in tmp_catalogue.member("3d-disc-timeline").refs}
    disc["01"]["flags"] = ["watermark"]
    disc["02"]["flags"] = ["watermark", "low-res"]
    disc["04"]["flags"] = ["watermark"]
    hub = {r["id"]: r for r in tmp_catalogue.member("3d-capsule-hub").refs}
    hub["01"]["flags"] = ["watermark"]
    hub["02"]["flags"] = ["watermark"]
    hub["03"]["flags"] = ["low-res"]
    return tmp_catalogue


def test_never_two_watermarks_even_when_pairing_names_two(iig3d, flagged):
    # winding-roadmap pairing is ["03" (clean), "04" (watermark)]; bridge is ["01" (wm), "03"]
    for layout in ("winding-roadmap", "bridge", "circular-flow"):
        picked = names(iig3d.select_refs(flagged, "3d-disc-timeline", layout))
        flags = {r["file"]: set(r["flags"]) for r in flagged.member("3d-disc-timeline").refs}
        assert sum("watermark" in flags[f] for f in picked) <= 1, (layout, picked)
        assert len(picked) >= 2
    # capsule-hub hub-spoke pairing ["01" (wm), "05" (clean), "02" (wm)] -> second watermark dropped
    picked = names(iig3d.select_refs(flagged, "3d-capsule-hub", "hub-spoke"))
    assert picked == ["ref-05-rimmed-capsule-wheel.jpg", "ref-01-capsule-hub.jpg"]
    assert iig3d.ref_rule_violations(iig3d.pick_style_refs(flagged, flagged.member("3d-capsule-hub"), "hub-spoke")) == []


def test_low_res_alone_gets_company(iig3d, flagged):
    hub = flagged.member("3d-capsule-hub")
    hub.raw["pairings"]["circular-flow"] = ["03"]
    picked = iig3d.pick_style_refs(flagged, hub, "circular-flow")
    assert picked[0]["id"] == "03" or any(r["id"] == "03" for r in picked)
    assert any("low-res" not in r["flags"] for r in picked)
    assert iig3d.ref_rule_violations(picked) == []


def test_pairing_order_and_existence(iig3d, tmp_catalogue):
    picked = iig3d.select_refs(tmp_catalogue, "3d-paper-tile", "hub-spoke")
    assert names(picked) == ["ref-02-semicircle-tabs.jpg", "ref-03-hexagon-tree.jpg"]
    assert all(p.is_file() for p in picked)


def test_clean_first_and_no_two_watermarks(iig3d, flagged):
    tmp_catalogue = flagged
    # pairing 03 (clean), 01 (watermark), then fallback pool 02 (watermark, low-res), 04 (watermark)
    picked = names(iig3d.select_refs(tmp_catalogue, "3d-disc-timeline", "linear-progression"))
    assert picked[0] == "ref-03-disc-chain-track.jpg"
    flags = {r["file"]: set(r["flags"]) for r in tmp_catalogue.member("3d-disc-timeline").refs}
    assert sum("watermark" in flags[f] for f in picked) <= 1
    assert 2 <= len(picked) <= 3


def test_low_res_never_alone(iig3d, flagged):
    tmp_catalogue = flagged
    member = tmp_catalogue.member("3d-capsule-hub")
    # circular-flow pairing is ["03" (low-res), "01" (watermark)]
    picked = names(iig3d.select_refs(tmp_catalogue, "3d-capsule-hub", "circular-flow"))
    flags = {r["file"]: set(r["flags"]) for r in member.refs}
    assert len(picked) >= 2
    assert any("low-res" not in flags[f] for f in picked)
    assert "ref-03-segment-ring.jpg" in picked


def test_single_ref_member_returns_one(iig3d, tmp_catalogue):
    picked = names(iig3d.select_refs(tmp_catalogue, "3d-hex-cluster", "hub-spoke"))
    assert picked == ["ref-01-honeycomb-hub.jpg"]


def test_fallback_when_layout_has_no_pairing(iig3d, tmp_catalogue):
    picked = names(iig3d.select_refs(tmp_catalogue, "3d-slab-stack", "dashboard"))
    assert picked[:2] == ["ref-01-stacked-slabs.jpg", "ref-03-folded-ribbon-tiers.jpg"]


def test_device_layout_uses_first_pairing(iig3d, tmp_catalogue):
    picked = names(iig3d.select_refs(tmp_catalogue, "3d-slab-stack", "3d-slab-stack"))
    assert picked == ["ref-01-stacked-slabs.jpg", "ref-03-folded-ribbon-tiers.jpg", "ref-04-rounded-slab-column-eight.jpg"]


def test_user_refs_appended_and_capped_at_six(iig3d, tmp_catalogue, tmp_path):
    from PIL import Image

    user = []
    for i in range(6):
        p = tmp_path / f"user{i}.jpg"
        Image.new("RGB", (8, 8)).save(p, "JPEG")
        user.append(p)
    base = iig3d.select_refs(tmp_catalogue, "3d-capsule-hub", "hub-spoke")
    picked = iig3d.select_refs(tmp_catalogue, "3d-capsule-hub", "hub-spoke", user_refs=user)
    assert len(picked) == 6
    assert picked[: len(base)] == base
    assert picked[len(base) :] == user[: 6 - len(base)]
    assert names(base) == ["ref-01-capsule-hub.jpg", "ref-05-rimmed-capsule-wheel.jpg", "ref-02-central-disc-ribbon.jpg"]


def test_missing_ref_file_raises(iig3d, tmp_catalogue):
    (tmp_catalogue.root / "refs" / "3d-hex-cluster" / "ref-01-honeycomb-hub.jpg").unlink()
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.select_refs(tmp_catalogue, "3d-hex-cluster", "hub-spoke")
    assert "ref-01-honeycomb-hub.jpg" in str(err.value)


def test_missing_user_ref_raises(iig3d, tmp_catalogue, tmp_path):
    with pytest.raises(iig3d.UsageError):
        iig3d.select_refs(tmp_catalogue, "3d-hex-cluster", "hub-spoke", user_refs=[tmp_path / "nope.jpg"])


def test_style_refs_disabled(iig3d, tmp_catalogue):
    assert iig3d.select_refs(tmp_catalogue, "3d-hex-cluster", "hub-spoke", style_refs=False) == []


# --- pinned catalogue refs: reproduce one JPEG's composition with the user's content ---


def test_resolve_ref_forms(iig3d, tmp_catalogue):
    cat = tmp_catalogue
    for token in ("3d-capsule-hub/06", "3d-capsule-hub/ref-06-capsule-hierarchy.jpg", "3d-capsule-hub/ref-06-capsule-hierarchy", "refs/3d-capsule-hub/ref-06-capsule-hierarchy.jpg"):
        member, ref = cat.resolve_ref(token)
        assert member.name == "3d-capsule-hub" and ref["id"] == "06", token
    member, ref = cat.resolve_ref("06", style="3d-capsule-hub")
    assert member.name == "3d-capsule-hub" and ref["id"] == "06"
    assert cat.pin_token(member.name, ref) == "3d-capsule-hub/06"


@pytest.mark.parametrize(
    "token,style,needle",
    [
        ("06", None, "needs a member"),
        ("06", "industrial-3d", "needs a member"),
        ("3d-capsule-hub/99", None, "valid: 01"),
        ("3d-nope/01", None, "unknown member"),
        ("a/b/c", None, "not <member>/<ref>"),
        ("../../etc/passwd", None, "not <member>/<ref>"),
    ],
)
def test_resolve_ref_rejects(iig3d, tmp_catalogue, token, style, needle):
    with pytest.raises(iig3d.UsageError) as err:
        tmp_catalogue.resolve_ref(token, style)
    assert needle in str(err.value)


def test_pinned_ref_first_with_company(iig3d, tmp_catalogue):
    _, pinned = tmp_catalogue.resolve_ref("3d-capsule-hub/06")
    picked = names(iig3d.select_refs(tmp_catalogue, "3d-capsule-hub", "hub-spoke", pinned=pinned))
    assert picked[0] == "ref-06-capsule-hierarchy.jpg"
    assert 2 <= len(picked) <= 3 and len(set(picked)) == len(picked)
    assert all(p.is_file() for p in iig3d.select_refs(tmp_catalogue, "3d-capsule-hub", "hub-spoke", pinned=pinned))


def test_pinned_ref_dedupes_against_pairing(iig3d, tmp_catalogue):
    # hub-spoke pairing starts with 01; pinning 01 must not pass it twice
    _, pinned = tmp_catalogue.resolve_ref("3d-capsule-hub/01")
    picked = names(iig3d.select_refs(tmp_catalogue, "3d-capsule-hub", "hub-spoke", pinned=pinned))
    assert picked[0] == "ref-01-capsule-hub.jpg" and picked.count("ref-01-capsule-hub.jpg") == 1
    assert len(picked) == 3


def test_pinned_watermark_blocks_second_watermark(iig3d, flagged):
    _, pinned = flagged.resolve_ref("3d-capsule-hub/01")  # watermark in the flagged fixture
    picked = iig3d.pick_pinned_refs(flagged, flagged.member("3d-capsule-hub"), "hub-spoke", pinned)
    assert picked[0]["id"] == "01"
    assert sum("watermark" in r["flags"] for r in picked) == 1


def test_pinned_alone_when_style_refs_off(iig3d, tmp_catalogue):
    _, pinned = tmp_catalogue.resolve_ref("3d-capsule-hub/06")
    assert names(iig3d.select_refs(tmp_catalogue, "3d-capsule-hub", "hub-spoke", pinned=pinned, style_refs=False)) == ["ref-06-capsule-hierarchy.jpg"]


def test_pinned_then_user_refs_capped(iig3d, tmp_catalogue, tmp_path):
    from PIL import Image

    user = []
    for i in range(6):
        p = tmp_path / f"user{i}.jpg"
        Image.new("RGB", (8, 8)).save(p, "JPEG")
        user.append(p)
    _, pinned = tmp_catalogue.resolve_ref("3d-capsule-hub/06")
    picked = iig3d.select_refs(tmp_catalogue, "3d-capsule-hub", "hub-spoke", user_refs=user, pinned=pinned)
    assert len(picked) == 6 and picked[0].name == "ref-06-capsule-hierarchy.jpg"
