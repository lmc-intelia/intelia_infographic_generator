# iig3d: 3D corporate infographics for Claude Code

`iig3d` is a Claude Code skill that renders infographics in the glossy corporate 3D
family (stacked slabs, rimmed disc timelines, capsule hubs, glass layers, isometric
platforms and so on) with Google's Nano Banana Pro image model. One Python script does
every deterministic step: it routes a layout to a family member, picks reference images,
assembles the prompt, persists it, calls the Gemini API and saves the PNG. Claude only
writes a short YAML content spec and confirms the choices.

The skill lives in `skills/iig3d/`. Everything else in this repository is the development
environment (tests, pre-commit, sdlc stage records) and can be ignored by users.

## Contents

- [Requirements](#requirements)
- [Install](#install)
- [Credentials](#credentials)
- [Quick start](#quick-start)
- [The content spec](#the-content-spec)
- [Choosing a member and layout](#choosing-a-member-and-layout)
- [Reproducing one reference image](#reproducing-one-reference-image)
- [Brand colours from a CSS file](#brand-colours-from-a-css-file)
- [Icons from a named pack](#icons-from-a-named-pack)
- [Logo stamp](#logo-stamp)
- [Commands](#commands)
- [Adding your own reference images](#adding-your-own-reference-images)
- [Using the skill from Claude Code](#using-the-skill-from-claude-code)
- [Output files](#output-files)
- [Troubleshooting](#troubleshooting)
- [Development](#development)

## Requirements

- [`uv`](https://docs.astral.sh/uv/) on the PATH. The script carries its own dependency
  header (PEP 723), so `uv run` installs `google-genai`, `pillow` and `pyyaml` on first use.
  Python 3.10 or later.
- A Google Gemini API key with access to `gemini-3-pro-image`.
- Claude Code, if you want Claude to drive it. The script also works on its own.

## Install

Pick one.

**From this repository into Claude Code (any project):**

```bash
npx skills add lmc-intelia/intelia_infographic_generator --skill iig3d --agent claude-code --copy
```

`--copy` puts a real copy under `~/.claude/skills/iig3d`. Without it the installer keeps the
skill in `~/.agents/skills/` and symlinks it, and on macOS Claude Code does not load skills
through that symlink.

**From a checkout, as symlinks (keeps the skill in sync with the repo):**

```bash
git clone https://github.com/lmc-intelia/intelia_infographic_generator.git
cd intelia_infographic_generator
just install-local      # ~/.claude/skills/iig3d and .claude/skills/iig3d -> skills/iig3d
```

`just uninstall-local` removes only those two symlinks. On macOS use `just install-copy`
instead: it copies `skills/iig3d` into `~/.claude/skills/iig3d` (rerun after pulling changes)
because Claude Code on macOS does not load a skill through a symlink there.

**Standalone, no Claude Code:** copy `skills/iig3d/` anywhere and call
`uv run <that dir>/scripts/iig3d.py ...`.

## Credentials

Put your key in a `.env` file in the directory you run the command from:

```
GEMINI_API_KEY=AIza...
```

The script reads `./.env` in the current directory, then `GEMINI_API_KEY` or
`GOOGLE_API_KEY` from the environment, then `--api-key`. It does not look in parent
directories. When nothing is found it exits 1 with:

```
no API key: expected GEMINI_API_KEY in /your/dir/.env or the environment
```

The key value is never written to stdout, prompt files, YAML or logs. Keep `.env` out of git
(this repository's `.gitignore` already lists it).

## Quick start

```bash
cp skills/iig3d/templates/spec.example.yaml spec.yaml   # edit title and items
uv run skills/iig3d/scripts/iig3d.py render --spec spec.yaml --out-dir infographic/my-topic
```

Output:

```json
{"status": "ok", "path": ".../infographic/my-topic/infographic.png", "bytes": 3013940,
 "model": "gemini-3-pro-image", "aspect_ratio": "16:9", "quality": "2K", "image_size": "2K", "refs": 1,
 "attempts": 1, "elapsed_seconds": 31.0,
 "prompt_file": ".../infographic/my-topic/prompts/01-infographic-my-title.md",
 "warnings": [], "member": "3d-glass-layer", "layout": "hierarchical-layers", ...}
```

A render takes about 30 seconds at 2K. Add `--dry-run` to write the prompt file and skip the
API call. Pick the quality with `quality:` in the spec or `--quality` on the command line. Every
level uses `gemini-3-pro-image`, so the rendering style never changes between levels; the level
is the `image_size` value the model accepts (it has no others):

| Level | `image_size` | Output | Use |
|-------|--------------|--------|-----|
| `1K` | `1K` | 1024 px long edge | drafts, slides, chat |
| `2K` | `2K` | 2048 px long edge | documents, web (default) |
| `4K` | `4K` | 4096 px long edge | print, posters |

`--model ID` or `IIG3D_MODEL` overrides the model. Claude asks for the level once per session
("Render quality?") unless the request names one. `--resolution` is still accepted as an alias of
`--quality`.

## The content spec

One YAML file per infographic. Only `title` and `items` are required.

```yaml
title: OPENWIKI REFRESH PIPELINE          # on-image title, verbatim
subtitle: Five steps from commit to published wiki
language: en                              # language of every label (default en)
layout: linear-progression                # a general layout or a 3d-* device name (a refs/ folder)
style: industrial-3d                      # industrial-3d routes by layout; a 3d-* member; or a ref of the layout member
aspect: landscape                         # landscape | portrait | square | W:H such as 4:3
quality: 2K                               # 1K | 2K | 4K, see Quick start
palette_css: ./brand.css                  # optional, see Brand colours
palette_vars: [--brand-primary, --brand-secondary]   # optional, restricts and orders the colours
icon_pack: lucide                         # optional, see Icons from a named pack
items:                                    # one per step, tier, capsule, pill, cell, plate or cylinder
  - label: COMMIT                         # required; rendered as "01 COMMIT"
    detail: Developer pushes to main      # one line under the label
    value: "73%"                          # optional stat shown with the item
    icon: git-branch                      # optional; a hint, or a glyph name when icon_pack is set
stats:                                    # optional headline numbers
  - {value: "12x", caption: faster refresh}
notes: keep the world map faint           # optional design instructions
pin: 3d-capsule-hub/06                    # optional, same as layout: 3d-capsule-hub + style: 06
refs: [./my-brand-reference.jpg]          # optional extra reference images (max 6 total)
```

Rules the script enforces: unknown keys and missing `title`, `items` or `label` fail with the
key named; relative `palette_css` and `refs` paths resolve against the spec file's directory;
anything that looks like an API key inside the text is replaced with `[redacted]`.

Warnings (not errors) are returned when the on-image text exceeds about 120 words for
landscape or 160 for portrait, when the item count is outside the member's range (the
warning names an alternate member), and when a custom aspect ratio is snapped to the nearest
supported one. `--strict` turns warnings into exit 1.

## Choosing a member and layout

Fifteen members share one rendering language and differ in the structural device:

| Style | Device | Items | Best for |
|-------|--------|-------|----------|
| `3d-slab-stack` | Stacked extruded slabs, staircase, folded ribbons | 3 to 7 | tiers, ranked lists, funnels |
| `3d-arrow-ribbon` | Fat chevron arrows, arrow bars, angled banners, folded ribbons | 4 to 8 | pipelines, journeys, ranked options |
| `3d-disc-timeline` | Rimmed discs on a track, chain or S-curve | 4 to 8 | timelines, procedures |
| `3d-paper-tile` | Embossed tiles, hexagons, tabs, tile-capped charts | 6 to 16 | dashboards, grids |
| `3d-gradient-pedestal` | Isometric gradient pedestals with 3D numerals | 3 to 5 | short summaries, comparisons |
| `3d-capsule-hub` | Central disc with pill capsules and connectors | 4 to 8 | capability maps, cycles |
| `3d-isometric-light` | Isometric platforms, roads and blocks on white | 4 to 6 | site and system maps |
| `3d-isometric-dark` | Isometric ribbon with 3D charts on navy | 3 to 5 | data stories, KPI pages |
| `3d-target-callout` | Tilted bullseye with beams to numbered pills | 3 to 6 | goals, OKRs |
| `3d-hex-cluster` | Honeycomb of outlined hexagons around a hub | 6 to 10 | inventories, taxonomies |
| `3d-cylinder-column` | Stepped glossy cylinders with bent arrows | 3 to 6 | ranked steps, bar charts |
| `3d-glass-layer` | Exploded stack of translucent plates | 3 to 7 | architecture layers |
| `3d-triangle-plate` | Facet pyramid of four prisms, or one triangle with corner nodes | 3 to 4 | pillars, triads, trade-offs |
| `3d-soft-emboss` | Neumorphic grey jigsaw ring, segment ring, overlapping circles or chevron row | 3 to 6 | small frameworks, cycles, overlaps, short sequences |
| `3d-winding-road` | Asphalt road ribbon with numbered map pins | 4 to 8 | roadmaps, journeys, phased programmes |

Three ways to pick, from most to least specific:

1. Folder and image: `layout: 3d-capsule-hub` names a folder under `skills/iig3d/refs/`,
   `style: "06"` names an image in it. The render reproduces that image with your content.
   See [Reproducing one reference image](#reproducing-one-reference-image).
2. Member only: `style: 3d-target-callout` (or `layout: 3d-target-callout`). The script picks
   two or three of that member's images by its pairings.
3. General layout: `style: industrial-3d` (or omit it) with one of the 21 general layouts
   (`linear-progression`, `hub-spoke`, `hierarchical-layers`, `dashboard`, `bento-grid`,
   `funnel`, `isometric-map`, ...). The routing table in `catalogue/family.yaml` maps each to a
   primary member and alternates; `route --layout L` shows them. These names are intent
   vocabulary kept from the 2D infographic family; they are aliases for a member choice, and
   `bento-grid` is the default when both keys are omitted.

`list` prints every member and layout. The generated catalogue at
`skills/iig3d/docs/CATALOGUE.md` and the per-member pages under `skills/iig3d/docs/members/`
describe each device, its reference images, palette and composition rules.

## Reproducing one reference image

Every member ships a folder of reference JPEGs under `skills/iig3d/refs/<member>/`. By default
the script picks two or three of them by layout pairing and passes them as style guidance.
To have the render reproduce one specific image's composition with your content, name the
folder as the layout and the image as the style:

```yaml
layout: 3d-capsule-hub                    # the folder under refs/
style: "06"                               # the ref id, or ref-06-capsule-hierarchy.jpg, or its stem
```

`--layout 3d-capsule-hub --style 06` on `prompt`, `render` or `route` does the same. The
one-key form `pin: 3d-capsule-hub/06` (also `--pin`) is equivalent and works with any layout;
it also accepts `refs/3d-capsule-hub/ref-06-capsule-hierarchy.jpg` as you see the path.
List a member's refs with `refs --member 3d-capsule-hub`; each entry carries `pin`, `file`,
`shows`, `variant`, `item_count` and `flags`. The per-member pages under `docs/members/` show
the same table.

What a pin changes:

- The pinned member becomes the style member, and the layout defaults to the member's own
  device. A `pin:` whose member differs from an explicit `3d-*` style is an error.
- The pinned image is reference image 1. Up to two pairing refs follow as style support,
  never a second watermarked one. Your own `refs:` still append, six images in total at most.
- The prompt gains a "Reference Composition" section: what the image shows, its variant and
  item count, and the instruction to reproduce the structure and replace only the text. The
  prompt file's frontmatter marks the first reference `usage: replicate` and records the pin.
- Warnings when the pinned image is `low-res` or `watermark`, and when your item count differs
  from the image's `item_count`.

Pins resolve against the catalogue YAML only; a path that is not a registered ref is an error
listing the valid ids.

## Brand colours from a CSS file

Point the skill at a stylesheet and its colours replace the family item colours. Backdrop,
neutrals, shadows and typography stay as they are.

```bash
uv run skills/iig3d/scripts/iig3d.py palette --css src/styles/brand.css          # preview
uv run skills/iig3d/scripts/iig3d.py render --spec spec.yaml --out-dir out --palette-css src/styles/brand.css
```

Extraction takes custom properties (`--name: value`) in declaration order, then bare
`#hex`, `rgb()` and `hsl()` literals; greys, near-white and near-black are dropped; duplicates
are dropped; at most 8 colours are kept. `--palette-vars a,b,c` (or `palette_vars` in the
spec) restricts and orders the extraction to named properties. Fewer than 3 usable colours is
an error. The prompt gains a "Project palette override" paragraph and the prompt file's
frontmatter records the source and colours.

## Icons from a named pack

Without a pack, `icon:` on an item is a free-text hint and the model draws its own idea of it.
Name a pack and the script builds an icon sheet the model copies from:

```yaml
icon_pack: lucide                         # any Iconify pack: lucide, tabler, ph, mdi, fa6-solid, ...
items:
  - {label: PLAN, icon: compass}          # lucide:compass
  - {label: SHIP, icon: tabler:rocket}    # a prefix overrides the pack for one item
  - {label: TALK, icon: a speech bubble}  # not a slug: stays a free-text hint
```

`--icon-pack lucide` on `prompt` or `render` sets the default pack. Glyphs are cached under
`skills/iig3d/icons/<pack>/<name>.svg` and fetched from the Iconify API on a miss; `--no-icon-fetch`
(or `IIG3D_ICON_FETCH=0`) uses the cache only. Browse names at https://icon-sets.iconify.design.

Items without an `icon:` still get one when a pack is set: the script maps words in the label,
then the detail, through a built-in business vocabulary (plan to compass, launch to rocket, data
to database, and so on), then searches Iconify names for each word. The prompt frontmatter
records how each glyph was chosen (`via: spec`, `synonym:launch`, `search:umbrella`). A named
icon that does not exist falls back the same way and fails only when nothing fits.
`icons --pack lucide --label "GOVERN" --detail "policy and control"` shows the pick without
rendering; `--query shield` lists matching names. Claude, following SKILL.md, names an icon per
item from the source text first and uses these suggestions to fill or check.

The sheet is one white PNG with each glyph in black under its item number, saved as
`icon-sheet.png` in the output directory and passed after the catalogue refs (before your own
`refs:`, still six images at most). The prompt gains an "Icon Set" section telling the model to
copy each numbered glyph's line work onto its item and recolour it; the frontmatter marks the
sheet `usage: icons` and lists the item-to-icon map. Expect faithful shapes and stroke weight,
not pixel-exact glyphs.

## Logo stamp

Every render gets the Intelia mark (`skills/iig3d/assets/trimmed_intellia_logo.png`) composited
into the bottom-left corner after the model returns: 5 px from the left and bottom edges, scaled
to 6 percent of the image height, alpha-blended over a soft drop shadow (35 percent black,
blurred, offset down and right), so it is the same at 1K, 2K and 4K. The result JSON reports
the `logo` path used.

- `--logo PATH` stamps another PNG (transparent background recommended); `IIG3D_LOGO=PATH` sets
  a default for the shell.
- `--no-logo`, `--logo none` or `IIG3D_LOGO=none` render without it.
- Always use `--no-logo` when a render is going back into the catalogue as a reference image,
  otherwise the model learns to draw the mark.

## Commands

Every command prints one JSON line on stdout; diagnostics go to stderr.

| Command | Purpose |
|---------|---------|
| `list` | members (device, item range, aspect default, refs), the 21 general layouts, the quality levels |
| `refs --member M [--layout L] [--pin P] [--ref IMG]` | the 2 to 3 reference images a render would pass, plus every ref of the member with its pin token |
| `route --layout L [--style S]` | which member renders this layout; alternates; `pin` when `--style` names a ref of the `--layout` member |
| `icons [--pack P] [--query WORD] [--label TEXT] [--detail TEXT]` | glyph names matching a word in a pack; the glyph the script would pick for an item's text |
| `palette --css PATH [--vars a,b]` | colours extracted from a CSS file |
| `prompt --spec F --out-dir D [...]` | write `prompts/NN-infographic-<slug>.md`; no API call |
| `render --spec F --out-dir D [--dry-run] [--quality 1K\|2K\|4K] [--logo PATH\|none] [--no-logo] [--aspect A] [--style S] [--layout L] [--palette-css P] [--pin M/ID] [--icon-pack P] [--no-icon-fetch] [--ref IMG] [--no-style-refs] [--strict] [--model ID] [--retries N] [--api-key K]` | prompt file, then Gemini, then `infographic.png` |
| `add --image IMG --meta meta.yaml` | register an image as a reference (below) |
| `docs` | regenerate `docs/` markdown from the YAML catalogue |
| `check [--allow-watermark]` | validate catalogue, refs and docs; exit 1 with every violation |

Every command that touches the catalogue accepts `--skill-root DIR` (default: the script's
own skill directory).

Exit codes: 0 ok, 1 usage or credentials (`{"status":"error","error":...}`), 2 API or
output failure (same shape, `attempts` and `elapsed_seconds` filled in).

## Adding your own reference images

Any image can become a first-class reference with the same build-out as the shipped ones.

1. Look at the image and decide whether it belongs to an existing member or founds a new one.
2. Write a meta file (start from `skills/iig3d/templates/meta.example.yaml`):

   ```yaml
   member: 3d-capsule-hub                 # or new_member: {name: 3d-orbit-ring, ...full member block...}
   shows: "Three-level capsule hierarchy: hub disc, eight capsules, sub-capsules per capsule"
   flags: [clean]                         # clean | watermark | low-res
   pairings: [hub-spoke, tree-branching]  # layouts this reference suits
   variant: Capsule hierarchy             # optional; a name from the member's layout.variants
   item_count: 8                          # optional; items the image holds
   slug: capsule-hierarchy                # optional file name stem
   ```

3. Run it:

   ```bash
   uv run skills/iig3d/scripts/iig3d.py add --image CAPSULE-hierarchy.png --meta meta.yaml
   ```

The script resizes to at most 1600 px as an RGB JPEG at `refs/<member>/ref-NN-<slug>.jpg`,
appends the entry to the member YAML with `source: {path, added, user_added: true}`, extends
the pairings, regenerates the docs and runs `check`. The result's `pin` (here
`3d-capsule-hub/07`) is what a spec's `pin:` takes to reproduce the new image straight away;
`variant` and `item_count` feed that prompt's Reference Composition section. Vendored entries
are never edited by `add`, only extended. A new member needs its full block in `new_member` (copy a file from
`skills/iig3d/catalogue/members/` and drop `refs`, `pairings`, `source`); `routing:` lists the
general layouts whose alternates gain the member. Member names must match
`3d-[a-z0-9-]+`.

A `watermark` flag is reported as a violation until you pass `--allow-watermark` to `check`;
the selector never passes two watermarked references together, and a pinned watermarked ref
renders with a warning. To clean one up, render it with itself pinned, delete the JPEG and
`add` the render with `file:` set to the old name; the entry records `regenerated: true` and
`derived_from` (the original image). The shipped user-added refs were cleaned this way. Rights for images you add stay
with you.

## Using the skill from Claude Code

With the skill installed, ask for a "3d infographic", "industrial 3d", or `/iig3d`. Claude
follows `skills/iig3d/SKILL.md`:

1. Once per session it asks "Load a CSS file for brand colours?" (skip by naming a CSS file
   in the request, setting `palette_css`, or saying `--no-confirm`) and "Render quality?"
   (1K, 2K or 4K; skip by naming a level or setting `quality`).
2. It writes `spec.yaml` from your source, verbatim labels, secrets stripped.
3. It confirms member, layout, aspect and language once, then runs `render`.
4. It reports the PNG path, the prompt file and any warnings. It never patches rendered text
   with code and never substitutes SVG or HTML for the image; a bad render is re-rendered from
   a corrected spec.

## Output files

```
infographic/<slug>/
  prompts/01-infographic-<title-slug>.md   # frontmatter: layout, style, style_member, aspect,
                                           #   language, references[, pinned][, palette]; body: the full prompt
  infographic.png                          # RGB PNG at the requested resolution, logo bottom-left
  infographic-backup-YYYYMMDD-HHMMSS.png   # previous render, when you render again
```

Prompt numbers only increase (`02-`, `03-`, ...); nothing is overwritten. The prompt file is
the reproducibility record.

## Troubleshooting

| Symptom | Cause and fix |
|---------|---------------|
| `no API key: expected GEMINI_API_KEY in <dir>/.env or the environment` | Put the key in `./.env` of the directory you run from, or export it. No parent-directory lookup. |
| `unknown layout 'x'; valid: ...` | Use one of the listed general layouts or a `3d-*` member name. |
| `unknown key(s) ...` in the spec | Only the keys shown in [The content spec](#the-content-spec) are allowed. |
| `status: error`, `no image part in response` | Content refused or truncated. Simplify the spec, remove named people or brands, rerun. |
| `429` in the error | Quota. The script already retried once; wait and rerun. |
| Garbled text in the PNG | Fix the spec (shorter labels, fewer items) and render again; the old PNG is kept as a backup. |
| `reference image missing: ...` | A catalogue ref file is absent; run `check` and restore the file. |
| `unknown ref '07' for 3d-capsule-hub; valid: ...` | The style or pin names no registered ref; pick one from `refs --member M` or `add` the image first. |
| `unknown style '06'; valid: industrial-3d, a 3d-* member, or a ref of the member named by layout` | A ref id as `style:` needs `layout:` set to that ref's `3d-*` folder. |
| `style 3d-slab-stack conflicts with pinned ref member 3d-capsule-hub` | Drop `style:` or set it to the pinned member. |
| `not valid YAML: ...` | A colon inside an unquoted value is the usual cause; quote the string. |

## Development

```bash
uv sync                 # runtime deps plus pytest, ruff, bandit, pre-commit
just hooks              # install pre-commit hooks (ruff, ruff-format, bandit, gitleaks, uv-lock)
just test               # uv run pytest -q
just lint               # uv run pre-commit run --all-files
just iig3d-check        # validate the catalogue, refs and generated docs
IIG3D_LIVE=1 uv run pytest -q tests/test_render.py   # one live smoke render (costs one API call)
```

Layout of the skill:

```
skills/iig3d/
  SKILL.md                    # what Claude reads
  scripts/iig3d.py            # the whole CLI, one file, PEP 723 header
  catalogue/family.yaml       # palette, typography, negative list, routing table, ref rules
  catalogue/members/3d-*.yaml # one member each: device, layout, style, prompt fragment, refs, pairings
  catalogue/schema.yaml       # walked by validate_member
  refs/<member>/ref-NN-*.jpg  # reference images, all clean renders or clean originals
  templates/                  # base-prompt.md, spec.example.yaml, meta.example.yaml
  assets/                     # trimmed_intellia_logo.png, stamped on every render
  icons/<pack>/<name>.svg     # icon cache for icon sheets; a few Lucide glyphs vendored for tests
  docs/                       # generated by `iig3d.py docs`; do not edit by hand
```

The catalogue is the source of truth; markdown under `docs/` is generated and `check` fails
when it is stale. Adding a member is one YAML file plus one refs folder; no Python changes.

The repository is developed with the `sdlc` Claude Code plugin; stage records live under
`sdlc/`. `evals/` holds a headless eval that drives the skill from a brief to a prompt file.
