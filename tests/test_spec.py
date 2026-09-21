"""R6: the YAML content spec loads with defaults and rejects bad shapes by name."""

from __future__ import annotations

import pytest


def test_fixture_loads(iig3d, fixtures):
    spec = iig3d.load_spec(fixtures / "spec-pipeline.yaml")
    assert spec.title == "OPENWIKI REFRESH PIPELINE"
    assert spec.subtitle.startswith("Five steps")
    assert spec.language == "en"
    assert spec.layout == "linear-progression" and spec.style == "3d-disc-timeline"
    assert spec.aspect == "landscape"
    assert [i.label for i in spec.items] == ["COMMIT", "TRIGGER", "ANALYSE", "GENERATE", "PUBLISH"]
    assert spec.items[0].detail == "Developer pushes to main"
    assert spec.stats == [] and spec.refs == [] and spec.notes == "" and spec.palette_css is None


def test_defaults(iig3d, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: T\nitems:\n  - label: A\n")
    spec = iig3d.load_spec(path)
    assert spec.language == "en" and spec.layout is None and spec.style is None and spec.aspect is None
    assert spec.items[0].detail == "" and spec.items[0].icon is None and spec.items[0].value is None


@pytest.mark.parametrize(
    "text,key",
    [
        ("items:\n  - label: A\n", "title"),
        ("title: T\n", "items"),
        ("title: T\nitems:\n  - detail: x\n", "label"),
        ("title: T\nitems:\n  - label: A\ncolour: red\n", "colour"),
        ("title: T\nitems: []\n", "items"),
        ("title: T\nitems:\n  - label: A\n    weight: 2\n", "weight"),
    ],
)
def test_bad_spec_names_key(iig3d, tmp_path, text, key):
    path = tmp_path / "s.yaml"
    path.write_text(text)
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.load_spec(path)
    assert key in str(err.value)


def test_palette_css_resolves_against_spec_dir(iig3d, tmp_path):
    (tmp_path / "styles").mkdir()
    css = tmp_path / "styles" / "brand.css"
    css.write_text(":root{--a:#123456}")
    path = tmp_path / "s.yaml"
    path.write_text("title: T\npalette_css: styles/brand.css\npalette_vars: [--a]\nitems:\n  - label: A\n")
    spec = iig3d.load_spec(path)
    assert spec.palette_css == css.resolve()
    assert spec.palette_vars == ["--a"]


def test_stats_and_refs(iig3d, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: T\nitems:\n  - label: A\nstats:\n  - {value: '73%', caption: uplift}\nrefs: [a.jpg]\nnotes: keep it airy\n")
    spec = iig3d.load_spec(path)
    assert spec.stats == [{"value": "73%", "caption": "uplift"}]
    assert spec.refs == [(tmp_path / "a.jpg").resolve()]
    assert spec.notes == "keep it airy"


def test_invalid_yaml_is_usage_error(iig3d, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: a: b\nitems: []\n")
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.load_spec(path)
    assert "not valid YAML" in str(err.value) and "s.yaml" in str(err.value)


def test_pin_key(iig3d, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: T\npin: 3d-capsule-hub/06\nitems:\n  - label: A\n")
    assert iig3d.load_spec(path).pin == "3d-capsule-hub/06"
    path.write_text("title: T\nitems:\n  - label: A\n")
    assert iig3d.load_spec(path).pin is None


def test_quality_key(iig3d, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: T\nquality: 4K\nitems:\n  - label: A\n")
    assert iig3d.load_spec(path).quality == "4K"
    path.write_text("title: T\nquality: 8K\nitems:\n  - label: A\n")
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.load_spec(path)
    assert "quality" in str(err.value) and "1K, 2K, 4K" in str(err.value)


def test_icon_style_key(iig3d, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: T\nicon_style: white line icons\nitems:\n  - label: A\n")
    assert iig3d.load_spec(path).icon_style == "white line icons"
