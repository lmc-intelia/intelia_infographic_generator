# Intent: iig3d skill
Author: Linus McManamey. Status: accepted. Risk: low.

## Problem
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

## Proposed outcome
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

## Affected users and systems
- Linus McManamey: author, sole operator, product owner for this intent.
- This repository: gains `skills/iig3d/` at the repository root as the canonical, shareable
  copy (SKILL.md, `scripts/iig3d.py`, vendored `refs/<member>/ref-NN-*.jpg`, catalogue data).
  The `skills/<name>/SKILL.md` layout is the one `npx skills add <repo>` already installs
  from (see `~/.agents/.skill-lock.json`), so other people install it straight from the
  Intelia repo. Tests live under `tests/` at the repository root per `.sdlc.toml`.
- Local install: `~/.claude/skills/iig3d` is a symlink to the repository copy, the same
  pattern the baoyu skills use today (`~/.claude/skills/baoyu-* -> ../../.agents/skills/...`),
  so one checkout serves every project on this machine and edits never diverge. A `just`
  recipe (or short install script) creates the link and an equivalent `.claude/skills/iig3d`
  link inside this repository for project-scoped discovery.
- Claude Code runtime: discovers the skill from the user or project skills directory;
  invokes it on "3d infographic", "industrial 3d", "iig3d" or a `/iig3d` command. For `add`
  it reads the supplied image with its image-reading tool to categorise and describe it.
- Anyone who installs the shared skill: needs `uv`, a `.env` with `GEMINI_API_KEY` in the
  directory they run from, and nothing else.
- Google Gemini API: model `gemini-3-pro-image` via the `google-genai` Python SDK; credential
  `GEMINI_API_KEY` (or `GOOGLE_API_KEY`) from `./.env` in the calling directory, else the
  process environment.
- `uv`: runs the script with inline dependencies (`google-genai`, `pillow`, `pyyaml`).
- Source material read once at build time and then untouched: `~/.agents/skills/baoyu-infographic`
  (`references/styles/3d-*.md`, `references/styles/3d-family.md`,
  `references/layouts/3d-*.md`, `references/base-prompt.md`, `references/nano-banana-pro.md`,
  `scripts/generate_image.py`, 36 reference JPEGs, two `sample-prompt.md` files) and the
  preference file `~/.baoyu-skills/baoyu-infographic/EXTEND.md`.
- Not touched: the five baoyu skills and their symlinks under `~/.claude/skills`, the
  `nano-banana-pro` plugin, `~/.agents/.skill-lock.json`.

## Constraints
- Policy carried over from the source skill: never substitute SVG, HTML or canvas for raster
  output; never paint over rendered text with code (regenerate from a corrected prompt to a
  new path instead); persist the full prompt before calling the API; never copy text,
  numbers or icons from a reference image; strip credentials from all outputs.
- Data: reference JPEGs, vendored or user-added, stay at or under 1600 px on the long edge
  and are JPEG; about 5 MB of vendored refs is committed to the repository. Reference images
  that carry stock-library watermarks keep their flag so the selector never pairs two of
  them. User-added images are the user's responsibility for rights; the skill records the
  source path and date in the catalogue entry.
- Auth: only `GEMINI_API_KEY` / `GOOGLE_API_KEY`, read from `./.env` in the calling directory
  or the environment; the script must never write the key into a prompt, log, catalogue or
  result file, and `.env` is git-ignored. No other image provider.
- Extensibility: the catalogue, member markdown and reference folders are the only things
  `add` touches; the twelve vendored members are never modified by `add`, only extended.
- Scope discipline: 3D family only. Out of scope are the 21 general layouts and 23 general
  styles, the EXTEND.md first-time interview, keyword shortcuts, `baoyu-slide-deck`,
  `baoyu-image-gen`, `baoyu-diagram`, `baoyu-format-markdown`, the plugin fallback runner,
  and any change to the baoyu skills themselves.
- Style: prose in SKILL.md and in the catalogue limited to what a model needs to make a
  judgement; every deterministic rule is code with a test. Python 3.10 or later; no
  project-level virtual environment required beyond `uv`.
- Budget: each real render costs one Gemini Pro image call at 2K by default; the acceptance
  render pass is 12 calls.
- Repository conventions: `.sdlc.toml` test command is `pytest -q` with TDD required; tests
  live under `tests/`.

## Open questions
None.

Decided on 2026-09-17 with the product owner:
- The skill is shared from the Intelia repository at `skills/iig3d/` and installed locally by
  symlink; the 36 reference JPEGs are vendored so the shared copy is self-contained.
- SKILL.md keeps a one-line confirmation gate (member, aspect, language) that `--no-confirm`
  skips.
- The content spec Claude writes before calling the script is YAML (`pyyaml` inline
  dependency).
