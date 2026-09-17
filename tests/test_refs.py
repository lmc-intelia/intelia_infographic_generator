"""R5: pick 2 to 3 refs per render honouring pairing order and the flag rules; cap 6."""

from __future__ import annotations

import pytest


def names(paths):
    return [p.name for p in paths]


def test_pairing_order_and_existence(iig3d, tmp_catalogue):
    picked = iig3d.select_refs(tmp_catalogue, "3d-paper-tile", "hub-spoke")
    assert names(picked) == ["ref-02-semicircle-tabs.jpg", "ref-03-hexagon-tree.jpg"]
    assert all(p.is_file() for p in picked)


def test_clean_first_and_no_two_watermarks(iig3d, tmp_catalogue):
    # pairing 03 (clean), 01 (watermark), then fallback pool 02 (watermark, low-res), 04 (watermark)
    picked = names(iig3d.select_refs(tmp_catalogue, "3d-disc-timeline", "linear-progression"))
    assert picked[0] == "ref-03-disc-chain-track.jpg"
    flags = {r["file"]: set(r["flags"]) for r in tmp_catalogue.member("3d-disc-timeline").refs}
    assert sum("watermark" in flags[f] for f in picked) <= 1
    assert 2 <= len(picked) <= 3


def test_low_res_never_alone(iig3d, tmp_catalogue):
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
    assert picked == ["ref-01-stacked-slabs.jpg", "ref-03-folded-ribbon-tiers.jpg"]


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
    assert names(base) == ["ref-05-rimmed-capsule-wheel.jpg", "ref-01-capsule-hub.jpg"]


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
