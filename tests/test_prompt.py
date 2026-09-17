"""R8, R9, R18: prompt assembly, persisted prompt files, warnings, redaction."""

from __future__ import annotations

import re

import pytest


def section(text: str, heading: str) -> str:
    """Body of a `## heading` section up to the next `##` or `---` line."""
    match = re.search(rf"^## {re.escape(heading)}\n(.*?)(?=^## |^---$)", text, re.MULTILINE | re.DOTALL)
    assert match, heading
    return match.group(1).strip()


def labels_block(text: str) -> str:
    return text[text.index("Text labels (in") :].strip()


@pytest.fixture(scope="module")
def cat(iig3d, skill_root):
    return iig3d.load_catalogue(skill_root)


@pytest.fixture
def spec(iig3d, fixtures):
    return iig3d.load_spec(fixtures / "spec-pipeline.yaml")


def test_style_guidelines_match_disc_timeline_sample(iig3d, cat, spec, fixtures):
    sample = (fixtures / "sample-prompt-3d-disc-timeline.md").read_text()
    prompt = iig3d.assemble(cat, spec, iig3d.route(cat, "linear-progression", "3d-disc-timeline"), "16:9")
    assert section(prompt.text, "Style Guidelines") == section(sample, "Style Guidelines")
    assert labels_block(prompt.text) == labels_block(sample)


def test_umbrella_routes_and_records_member(iig3d, cat, spec, fixtures):
    sample = (fixtures / "sample-prompt-industrial-3d.md").read_text()
    prompt = iig3d.assemble(cat, spec, iig3d.route(cat, "linear-progression", "industrial-3d"), "16:9")
    assert prompt.frontmatter["style"] == "industrial-3d"
    assert prompt.frontmatter["style_member"] == "3d-disc-timeline"
    assert labels_block(prompt.text) == labels_block(sample)
    assert cat.member("3d-disc-timeline").prompt_fragment in prompt.text


def test_header_and_layout_block(iig3d, cat, spec):
    prompt = iig3d.assemble(cat, spec, iig3d.route(cat, "linear-progression", "3d-disc-timeline"), "16:9")
    spec_section = section(prompt.text, "Image Specifications")
    assert "- **Layout**: linear-progression" in spec_section
    assert "- **Style**: 3d-disc-timeline" in spec_section
    assert "- **Aspect Ratio**: 16:9" in spec_section
    assert "- **Language**: en" in spec_section
    layout = prompt.text[prompt.text.index("## Layout Guidelines") + len("## Layout Guidelines") : prompt.text.index("## Style Guidelines")].strip()
    assert layout.startswith("# 3d-disc-timeline")
    assert "## Structure" in layout and "## Variants" in layout and "## Text Placement" in layout
    assert "Track passing behind a row of discs" in layout


def test_frontmatter_fields(iig3d, cat, spec, tmp_catalogue):
    refs = iig3d.select_refs(tmp_catalogue, "3d-disc-timeline", "linear-progression")
    prompt = iig3d.assemble(tmp_catalogue, spec, iig3d.route(tmp_catalogue, "linear-progression", "3d-disc-timeline"), "16:9", refs=refs)
    fm = prompt.frontmatter
    assert set(fm) >= {"layout", "style", "style_member", "aspect", "language", "references"}
    assert fm["aspect"] == "16:9" and fm["language"] == "en"
    assert fm["references"][0] == {"ref_id": "01", "filename": refs[0].name, "usage": "direct"}
    assert "palette" not in fm


def test_negative_list_appended_when_fragment_lacks_it(iig3d, cat, spec, tmp_catalogue):
    member = tmp_catalogue.member("3d-slab-stack")
    member.raw["prompt_fragment"] = "Render as slabs."
    prompt = iig3d.assemble(tmp_catalogue, spec, iig3d.route(tmp_catalogue, "hierarchical-layers", "3d-slab-stack"), "16:9")
    style = section(prompt.text, "Style Guidelines")
    assert style.startswith("Render as slabs.")
    assert style.endswith(tmp_catalogue.family["negative_list"])


def test_palette_override(iig3d, cat, spec, fixtures):
    colours = iig3d.extract_palette(fixtures / "brand.css", vars=["--brand-primary", "--brand-secondary", "--brand-accent"])
    prompt = iig3d.assemble(cat, spec, iig3d.route(cat, "linear-progression", "3d-disc-timeline"), "16:9", palette=colours, palette_source=fixtures / "brand.css")
    style = section(prompt.text, "Style Guidelines")
    assert style.endswith(iig3d.palette_paragraph(colours))
    assert cat.member("3d-disc-timeline").prompt_fragment in style
    assert prompt.frontmatter["palette"] == {"source": str(fixtures / "brand.css"), "colours": [c.as_dict() for c in colours]}


def test_content_block(iig3d, cat, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: T\nsubtitle: S\nnotes: keep it airy\nitems:\n  - {label: A, detail: d1, value: '73%'}\n  - {label: B}\nstats:\n  - {value: '12x', caption: faster}\n")
    spec = iig3d.load_spec(path)
    prompt = iig3d.assemble(cat, spec, iig3d.route(cat, "dashboard", None), "16:9")
    content = prompt.text[prompt.text.index("Generate the infographic based on the content below:") :]
    assert 'Title: "T"' in content and 'Subtitle: "S"' in content
    assert '1. "A" - d1 (73%)' in content and '2. "B"' in content
    assert 'Stats:\n- "12x" - faster' in content
    assert "Design notes: keep it airy" in content
    labels = labels_block(prompt.text).splitlines()
    assert labels[1:] == ['"T"', '"S"', '"01 A"', '"73%"', '"02 B"', '"12x"']


def test_write_prompt_numbers_never_overwrite(iig3d, cat, spec, tmp_path):
    prompt = iig3d.assemble(cat, spec, iig3d.route(cat, "linear-progression", "3d-disc-timeline"), "16:9")
    first = iig3d.write_prompt(tmp_path, prompt, "openwiki-refresh-pipeline")
    second = iig3d.write_prompt(tmp_path, prompt, "openwiki-refresh-pipeline")
    assert first.name == "01-infographic-openwiki-refresh-pipeline.md"
    assert second.name == "02-infographic-openwiki-refresh-pipeline.md"
    text = first.read_text()
    assert text.startswith("---\n") and "style_member: 3d-disc-timeline" in text.split("---")[1]
    assert text.rstrip().endswith('"05 PUBLISH"')


def test_slug(iig3d):
    assert iig3d.slugify("OPENWIKI REFRESH PIPELINE") == "openwiki-refresh-pipeline"
    assert iig3d.slugify("  A/B: test!! ") == "a-b-test"


def test_word_budget_warning(iig3d, cat, tmp_path):
    items = "\n".join(f"  - {{label: 'Item number {i} label words', detail: 'w'}}" for i in range(30))
    path = tmp_path / "s.yaml"
    path.write_text(f"title: T\nitems:\n{items}\n")
    spec = iig3d.load_spec(path)
    landscape = iig3d.assemble(cat, spec, iig3d.route(cat, "3d-paper-tile", None), "16:9")
    assert any("120" in w and "words" in w for w in landscape.warnings)
    portrait = iig3d.assemble(cat, spec, iig3d.route(cat, "3d-paper-tile", None), "9:16")
    assert any("160" in w for w in portrait.warnings)


def test_item_range_warning_names_alternate(iig3d, cat, tmp_path):
    items = "\n".join(f"  - {{label: L{i}}}" for i in range(9))
    path = tmp_path / "s.yaml"
    path.write_text(f"title: T\nitems:\n{items}\n")
    spec = iig3d.load_spec(path)
    prompt = iig3d.assemble(cat, spec, iig3d.route(cat, "hub-spoke", "3d-target-callout"), "16:9")
    warning = next(w for w in prompt.warnings if "items" in w)
    assert "9" in warning and "3d-capsule-hub" in warning


def test_strict_raises(iig3d, cat, tmp_path):
    items = "\n".join(f"  - {{label: L{i}}}" for i in range(9))
    path = tmp_path / "s.yaml"
    path.write_text(f"title: T\nitems:\n{items}\n")
    spec = iig3d.load_spec(path)
    with pytest.raises(iig3d.UsageError):
        iig3d.assemble(cat, spec, iig3d.route(cat, "hub-spoke", "3d-target-callout"), "16:9", strict=True)


def test_api_key_pattern_redacted(iig3d, cat, tmp_path):
    path = tmp_path / "s.yaml"
    path.write_text("title: T\nnotes: key AIzaSyD-1234567890abcdefghijklmnopqrstuv here\nitems:\n  - label: A\n")
    spec = iig3d.load_spec(path)
    prompt = iig3d.assemble(cat, spec, iig3d.route(cat, "dashboard", None), "16:9")
    assert "AIza" not in prompt.text and "[redacted]" in prompt.text
