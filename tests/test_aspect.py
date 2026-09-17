"""R7: named presets, exact ratios, snapping to the Gemini set, member default."""

from __future__ import annotations

import pytest

SUPPORTED = ["1:1", "3:2", "2:3", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"]


@pytest.fixture(scope="module")
def cat(iig3d, skill_root):
    return iig3d.load_catalogue(skill_root)


@pytest.mark.parametrize("preset,ratio", [("landscape", "16:9"), ("portrait", "9:16"), ("square", "1:1")])
def test_presets(iig3d, cat, preset, ratio):
    assert iig3d.snap_aspect(cat, preset, "landscape") == (ratio, None)


@pytest.mark.parametrize("ratio", SUPPORTED)
def test_supported_round_trip(iig3d, cat, ratio):
    assert iig3d.snap_aspect(cat, ratio, "landscape") == (ratio, None)


@pytest.mark.parametrize("given,expected", [("2.35:1", "21:9"), ("4:1", "21:9"), ("1:2", "9:16"), ("1.5:1", "3:2"), ("1:1.5", "2:3")])
def test_snaps_to_nearest(iig3d, cat, given, expected):
    assert iig3d.snap_aspect(cat, given, "landscape") == (expected, given)


def test_none_uses_member_default(iig3d, cat):
    assert iig3d.snap_aspect(cat, None, "portrait") == ("9:16", None)
    assert iig3d.snap_aspect(cat, None, "landscape") == ("16:9", None)


@pytest.mark.parametrize("bad", ["wide", "16x9", "0:9", "a:b"])
def test_malformed_rejected(iig3d, cat, bad):
    with pytest.raises(iig3d.UsageError):
        iig3d.snap_aspect(cat, bad, "landscape")


@pytest.mark.parametrize("ratio,orientation", [("16:9", "landscape"), ("1:1", "landscape"), ("21:9", "landscape"), ("9:16", "portrait"), ("3:4", "portrait")])
def test_orientation(iig3d, cat, ratio, orientation):
    assert iig3d.orientation(cat, ratio) == orientation
