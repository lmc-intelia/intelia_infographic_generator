"""R13: add a user image as a first-class reference; new members need no Python change."""

from __future__ import annotations

import pytest
import yaml
from PIL import Image


def write_meta(tmp_path, **data):
    path = tmp_path / "meta.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False))
    return path


def test_add_to_existing_member(iig3d, tmp_catalogue, fixtures, tmp_path):
    iig3d.render_docs(tmp_catalogue)
    meta = write_meta(tmp_path, member="3d-hex-cluster", shows="A ring of twelve cells", flags=["clean"], pairings=["hub-spoke", "jigsaw"])
    result = iig3d.add_ref(tmp_catalogue, fixtures / "wide-3000px.jpg", meta)
    assert result["status"] == "ok" and result["member"] == "3d-hex-cluster" and result["ref_id"] == "02"
    ref = tmp_catalogue.root / "refs" / "3d-hex-cluster" / "ref-02-wide-3000px.jpg"
    assert result["ref_file"] == str(ref) and ref.is_file()
    image = Image.open(ref)
    assert image.format == "JPEG" and image.mode == "RGB" and max(image.size) == 1600
    cat = iig3d.load_catalogue(tmp_catalogue.root)
    member = cat.member("3d-hex-cluster")
    entry = member.refs[-1]
    assert entry["id"] == "02" and entry["file"] == "ref-02-wide-3000px.jpg" and entry["flags"] == ["clean"]
    assert entry["source"]["path"] == str(fixtures / "wide-3000px.jpg") and entry["source"]["user_added"] is True
    assert entry["source"]["added"]
    assert member.pairings["hub-spoke"] == ["01", "02"] and member.pairings["jigsaw"] == ["01", "02"]
    assert member.pairings["bento-grid"] == ["01"]
    assert result["check"] == [] and iig3d.stale_docs(cat) == []
    assert "ref-02-wide-3000px.jpg" in (tmp_catalogue.root / "docs" / "members" / "3d-hex-cluster.md").read_text()


def test_new_member(iig3d, tmp_catalogue, fixtures, tmp_path):
    block = dict(tmp_catalogue.member("3d-hex-cluster").raw)
    block.pop("refs")
    block.pop("pairings")
    block.pop("source")
    block.update(name="3d-orbit-ring", device="Concentric orbit rings", alternates=["3d-capsule-hub"], routing=["hub-spoke", "circular-flow"])
    meta = write_meta(tmp_path, new_member=block, shows="Orbit rings", flags=["clean"], pairings=["hub-spoke"], slug="orbit")
    result = iig3d.add_ref(tmp_catalogue, fixtures / "wide-3000px.jpg", meta)
    assert result["status"] == "ok" and result["member"] == "3d-orbit-ring" and result["ref_id"] == "01"
    assert (tmp_catalogue.root / "catalogue" / "members" / "3d-orbit-ring.yaml").exists()
    assert (tmp_catalogue.root / "refs" / "3d-orbit-ring" / "ref-01-orbit.jpg").is_file()
    cat = iig3d.load_catalogue(tmp_catalogue.root)
    member = cat.member("3d-orbit-ring")
    assert member.pairings == {"hub-spoke": ["01"]}
    assert member.raw["source"]["origin"].startswith("user")
    assert "routing" not in member.raw
    assert cat.routing["hub-spoke"]["alternates"][-1] == "3d-orbit-ring"
    assert cat.routing["circular-flow"]["alternates"][-1] == "3d-orbit-ring"
    assert cat.routing["dashboard"]["alternates"][-1] != "3d-orbit-ring"
    assert (tmp_catalogue.root / "docs" / "members" / "3d-orbit-ring.md").exists()


def test_replace_missing_file_entry(iig3d, tmp_catalogue, fixtures, tmp_path):
    target = tmp_catalogue.root / "refs" / "3d-disc-timeline" / "ref-01-rimmed-disc-timeline.jpg"
    target.unlink()
    meta = write_meta(tmp_path, member="3d-disc-timeline", shows="Clean regenerated disc timeline", flags=["clean"], pairings=[], file="ref-01-rimmed-disc-timeline.jpg")
    result = iig3d.add_ref(tmp_catalogue, fixtures / "wide-3000px.jpg", meta)
    assert result["ref_id"] == "01" and target.is_file()
    cat = iig3d.load_catalogue(tmp_catalogue.root)
    entry = cat.member("3d-disc-timeline").refs[0]
    assert entry["id"] == "01" and entry["flags"] == ["clean"] and entry["shows"] == "Clean regenerated disc timeline"
    assert entry["source"]["regenerated"] is True
    assert cat.member("3d-disc-timeline").pairings["linear-progression"] == ["03", "01"]


def test_existing_entry_with_file_on_disk_rejected(iig3d, tmp_catalogue, fixtures, tmp_path):
    meta = write_meta(tmp_path, member="3d-disc-timeline", shows="x", flags=["clean"], pairings=[], file="ref-03-disc-chain-track.jpg")
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.add_ref(tmp_catalogue, fixtures / "wide-3000px.jpg", meta)
    assert "ref-03-disc-chain-track.jpg" in str(err.value)


@pytest.mark.parametrize("missing", ["shows", "flags"])
def test_meta_missing_key_named(iig3d, tmp_catalogue, fixtures, tmp_path, missing):
    data = {"member": "3d-hex-cluster", "shows": "x", "flags": ["clean"], "pairings": []}
    del data[missing]
    meta = write_meta(tmp_path, **data)
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.add_ref(tmp_catalogue, fixtures / "wide-3000px.jpg", meta)
    assert missing in str(err.value)


def test_bad_flag_and_unknown_pairing_rejected(iig3d, tmp_catalogue, fixtures, tmp_path):
    meta = write_meta(tmp_path, member="3d-hex-cluster", shows="x", flags=["shiny"], pairings=[])
    with pytest.raises(iig3d.UsageError):
        iig3d.add_ref(tmp_catalogue, fixtures / "wide-3000px.jpg", meta)
    meta = write_meta(tmp_path, member="3d-hex-cluster", shows="x", flags=["clean"], pairings=["spiral"])
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.add_ref(tmp_catalogue, fixtures / "wide-3000px.jpg", meta)
    assert "spiral" in str(err.value)


def test_member_and_new_member_exclusive(iig3d, tmp_catalogue, fixtures, tmp_path):
    meta = write_meta(tmp_path, member="3d-hex-cluster", new_member={"name": "3d-x"}, shows="x", flags=["clean"], pairings=[])
    with pytest.raises(iig3d.UsageError):
        iig3d.add_ref(tmp_catalogue, fixtures / "wide-3000px.jpg", meta)


def test_ids_increment_past_highest(iig3d, tmp_catalogue, fixtures, tmp_path):
    meta = write_meta(tmp_path, member="3d-capsule-hub", shows="x", flags=["clean"], pairings=[])
    result = iig3d.add_ref(tmp_catalogue, fixtures / "wide-3000px.jpg", meta)
    assert result["ref_id"] == "06"


def test_normalise_image_small_stays_small(iig3d, tmp_path):
    src = tmp_path / "small.png"
    Image.new("RGBA", (300, 200), (1, 2, 3, 255)).save(src)
    out = iig3d.normalise_image(src, tmp_path / "out.jpg")
    image = Image.open(out)
    assert image.size == (300, 200) and image.mode == "RGB" and image.format == "JPEG"


@pytest.mark.parametrize("bad_name", ["3d-../../../pwned", "3d-Bad Name", "3d-", "3d-x/y"])
def test_new_member_name_must_be_slug(iig3d, tmp_catalogue, fixtures, tmp_path, bad_name):
    """Review finding: a member name is a path segment; only 3d-[a-z0-9-]+ is allowed."""
    block = dict(tmp_catalogue.member("3d-hex-cluster").raw)
    for key in ("refs", "pairings", "source"):
        block.pop(key)
    block["name"] = bad_name
    meta = write_meta(tmp_path, new_member=block, shows="x", flags=["clean"], pairings=[])
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.add_ref(tmp_catalogue, fixtures / "wide-3000px.jpg", meta)
    assert "name" in str(err.value)
    assert not list(tmp_catalogue.root.glob("**/pwned*"))


def test_user_added_watermark_is_reported(iig3d, tmp_catalogue, fixtures, tmp_path):
    """Review finding (R21): a watermarked user image is registered but check must say so."""
    iig3d.render_docs(tmp_catalogue)
    meta = write_meta(tmp_path, member="3d-hex-cluster", shows="stock preview", flags=["watermark"], pairings=[])
    result = iig3d.add_ref(tmp_catalogue, fixtures / "wide-3000px.jpg", meta)
    assert result["status"] == "violations"
    assert any("watermark" in v and "ref-02-wide-3000px.jpg" in v for v in result["check"])
    cat = iig3d.load_catalogue(tmp_catalogue.root)
    assert iig3d.check(cat, allow_watermark=True) == []
