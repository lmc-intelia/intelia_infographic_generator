---
type: Feature
title: iig3d skill
description: The 3D corporate infographic capability built on 2026-09-15 to 2026-09-17 lives inside the
resource: sdlc/iig3d-skill
tags: [feature, accepted]
status: stable
generated: { by: sdlc/0.3.5, at: "2026-09-17T00:38:17Z" }
stale_after: "2026-10-01T00:38:17Z"
source_commit: HEAD
sources:
  - { id: intent, resource: sdlc/iig3d-skill/intent.md, last_modified: "2026-09-17T00:38:17Z", digest: a2d1906944e50ff8 }
verified:
  - { by: "human:linus-mcmanamey", at: "2026-09-17T00:38:17Z" }
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
- spec.md not written yet

# Files
- plan.md not written yet

# Review
- no review yet

# Status
- intent.md: accepted
- spec.md: missing
- plan.md: missing
- test-report: missing or failed
- deployed: nowhere

# Documents
- plan: sdlc/iig3d-skill/docs/plan.html (9/9 showcase, 0 errors, 0 warnings)
