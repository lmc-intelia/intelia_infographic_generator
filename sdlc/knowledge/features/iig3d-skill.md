---
type: Feature
title: iig3d skill
description: The 3D corporate infographic capability built on 2026-09-15 to 2026-09-17 lives inside the
resource: sdlc/iig3d-skill
tags: [feature, accepted]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T01:19:06Z" }
verified:
  - { by: "human:linus-mcmanamey", at: "2026-09-17T00:38:17Z" }
  - { by: "human:linus-mcmanamey", at: "2026-09-17T00:56:26Z" }
  - { by: "human:linus-mcmanamey", at: "2026-09-17T01:07:19Z" }
stale_after: "2026-10-01T01:19:06Z"
source_commit: c41d6d6a630903c77274cef3967923ec721af525
sources:
  - { id: intent, resource: sdlc/iig3d-skill/intent.md, last_modified: "2026-09-17T10:38:23+10:00", digest: a2d1906944e50ff8 }
  - { id: spec, resource: sdlc/iig3d-skill/spec.md, last_modified: "2026-09-17T11:13:02+10:00", digest: 4948ad7b23ac3a24 }
  - { id: plan, resource: sdlc/iig3d-skill/plan.md, last_modified: "2026-09-17T11:15:25+10:00", digest: 4835459672b9e05e }
---

# Problem
The 3D corporate infographic capability built on 2026-09-15 to 2026-09-17 lives inside the
`baoyu-infographic` fork at `~/.agents/skills/baoyu-infographic` (version 2.1.0-lmc). It is
one part of a general catalogue: 12 `3d-*` device layouts sit beside 21 general layouts, 12
`3d-*` member styles plus the `industrial-3d` umbrella sit beside 23 general styles, and the
routing table, palette, typography, reference-image rules and negative list are spread across
`references/styles/3d-family.md`, twelve style files, twelve layout files,
`references/base-prompt.md` and `references/nano-banana-pro.md`.

To render one 3D infographic today Claude must read a 400-line prose SKILL.md, then load the
family file, the chosen layout file, the chosen style file, the base prompt template and the
backend contract, route `industrial-3d` to a member by hand from a table, pick 2 to 3
reference images by hand while honouring four flag rules (clean first, never two watermarked,
never a low-res ref alone, cap of 6), snap the aspect ratio to the Gemini set, check the
on-image text budget, assemble the prompt file by hand, and only then call the runner. Every
one of those steps is deterministic yet is done by the model, so it costs tokens on every run
and drifts between runs (wrong ref pairing, unsupported ratio, missing negative list, wrong
family colour cycle for the member). The first-time EXTEND.md interview, keyword shortcuts and
five-step confirmation workflow add further prose that is not needed when the user has
already decided on the 3D family.

Affected: Linus McManamey as the sole author and operator, and this repository
(`intelia_infographic_generator`), which exists to produce Intelia-branded infographics and
today has no skill of its own.

# Outcome
A self-contained Claude Code skill named `iig3d` lives in this repository and produces 3D
corporate-family infographics only. It reverse-engineers the current baoyu 3D functionality
so that a user can run it without the baoyu skills installed.

What better looks like:

- **Python holds the rules, SKILL.md holds the trigger.** A single script (PEP 723 inline
  dependencies, run with `uv run`) exposes subcommands such as `list`, `route`, `prompt`,
  `render` and `check`. SKILL.md is short (target under 80 lines): trigger phrases, the
  content-spec format Claude must write, one command table, and the two hard rules that
  need judgement. No layout galleries, no recommendation prose, no interview flows.
- **Catalogue as data, not prose.** The 12 members are encoded once in a YAML catalogue the
  script loads: device name, structural rules distilled to short bullet strings,
  the verbatim Prompt Fragment, item-count limits, aspect defaults, per-layout reference
  picks, and every reference image with its `clean` / `watermark` / `low-res` flags. The
  shared palette hex values, typography block and family negative list are constants.
- **Routing in code.** `industrial-3d` plus any of the 21 general layout names resolves to a
  primary member and alternates via the table in `3d-family.md`. Naming a `3d-*` member
  directly skips routing. Both the member's own device layout and a general layout are
  accepted.
- **Reference selection in code.** Given member and layout the script returns 2 to 3 refs
  following the flag rules, adds user `direct` refs, and caps at 6. Reference JPEGs are
  vendored into the skill so nothing is read from `~/.agents` at run time.
- **Prompt assembly in code.** Base template plus layout guidelines plus member fragment plus
  family negative list plus the content block plus quoted text labels, with the aspect ratio
  snapped to `1:1 3:2 2:3 3:4 4:3 4:5 5:4 9:16 16:9 21:9` and a warning when on-image text
  exceeds about 120 words at 16:9 or 160 at 9:16. The prompt is written to
  `prompts/NN-infographic-<slug>.md` with frontmatter (layout, style, style_member, aspect,
  references) before any API call, and existing outputs are renamed with a timestamp
  suffix rather than overwritten.
- **Rendering in code.** The bundled Nano Banana Pro runner logic (Gemini `gemini-3-pro-image`
  through `google-genai`, `--aspect-ratio`, repeatable `--ref`, `--dry-run`, retries, single
  JSON result line, exit codes 0/1/2) is vendored into the skill script.
- **Credentials from the caller's directory.** The user keeps `GEMINI_API_KEY=...` in a
  `.env` file in the directory they call the skill from. The script reads that file first, then
  falls back to `GEMINI_API_KEY` / `GOOGLE_API_KEY` already in the environment. It does not
  walk up parent directories. When neither exists it exits 1 and names the exact `.env` path
  it expected, so the fix is one line in one obvious place.
- **User-added reference images.** An `add` subcommand takes any image the user supplies (a
  template screenshot, a stock preview, a rendered infographic they like) and gives it the
  same build-out every vendored reference already has. The script does the deterministic
  part: copy, resize to at most 1600 px on the long edge, convert to JPEG, name it
  `ref-NN-<slug>.jpg` under the chosen member (or a new `3d-<name>` member folder), and
  register it in the catalogue with its flags and per-layout pairings. Claude does the
  judgement part by looking at the image: decide whether it belongs to an existing member or
  founds a new one, describe what it shows, flag `clean` / `watermark` / `low-res`, draft the
  structural rules, Prompt Fragment, best-for list and layout pairings, and write or update
  the member's markdown (style file, device layout file, family table row) in the same
  format the twelve existing members use. The catalogue is therefore a data file the script
  loads, not Python constants, so a new member needs no code change. This is the same
  process that produced the six members added on 2026-09-17 from Greenshot screenshots, made
  repeatable.
- **Claude's remaining job** is the part that needs judgement: turn the user's source into a
  small content spec (title, subtitle, ordered items with label and one-line detail,
  optional stats, language) and pick or confirm the member. Everything after that is one
  command.

Success looks like:

- `pytest -q` passes with tests for routing (every row of the family table), ref selection
  (all four flag rules, cap of 6), aspect snapping, text-budget warning, prompt assembly
  against the two existing `sample-prompt.md` files, and `render --dry-run`.
- `render --dry-run` for all 12 members against each of their paired layouts yields a valid
  prompt file and ref set with zero rule violations.
- One real render per member from a fixture content spec produces an image the author
  accepts as matching the family look shown in the reference screenshots.
- The skill directory works when `~/.agents/skills/baoyu-*` is absent.
- `add` on a fresh screenshot leaves the repository in the same shape as a vendored member:
  resized JPEG in place, catalogue entry with flags and pairings, markdown files present, and
  `check` reports no rule violations. Adding a thirteenth member needs no Python change.
- Running from a directory without `.env` fails fast with the expected path in the message;
  running with `.env` present renders.

# Requirements
Each requirement traces to intent.md (I-outcome, I-success, I-constraints, I-decisions).

1. **Skill layout** (I-outcome, I-decisions). `skills/iig3d/` at the repository root holds `SKILL.md`, `scripts/iig3d.py`, `catalogue/`, `refs/`, `templates/`. `SKILL.md` has frontmatter `name: iig3d` and a `description` that triggers on "3d infographic", "industrial 3d", "iig3d", and is at most 80 lines.
2. **Standalone** (I-success). The skill runs with only `uv` on the PATH and never reads `~/.agents`, `~/.baoyu-skills` or the `nano-banana-pro` plugin. `scripts/iig3d.py` carries a PEP 723 header (`google-genai>=1.0.0`, `pillow>=10.0.0`, `pyyaml>=6.0`), so `uv run skills/iig3d/scripts/iig3d.py ...` works from a fresh `npx skills add` install.
3. **Catalogue as data** (I-outcome). `catalogue/family.yaml` holds palette, typography, negative list, aspect map, text budget and the layout routing table. `catalogue/members/<member>.yaml` holds one member each (12 files) with: `device`, `backdrop`, `layout` (structure, variants, text placement bullets), `prompt_fragment` (verbatim from the source style file), `best_for`, `items` `{min, max}`, `aspect_default`, `refs` (file, shows, flags), `pairings` (layout → ordered ref ids), `alternates`, `source` (origin note). Adding a member is adding one YAML file and one refs folder; no Python edit.
4. **Routing** (I-outcome). `route --layout L [--style S]` returns `{member, alternates, reason}`. `S` omitted or `industrial-3d`: `L` is looked up in the family routing table (every row of `3d-family.md`, 21 general layouts); `L` equal to a member's own device name (`3d-*`) returns that member. `S` equal to a `3d-*` member returns it and skips the table. Unknown `L` or `S` exits 1 with the valid lists.
5. **Reference selection** (I-outcome). `refs --member M --layout L [--ref FILE]...` returns 2 to 3 member refs from the member's `pairings[L]` (fallback: first pairing entry, then all refs in order), ordered clean first, with: never two `watermark` refs together, never a `low-res` ref alone or as the only clean-free pick, user refs appended, total capped at 6. Every selected path exists on disk.
6. **Content spec** (I-decisions). Input is one YAML file: `title` (required), `subtitle`, `language` (default `en`), `layout`, `style`, `aspect`, `palette_css`, `palette_vars[]`, `items[]` (`label` required, `detail`, `icon`, `value`), `stats[]` (`value`, `caption`), `notes`, `refs[]`. Unknown keys or a missing `title`/`items` exit 1 naming the key.
7. **Aspect snapping** (I-outcome). Named presets map landscape→`16:9`, portrait→`9:16`, square→`1:1`. Any `W:H` outside `1:1 3:2 2:3 3:4 4:3 4:5 5:4 9:16 16:9 21:9` snaps to the nearest supported ratio by numeric value and the result carries `aspect_snapped_from`. Missing aspect uses the member's `aspect_default`.
8. **Prompt assembly** (I-outcome). `prompt --spec F --out-dir D [...]` writes `D/prompts/NN-infographic-<slug>.md` (NN = next free two-digit number, never overwriting) with YAML frontmatter `{layout, style, style_member, aspect, language, references[]}` and a body built from `templates/base-prompt.md` slots: `{{LAYOUT}}`, `{{STYLE}}`, `{{ASPECT_RATIO}}`, `{{LANGUAGE}}`, `{{LAYOUT_GUIDELINES}}` (member `layout` block rendered as markdown), `{{STYLE_GUIDELINES}}` (member `prompt_fragment`, plus the family negative list when the fragment lacks it), `{{CONTENT}}` (title, subtitle, numbered items `NN. "LABEL" - detail`, stats, notes), `{{TEXT_LABELS}}` (one quoted line each: title, subtitle, `"NN LABEL"`, stat values). Output JSON lists `warnings`.
9. **Guards as warnings** (I-outcome). `prompt` warns, not fails, when on-image words exceed 120 for landscape ratios or 160 for portrait ratios (`1:1` counts as landscape), and when item count is outside the member's `items` range (suggesting the first alternate). `--strict` turns warnings into exit 1.
10. **Credentials** (I-decisions). `render` reads `GEMINI_API_KEY` or `GOOGLE_API_KEY` from `./.env` in the current working directory, then from the process environment, then `--api-key`. No parent-directory walk. Missing key exits 1 with the message `no API key: expected GEMINI_API_KEY in <cwd>/.env or the environment`. The key is never written to any file or stdout.
11. **Render** (I-outcome). `render --spec F --out-dir D [--dry-run] [--resolution 1K|2K|4K] [--model ID] [--retries N] [--no-confirm]` runs steps 4 to 8, then calls Gemini `gemini-3-pro-image` (env `IIG3D_MODEL` overrides) through `google-genai` with `ImageConfig(aspect_ratio, image_size)`, refs prepended with the "style reference only" instruction, saves RGB PNG to `D/infographic.png` (existing file renamed `infographic-backup-YYYYMMDD-HHMMSS.png`), and prints one JSON line `{status, path, bytes, model, aspect_ratio, resolution, refs, attempts, elapsed_seconds, prompt_file, warnings}`. Exit codes: 0 ok, 1 usage or credentials, 2 API or output failure. `--dry-run` prints the same shape with `status: dry-run` and makes no network call.
12. **Confirmation gate** (I-decisions). SKILL.md instructs Claude to state member, layout, aspect, language once and get a yes before `render`, unless the user request includes `--no-confirm` or equivalent wording. The script itself has no interactive prompt.
    - **Palette prompt at skill start** (product owner request 2026-09-17). On the first invocation of the skill in a session, before content analysis, Claude asks one question through the runtime's user-input tool (`AskUserQuestion` in Claude Code): "Load a CSS file for brand colours?" with options: a path the user types (Claude then runs `palette --css PATH` and shows the extracted colours for a yes), "no, family palette" (default). The answer is remembered for the session and reused for later renders unless the user names a different file; `--palette-css` or `palette_css` in the spec, or `--no-confirm`, skips the question. When the user's request already names a CSS file the question is skipped and the file is used.
13. **Add reference** (I-outcome, I-success). `add --image PATH --meta META.yaml` where META names `member` (existing) or `new_member` (full member block per R3 minus refs), plus `shows`, `flags[]`, `pairings`. The script: validates META against the member schema; copies the image to `refs/<member>/ref-NN-<slug>.jpg` resized to at most 1600 px on the long edge as RGB JPEG quality 88; appends the ref to the member YAML (creating `catalogue/members/<new>.yaml` and the routing-table `alternates` entries the meta names); records `source: {path, added: date}`; regenerates docs (R14); runs `check` (R15). It never edits an existing ref entry or another member.
14. **Generated markdown** (I-outcome). `docs` renders `skills/iig3d/docs/CATALOGUE.md` (family table, routing table, palette) and `skills/iig3d/docs/members/<member>.md` (same sections as the source style and layout files: device, refs table, palette, visual elements, typography, composition rules, prompt fragment, best for, pairings) from YAML. Markdown is never hand-edited; `check` fails when it is stale.
15. **Check** (I-success). `check` validates every member YAML against the schema, every ref file exists and is ≤1600 px JPEG, flags are from `{clean, watermark, low-res}`, pairings reference known layouts and ref ids, prompt fragments end with the negative list, routing table rows name existing members, docs are fresh, and a dry-run prompt assembles for every member × every pairing layout with zero R5 violations. Exit 1 lists every violation.
16. **List** (I-outcome). `list [--json]` prints members with device, item range, aspect default, ref count; and the 21 general layouts with their primary member.
17. **Install** (I-decisions). `just install-local` creates `~/.claude/skills/iig3d -> <repo>/skills/iig3d` and `.claude/skills/iig3d -> ../../skills/iig3d`, refusing to overwrite a real directory; `just uninstall-local` removes only symlinks it made. `npx skills add <repo>` works because the layout is `skills/<name>/SKILL.md`.
18. **Source policy** (I-constraints). The script never emits SVG, HTML or canvas; never post-processes text in a generated PNG; always writes the prompt file before the API call; strips any string matching an API-key pattern from spec, notes and prompt output.
19. **Repository hygiene** (I-constraints). `.gitignore` lists `.env`, `.venv/`, `__pycache__/`, `infographic/`-style output directories are not ignored (user decides). Root `pyproject.toml` declares the same runtime deps plus `pytest` for the test suite; `.sdlc.toml` test command becomes `uv run pytest -q`.

20. **Brand palette from CSS** (product owner request 2026-09-17, extends the intent's "project palette override replaces the item colours only" rule). `--palette-css PATH` on `prompt` and `render`, or `palette_css: PATH` in the content spec, reads a CSS file from the user's repository and derives the item colours. Extraction: custom properties in declaration order (`--name: <colour>`) first, then any other `#hex`, `rgb()`, `hsl()` literal; values normalised to `#RRGGBB`; duplicates dropped; neutrals dropped (HSL saturation under 15 percent, lightness over 92 or under 10 percent); at most 8 kept. `--palette-vars a,b,c` restricts and orders extraction to named custom properties. Precedence: `--palette-css` flag over `palette_css` in the spec; `--palette-vars` over `palette_vars`. A relative `palette_css` resolves against the spec file's directory; a relative `--palette-css` against the current working directory. A missing file exits 1 naming the resolved path. Fewer than 3 usable colours exits 1 naming the file. The prompt's Style Guidelines gain a trailing paragraph: `Project palette override: cycle item colours in this order: <name> #RRGGBB, ...; never repeat a colour on adjacent items; keep the family backdrop, neutrals, shadows and typography unchanged.` The prompt frontmatter records `palette: {source: <path>, colours: [{name, hex}]}`. Backdrop, neutral and shadow values are never replaced. `palette --css PATH [--vars ...]` prints the extraction as JSON for preview.

21. **Clean replacement of watermarked refs** (Concern 1 resolution, 2026-09-17). The 9 source refs flagged `watermark` (`3d-disc-timeline` 01, 02, 04; `3d-capsule-hub` 01, 02; `3d-isometric-dark` 02, 03; `3d-isometric-light` 02; `3d-target-callout` 02; `3d-cylinder-column` 01; `3d-glass-layer` 01) are not vendored. Before the skill is declared built, each is replaced by a clean image produced by `render` from `templates/spec.example.yaml` content with the original as the only `--ref`, at 2K and the member's `aspect_default`, then registered through `add --meta` with `flags: [clean]`, `shows` written by Claude from the render, and the same pairings the original held. The originals are deleted from the working tree before the first commit that adds `refs/`. `check` fails if any vendored ref carries the `watermark` flag (`--allow-watermark` relaxes this for user-added refs only, recorded per ref as `source.user_added: true`). Cost: 11 Gemini Pro image calls. Two of the eleven (`3d-disc-timeline` 02, `3d-isometric-light` 02) are also `low-res`; their regenerations lift that flag too.

# Files
- `.claude/skills/iig3d`
- `.gitignore`
- `.pre-commit-config.yaml`
- `.python-version`
- `.sdlc.toml`
- `11 clean regenerations replacing watermarked originals :`
- `19 clean originals copied from `~/.agents/skills/baoyu-infographic/references/styles/<member>/` :`
- `Reference images`
- `Repository root:`
- `Skill:`
- `Tests:`
- `justfile`
- `pyproject.toml`
- `skills/iig3d/SKILL.md`
- `skills/iig3d/catalogue/family.yaml`
- `skills/iig3d/catalogue/members/3d-arrow-ribbon.yaml`
- `skills/iig3d/catalogue/members/3d-capsule-hub.yaml`
- `skills/iig3d/catalogue/members/3d-cylinder-column.yaml`
- `skills/iig3d/catalogue/members/3d-disc-timeline.yaml`
- `skills/iig3d/catalogue/members/3d-glass-layer.yaml`
- `skills/iig3d/catalogue/members/3d-gradient-pedestal.yaml`
- `skills/iig3d/catalogue/members/3d-hex-cluster.yaml`
- `skills/iig3d/catalogue/members/3d-isometric-dark.yaml`
- `skills/iig3d/catalogue/members/3d-isometric-light.yaml`
- `skills/iig3d/catalogue/members/3d-paper-tile.yaml`
- `skills/iig3d/catalogue/members/3d-slab-stack.yaml`
- `skills/iig3d/catalogue/members/3d-target-callout.yaml`
- `skills/iig3d/catalogue/schema.yaml`
- `skills/iig3d/docs/CATALOGUE.md`
- `skills/iig3d/docs/members/3d-arrow-ribbon.md`
- `skills/iig3d/docs/members/3d-capsule-hub.md`
- `skills/iig3d/docs/members/3d-cylinder-column.md`
- `skills/iig3d/docs/members/3d-disc-timeline.md`
- `skills/iig3d/docs/members/3d-glass-layer.md`
- `skills/iig3d/docs/members/3d-gradient-pedestal.md`
- `skills/iig3d/docs/members/3d-hex-cluster.md`
- `skills/iig3d/docs/members/3d-isometric-dark.md`
- `skills/iig3d/docs/members/3d-isometric-light.md`
- `skills/iig3d/docs/members/3d-paper-tile.md`
- `skills/iig3d/docs/members/3d-slab-stack.md`
- `skills/iig3d/docs/members/3d-target-callout.md`
- `skills/iig3d/refs/3d-arrow-ribbon/ref-01-chevron-arrow-flow.jpg`
- `skills/iig3d/refs/3d-arrow-ribbon/ref-02-folded-ribbon-tiers.jpg`
- `skills/iig3d/refs/3d-capsule-hub/ref-01-capsule-hub.jpg`
- `skills/iig3d/refs/3d-capsule-hub/ref-02-central-disc-ribbon.jpg`
- `skills/iig3d/refs/3d-capsule-hub/ref-03-segment-ring.jpg`
- `skills/iig3d/refs/3d-capsule-hub/ref-04-comparision.jpg`
- `skills/iig3d/refs/3d-capsule-hub/ref-05-rimmed-capsule-wheel.jpg`
- `skills/iig3d/refs/3d-cylinder-column/ref-01-stepped-cylinders-arrows.jpg`
- `skills/iig3d/refs/3d-disc-timeline/ref-01-rimmed-disc-timeline.jpg`
- `skills/iig3d/refs/3d-disc-timeline/ref-02-s-curve-ribbon-discs.jpg`
- `skills/iig3d/refs/3d-disc-timeline/ref-03-disc-chain-track.jpg`
- `skills/iig3d/refs/3d-disc-timeline/ref-04-serpentine-ribbon.jpg`
- `skills/iig3d/refs/3d-glass-layer/ref-01-five-glass-layers.jpg`
- `skills/iig3d/refs/3d-gradient-pedestal/ref-01-four-pedestals.jpg`
- `skills/iig3d/refs/3d-hex-cluster/ref-01-honeycomb-hub.jpg`
- `skills/iig3d/refs/3d-isometric-dark/ref-01-ribbon-dataviz.jpg`
- `skills/iig3d/refs/3d-isometric-dark/ref-02-isometric-city.jpg`
- `skills/iig3d/refs/3d-isometric-dark/ref-03-glass-bar-towers.jpg`
- `skills/iig3d/refs/3d-isometric-light/ref-01-smart-city-platform.jpg`
- `skills/iig3d/refs/3d-isometric-light/ref-02-road-timeline-cubes.jpg`
- `skills/iig3d/refs/3d-isometric-light/ref-03-factory-workflow-scene.jpg`
- `skills/iig3d/refs/3d-isometric-light/ref-04-stacked-platform-tiers.jpg`
- `skills/iig3d/refs/3d-paper-tile/ref-01-tile-chart-set.jpg`
- `skills/iig3d/refs/3d-paper-tile/ref-02-semicircle-tabs.jpg`
- `skills/iig3d/refs/3d-paper-tile/ref-03-hexagon-tree.jpg`
- `skills/iig3d/refs/3d-slab-stack/ref-01-stacked-slabs.jpg`
- `skills/iig3d/refs/3d-slab-stack/ref-02-staircase-steps.jpg`
- `skills/iig3d/refs/3d-slab-stack/ref-03-folded-ribbon-tiers.jpg`
- `skills/iig3d/refs/3d-target-callout/ref-01-target-four-pills.jpg`
- `skills/iig3d/refs/3d-target-callout/ref-02-target-six-pills-symmetric.jpg`
- `skills/iig3d/scripts/iig3d.py` in [iig3d.py](/modules/iig3d-py.md)
- `skills/iig3d/templates/base-prompt.md`
- `skills/iig3d/templates/meta.example.yaml`
- `skills/iig3d/templates/spec.example.yaml`
- `tests/__init__.py`
- `tests/conftest.py` in [conftest.py](/modules/conftest-py.md)
- `tests/fixtures/brand.css`
- `tests/fixtures/sample-prompt-3d-disc-timeline.md`
- `tests/fixtures/sample-prompt-industrial-3d.md`
- `tests/fixtures/spec-pipeline.yaml`
- `tests/fixtures/wide-3000px.jpg`
- `tests/test_add.py`
- `tests/test_aspect.py` in [test_aspect.py](/modules/test-aspect-py.md)
- `tests/test_catalogue.py` in [test_catalogue.py](/modules/test-catalogue-py.md)
- `tests/test_cli.py`
- `tests/test_creds.py`
- `tests/test_docs.py`
- `tests/test_install.py`
- `tests/test_palette.py` in [test_palette.py](/modules/test-palette-py.md)
- `tests/test_prompt.py`
- `tests/test_refs.py` in [test_refs.py](/modules/test-refs-py.md)
- `tests/test_render.py`
- `tests/test_routing.py` in [test_routing.py](/modules/test-routing-py.md)
- `tests/test_skill_md.py`
- `tests/test_spec.py` in [test_spec.py](/modules/test-spec-py.md)
- `uv.lock`

# Review
- no review yet

# Status
- intent.md: accepted
- spec.md: accepted
- plan.md: accepted
- test-report: missing or failed
- deployed: nowhere

# Documents
- build: sdlc/iig3d-skill/docs/build.html (9/9 showcase, 0 errors, 0 warnings)
- design: sdlc/iig3d-skill/docs/design.html (9/9 showcase, 0 errors, 0 warnings)
- plan: sdlc/iig3d-skill/docs/plan.html (9/9 showcase, 0 errors, 0 warnings)
