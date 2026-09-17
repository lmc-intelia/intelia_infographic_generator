# Plan: iig3d skill
From: spec.md (2026-09-17). Status: accepted. Risk: low.

## Files that change
Repository root:
- pyproject.toml (new)
- .python-version (new)
- uv.lock (new)
- .sdlc.toml
- .gitignore
- .pre-commit-config.yaml (new)
- justfile
- .claude/skills/iig3d (new, symlink -> ../../skills/iig3d)

Skill:
- skills/iig3d/SKILL.md (new)
- skills/iig3d/scripts/iig3d.py (new)
- skills/iig3d/catalogue/family.yaml (new)
- skills/iig3d/catalogue/schema.yaml (new)
- skills/iig3d/catalogue/members/3d-slab-stack.yaml (new)
- skills/iig3d/catalogue/members/3d-arrow-ribbon.yaml (new)
- skills/iig3d/catalogue/members/3d-disc-timeline.yaml (new)
- skills/iig3d/catalogue/members/3d-paper-tile.yaml (new)
- skills/iig3d/catalogue/members/3d-gradient-pedestal.yaml (new)
- skills/iig3d/catalogue/members/3d-capsule-hub.yaml (new)
- skills/iig3d/catalogue/members/3d-isometric-light.yaml (new)
- skills/iig3d/catalogue/members/3d-isometric-dark.yaml (new)
- skills/iig3d/catalogue/members/3d-target-callout.yaml (new)
- skills/iig3d/catalogue/members/3d-hex-cluster.yaml (new)
- skills/iig3d/catalogue/members/3d-cylinder-column.yaml (new)
- skills/iig3d/catalogue/members/3d-glass-layer.yaml (new)
- skills/iig3d/templates/base-prompt.md (new)
- skills/iig3d/templates/spec.example.yaml (new)
- skills/iig3d/templates/meta.example.yaml (new)
- skills/iig3d/docs/CATALOGUE.md (new, generated)
- skills/iig3d/docs/members/3d-slab-stack.md (new, generated)
- skills/iig3d/docs/members/3d-arrow-ribbon.md (new, generated)
- skills/iig3d/docs/members/3d-disc-timeline.md (new, generated)
- skills/iig3d/docs/members/3d-paper-tile.md (new, generated)
- skills/iig3d/docs/members/3d-gradient-pedestal.md (new, generated)
- skills/iig3d/docs/members/3d-capsule-hub.md (new, generated)
- skills/iig3d/docs/members/3d-isometric-light.md (new, generated)
- skills/iig3d/docs/members/3d-isometric-dark.md (new, generated)
- skills/iig3d/docs/members/3d-target-callout.md (new, generated)
- skills/iig3d/docs/members/3d-hex-cluster.md (new, generated)
- skills/iig3d/docs/members/3d-cylinder-column.md (new, generated)
- skills/iig3d/docs/members/3d-glass-layer.md (new, generated)

Reference images, 19 clean originals copied from `~/.agents/skills/baoyu-infographic/references/styles/<member>/` (resized to ≤1600 px where larger):
- skills/iig3d/refs/3d-slab-stack/ref-01-stacked-slabs.jpg (new)
- skills/iig3d/refs/3d-slab-stack/ref-02-staircase-steps.jpg (new)
- skills/iig3d/refs/3d-slab-stack/ref-03-folded-ribbon-tiers.jpg (new)
- skills/iig3d/refs/3d-arrow-ribbon/ref-01-chevron-arrow-flow.jpg (new)
- skills/iig3d/refs/3d-arrow-ribbon/ref-02-folded-ribbon-tiers.jpg (new)
- skills/iig3d/refs/3d-disc-timeline/ref-03-disc-chain-track.jpg (new)
- skills/iig3d/refs/3d-paper-tile/ref-01-tile-chart-set.jpg (new)
- skills/iig3d/refs/3d-paper-tile/ref-02-semicircle-tabs.jpg (new)
- skills/iig3d/refs/3d-paper-tile/ref-03-hexagon-tree.jpg (new)
- skills/iig3d/refs/3d-gradient-pedestal/ref-01-four-pedestals.jpg (new)
- skills/iig3d/refs/3d-capsule-hub/ref-03-segment-ring.jpg (new)
- skills/iig3d/refs/3d-capsule-hub/ref-04-comparision.jpg (new)
- skills/iig3d/refs/3d-capsule-hub/ref-05-rimmed-capsule-wheel.jpg (new)
- skills/iig3d/refs/3d-isometric-light/ref-01-smart-city-platform.jpg (new)
- skills/iig3d/refs/3d-isometric-light/ref-03-factory-workflow-scene.jpg (new)
- skills/iig3d/refs/3d-isometric-light/ref-04-stacked-platform-tiers.jpg (new)
- skills/iig3d/refs/3d-isometric-dark/ref-01-ribbon-dataviz.jpg (new)
- skills/iig3d/refs/3d-target-callout/ref-01-target-four-pills.jpg (new)
- skills/iig3d/refs/3d-hex-cluster/ref-01-honeycomb-hub.jpg (new)

Reference images, 11 clean regenerations replacing watermarked originals (same file names so pairings hold; R21):
- skills/iig3d/refs/3d-disc-timeline/ref-01-rimmed-disc-timeline.jpg (new)
- skills/iig3d/refs/3d-disc-timeline/ref-02-s-curve-ribbon-discs.jpg (new)
- skills/iig3d/refs/3d-disc-timeline/ref-04-serpentine-ribbon.jpg (new)
- skills/iig3d/refs/3d-capsule-hub/ref-01-capsule-hub.jpg (new)
- skills/iig3d/refs/3d-capsule-hub/ref-02-central-disc-ribbon.jpg (new)
- skills/iig3d/refs/3d-isometric-dark/ref-02-isometric-city.jpg (new)
- skills/iig3d/refs/3d-isometric-dark/ref-03-glass-bar-towers.jpg (new)
- skills/iig3d/refs/3d-isometric-light/ref-02-road-timeline-cubes.jpg (new)
- skills/iig3d/refs/3d-target-callout/ref-02-target-six-pills-symmetric.jpg (new)
- skills/iig3d/refs/3d-cylinder-column/ref-01-stepped-cylinders-arrows.jpg (new)
- skills/iig3d/refs/3d-glass-layer/ref-01-five-glass-layers.jpg (new)

Tests:
- tests/conftest.py (new)
- tests/test_cli.py (new)
- tests/test_catalogue.py (new)
- tests/test_routing.py (new)
- tests/test_aspect.py (new)
- tests/test_spec.py (new)
- tests/test_refs.py (new)
- tests/test_palette.py (new)
- tests/test_prompt.py (new)
- tests/test_creds.py (new)
- tests/test_render.py (new)
- tests/test_docs.py (new)
- tests/test_add.py (new)
- tests/test_skill_md.py (new)
- tests/test_install.py (new)
- tests/fixtures/sample-prompt-industrial-3d.md (new)
- tests/fixtures/sample-prompt-3d-disc-timeline.md (new)
- tests/fixtures/brand.css (new)
- tests/fixtures/wide-3000px.jpg (new)
- tests/fixtures/spec-pipeline.yaml (new)

## Order of work
Conventions for every step: write the test file first; `sdlc build red <step>` must fail; implement; `sdlc build green <step>`; `sdlc build sync`; commit `build(iig3d-skill): <step>`. All commands run from the repository root. The script is one file; sections are marked with `# --- <section> ---` comments in the order listed in spec.md Design. Every subcommand prints exactly one JSON object to stdout; diagnostics go to stderr. Source material for the catalogue is read from `~/.agents/skills/baoyu-infographic/references/` once, during steps 2 and 13, and never at run time.

1. **scaffold** — test: `tests/test_cli.py::test_module_imports_and_has_main` (imports `iig3d` via `tests/conftest.py`, which inserts `skills/iig3d/scripts` on `sys.path`; asserts `main` callable and `SUBCOMMANDS == ["list","route","refs","prompt","render","add","docs","check","palette"]`). Red: no script, and `pytest` is not on PATH. Green: root `pyproject.toml` (`[project] name="iig3d-dev"`, `requires-python=">=3.10"`, `dependencies=["google-genai>=1.0.0","pillow>=10.0.0","pyyaml>=6.0"]`, `[dependency-groups] dev=["pytest>=8"]`, `[tool.pytest.ini_options] testpaths=["tests"]`), `.python-version` = `3.12` (google-genai wheels are not yet verified on 3.14), `.sdlc.toml` `[commands] test = "uv run pytest -q"`, `skills/iig3d/scripts/iig3d.py` with PEP 723 header, `SUBCOMMANDS`, argparse skeleton whose subcommands each raise `NotImplementedError`, `main()` returning an exit code.
2. **catalogue** — test: `tests/test_catalogue.py` (`load()` returns 12 members named exactly as spec R3; every member has the keys in spec R3; every `prompt_fragment` ends with the family `negative_list` sentence "Clean premium business-template 3D."; `family.routing` has 21 rows whose `primary` and `alternates` name existing members; every pairing layout is a routing row key or the member's own name; every pairing ref id exists in that member's `refs`; every ref has `flags` ⊆ {clean, watermark, low-res}; `schema.yaml` rejects a member missing `prompt_fragment`). Green: `catalogue/family.yaml` (palette, typography, negative_list, aspect_map, supported_ratios, text_budget, routing table transcribed from `3d-family.md` "Layout routing"), `catalogue/schema.yaml` (required keys and types, hand-written, validated by a 40-line walker, no jsonschema dependency), 12 member YAML files transcribed from `references/styles/3d-<member>.md` and `references/layouts/3d-<member>.md` (prompt fragment verbatim; refs table with the source flags; pairings from "Recommended Pairings" parsing the `(refs NN, NN)` lists; `items` min/max from the composition rules; `alternates` from the routing table), plus the `catalogue` section (`load`, `Catalogue`, `validate_member`).
3. **routing** — test: `tests/test_routing.py` (parametrised over all 21 routing rows with style omitted and with `industrial-3d`; each of the 12 device names as layout; each member as explicit style with any layout; unknown layout and unknown style raise `UsageError` whose message lists valid names). Green: `routing` section, `Route` dataclass, `UsageError`.
4. **aspect-spec** — tests: `tests/test_aspect.py` (presets; every supported ratio round-trips; `2.35:1`→`21:9`, `4:1`→`21:9`, `1:2`→`9:16`, `1.5:1`→`3:2`; `snapped_from` set only when snapped; `None` uses the member default) and `tests/test_spec.py` (loads `tests/fixtures/spec-pipeline.yaml`; missing `title`, missing `items`, item without `label`, unknown top-level key each raise `UsageError` naming the key; `palette_css` relative path resolves against the spec directory; defaults `language="en"`). Green: `aspect` and `spec` sections, `Spec` and `Item` dataclasses.
5. **refs** — test: `tests/test_refs.py` using a temporary catalogue fixture with dummy JPEGs (built in `conftest.py` by `tmp_catalogue`): pairing order honoured; clean refs first; two `watermark` refs never both selected; a `low-res` ref never returned alone; falls back to the first pairing, then all refs, when the layout has no pairing; user refs appended; total capped at 6; every returned path exists; a missing ref file raises `UsageError`. Green: `refs` section `select_refs`.
6. **palette** — test: `tests/test_palette.py` with `tests/fixtures/brand.css` (`:root` custom properties in mixed order including `--brand-grey: #9aa3ae`, `--white: #fff`, `rgb(31,181,200)`, `hsl(210 80% 40%)`, a duplicate, ten distinct saturated colours): declaration order kept; hex normalised upper-case `#RRGGBB`; neutrals dropped by the HSL rule; duplicates dropped; capped at 8; `vars=[...]` restricts and orders; fewer than 3 usable raises `UsageError` naming the file; `palette_paragraph` starts with "Project palette override:". Green: `palette` section (`Colour`, `extract_palette`, `palette_paragraph`; regex for `--name:\s*value`, `#[0-9a-f]{3,8}`, `rgba?\(`, `hsla?\(`; HSL maths with `colorsys`).
7. **prompt** — test: `tests/test_prompt.py`: assembling `tests/fixtures/spec-pipeline.yaml` with layout `linear-progression` and style `3d-disc-timeline` yields a body whose "## Style Guidelines" paragraph equals the one in `tests/fixtures/sample-prompt-3d-disc-timeline.md` and whose "Text labels" block equals that fixture's block; same for `industrial-3d` against `sample-prompt-industrial-3d.md` (routes to `3d-disc-timeline`, so `style_member` is recorded and the fragment is the member's); frontmatter has `layout, style, style_member, aspect, language, references`; `palette` block present when a CSS path is given and the override paragraph follows the fragment; `write_prompt` twice yields `01-` then `02-`; word budget warning at 121 landscape words and 161 portrait; item-range warning names the first alternate; `strict=True` raises; a `AIza...` string in `notes` is replaced by `[redacted]`. Green: `templates/base-prompt.md` (copied from the fork with the same slots), `prompt` section (`assemble`, `write_prompt`, `render_layout_block`, `text_labels`, `word_count`, `redact`).
8. **creds** — test: `tests/test_creds.py` with `monkeypatch.chdir(tmp)`: `./.env` with `GEMINI_API_KEY` wins over env var; `GOOGLE_API_KEY` accepted; env var used when no `.env`; explicit key wins over both; a `.env` in the parent directory is ignored; missing everything raises `UsageError` with message `no API key: expected GEMINI_API_KEY in <cwd>/.env or the environment`; the key value never appears in the returned `source` string. Green: `creds` section (`parse_env_file` ported from the fork runner, `api_key`).
9. **render** — test: `tests/test_render.py`: `render(..., dry_run=True)` returns `status: dry-run` with every key of spec R11 and creates no PNG; with a fake `genai` client (a `conftest.py` stub exposing `models.generate_content` returning parts with `inline_data`) a PNG is written, RGBA is flattened to RGB, the JSON has `attempts: 1`; on a raised exception it retries `retries` times then returns `status: error` and exit code 2; a response without an image part returns exit 2; an existing `infographic.png` is renamed to `infographic-backup-YYYYMMDD-HHMMSS.png`; refs are passed as PIL images followed by the "style reference only" sentence; a live smoke test decorated `@pytest.mark.skipif(not os.environ.get("IIG3D_LIVE"))`. Green: `render` section ported from the fork's `generate_image.py` `main()` body (client construction injected for testing via `client_factory`).
10. **cli** — test: `tests/test_cli.py` extended: every subcommand invoked through `main([...])` with `capsys` prints exactly one JSON object; `list` reports 12 members and 21 layouts; `route`, `refs`, `palette`, `prompt --dry`, `render --dry-run` return the shapes from spec; usage errors exit 1 with a JSON `{"status":"error","error":...}` on stdout and nothing else; `render` refuses without `--out-dir`. Green: `cli` section wiring every section; `--json` is implicit (always JSON).
11. **docs** — test: `tests/test_docs.py`: `render_docs` on the shipped catalogue writes `docs/CATALOGUE.md` with the family table, routing table and palette, and 12 `docs/members/<member>.md` files with the sections listed in spec R14; output is byte-stable across two runs; `check()` reports `docs stale: <path>` after a member YAML edit. Green: `docs` section (string templates, no external engine).
12. **add** — test: `tests/test_add.py` on `tmp_catalogue`: `add_ref(image=tests/fixtures/wide-3000px.jpg, meta={member, shows, flags:[clean], pairings})` writes `refs/<member>/ref-NN-<slug>.jpg` at 1600 px long edge, RGB JPEG; appends the ref to the member YAML with `source: {path, added}`; regenerates docs; `check()` is clean; `meta` with `new_member` creates the YAML, its refs folder, and appends the member to the named routing rows' `alternates`; meta that names an existing ref id raises `UsageError`; meta missing `shows` or `flags` raises `UsageError` naming the key; NN increments past the highest existing id. Green: `add` section, `templates/meta.example.yaml`.
13. **check-and-refs** — test: `tests/test_catalogue.py` extended with `test_ref_files_on_disk` (every catalogue ref exists under `skills/iig3d/refs`, is JPEG, long edge ≤1600 px) and `test_no_vendored_watermark` (no ref has the `watermark` flag unless `source.user_added` is true), and `tests/test_catalogue.py::test_check_clean` (`check()` on the shipped catalogue returns `[]`, including the dry-run assembly for every member × pairing layout with zero ref-rule violations). Red because no ref files exist yet. Green, in this order: (a) copy the 19 clean originals listed above, resizing `3d-capsule-hub/ref-04-comparision.jpg` from 3000 px to 1600 px through the same `normalise_image` used by `add`; (b) with `GEMINI_API_KEY` in `./.env` (copy from `../intelia_knowledge_base/.env`; not committed), regenerate the 11 watermarked refs: for each, `uv run skills/iig3d/scripts/iig3d.py render --spec skills/iig3d/templates/spec.example.yaml --style <member> --layout <first pairing layout of that ref> --ref <original watermarked file under ~/.agents> --out-dir /tmp/…/regen/<member>-<NN> --resolution 2K`, view the PNG, reject and rerun once if a watermark or stock badge is visible, then `iig3d.py add --image <png> --meta <meta.yaml>` with the original's `shows` text, `flags: [clean]`, the original's pairings, and `file` forced to the original file name; (c) flip the catalogue entries from `watermark`/`low-res` to `clean` (the `add` path does this when `file` matches an existing entry that has no file on disk); (d) run `iig3d.py docs` and `iig3d.py check`. Never copy a watermarked original into `skills/iig3d/refs`.
14. **skill-md** — test: `tests/test_skill_md.py`: `skills/iig3d/SKILL.md` has frontmatter `name: iig3d` and a `description` containing "3d infographic", "industrial 3d" and "iig3d"; at most 80 lines; every subcommand in `SUBCOMMANDS` appears in the command table; contains the sentence "Confirm member, layout, aspect and language once before render" and the question "Load a CSS file for brand colours?"; names `./.env`; states the two policies "never emit SVG/HTML" and "never paint over rendered text"; `templates/spec.example.yaml` loads as a valid spec. Green: `SKILL.md` (sections: When to use; Start of skill: palette question; Content spec (YAML block copied from `templates/spec.example.yaml`); Commands (table); Rules (confirm gate, `.env`, two policies, add flow in four lines)); `templates/spec.example.yaml` = the OpenWiki pipeline content used by the fork's sample prompts.
15. **install** — test: `tests/test_install.py` (skipped when `just` is absent): with `HOME` pointed at a temp dir and a temp copy of the repo, `just install-local` creates `~/.claude/skills/iig3d` and `.claude/skills/iig3d` symlinks resolving to `skills/iig3d`; a pre-existing real directory at either target makes it exit 1 without changes; `just uninstall-local` removes both links and leaves a real directory alone. Green: `justfile` recipes `install-local`, `uninstall-local`, `test` (`uv run pytest -q`), `iig3d-check`; append `infographic/` to `.gitignore`; run `just install-local` for real and commit the in-repo symlink `.claude/skills/iig3d`.
16. **acceptance-renders** (manual, after `/simplify` and the final `sdlc build sync`) — for each of the 12 members: `uv run skills/iig3d/scripts/iig3d.py render --spec skills/iig3d/templates/spec.example.yaml --style <member> --out-dir infographic/acceptance/<member> --no-confirm`; view each PNG; product owner accepts or names the member to redo. Outputs are not committed.

## Risks
- **Riskiest step: 13 (regenerating 11 refs).** Needs a live Gemini key in `./.env` (none in this repo today; sibling repo `../intelia_knowledge_base/.env` has one) and 11 to 22 Pro image calls. A regeneration may echo the stock watermark from its style ref; mitigation: view every output, rerun once with the watermark sentence strengthened in `notes`, and if still visible use a clean sibling ref of the same member instead of the watermarked original. Regenerated images are renders of the OpenWiki fixture content, so their `shows` text is rewritten by Claude to describe the new image, not the original.
- **Prompt fidelity (step 7).** The fork's `sample-prompt.md` files put the general `linear-progression` layout text in the Layout Guidelines slot; this skill puts the member's device layout block there (accepted as Concern 5). The test therefore compares only the Style Guidelines paragraph and the Text labels block, not the whole body. Rejected: vendoring the 21 general layout files, which would reintroduce prose the intent excludes.
- **Dependency drift.** `pyproject.toml` and the PEP 723 header list the same three runtime packages; `check()` compares them and `test_catalogue.py::test_check_clean` would fail on drift. `google-genai` on Python 3.14 is unverified, hence `.python-version` 3.12; if `uv` cannot find 3.12 it downloads it.
- **`build sync` exact matching.** Every file the build creates must be listed above, including all 30 ref JPEGs, 13 generated markdown files and the in-repo symlink; a stray file (for example `infographic/` output or `.env`) fails sync. `.gitignore` already covers `.env` and `__pycache__/`; step 15 appends `infographic/` so smoke and acceptance renders never count as unplanned.
- **Interactive parts.** The confirmation gate and the palette question live in SKILL.md and are exercised by Claude, not by tests; `test_skill_md.py` only asserts the text exists. Rejected: putting a TTY prompt in the script, which would break non-interactive use.
- **Add command writes into the skill directory.** When the skill is installed by symlink this edits the repository checkout, which is intended; when installed by `npx skills add --copy` it edits the copy, and the user must re-add in the source repo to share. Documented in SKILL.md; not solved.
- **Chosen not to do:** general layouts and styles; EXTEND.md preferences; plugin fallback runner; CSS parsing beyond regex (no `@import`, no `var()` resolution beyond one level); a JSON schema library; a `tests/` per-member golden image comparison (non-deterministic model output).

## Proof
- `uv run pytest -q` → all tests pass; expected final count ≥ 90 tests, 1 skipped (`IIG3D_LIVE` smoke) plus `test_install.py` skipped only when `just` is absent.
- `uv run skills/iig3d/scripts/iig3d.py check` → `{"status":"ok","violations":[]}`; exit 0.
- `uv run skills/iig3d/scripts/iig3d.py list` → JSON with `members` length 12 and `layouts` length 21.
- `uv run skills/iig3d/scripts/iig3d.py route --layout hierarchical-layers` → `{"member":"3d-slab-stack","alternates":["3d-glass-layer","3d-isometric-light","3d-cylinder-column"],...}`.
- `uv run skills/iig3d/scripts/iig3d.py palette --css tests/fixtures/brand.css` → JSON `colours` list of 8 entries, no greys.
- `cd /tmp && mkdir -p nokey && cd nokey && uv run <abs>/skills/iig3d/scripts/iig3d.py render --spec <abs>/skills/iig3d/templates/spec.example.yaml --out-dir out --dry-run` → exit 1, stdout JSON `error` = `no API key: expected GEMINI_API_KEY in /tmp/nokey/.env or the environment`.
- With `./.env` present: `uv run skills/iig3d/scripts/iig3d.py render --spec skills/iig3d/templates/spec.example.yaml --out-dir infographic/smoke --dry-run` → `{"status":"dry-run",...,"prompt_file":".../prompts/01-infographic-openwiki-refresh-pipeline.md"}` and the prompt file exists; without `--dry-run` → `status: ok` and `infographic/smoke/infographic.png` exists.
- `ls skills/iig3d/refs/*/ | wc -l` → 30 JPEG files; `grep -rl watermark skills/iig3d/catalogue/members/` → no output.
- `wc -l skills/iig3d/SKILL.md` → ≤ 80.
- `ls -l ~/.claude/skills/iig3d .claude/skills/iig3d` → both symlinks resolve to `skills/iig3d`.
- `sdlc build sync` → `{"ok": true, "unplanned": []}` after every step; `sdlc build check` → `ok: true`.
- Acceptance: 12 PNGs under `infographic/acceptance/<member>/infographic.png` reviewed by the product owner.
