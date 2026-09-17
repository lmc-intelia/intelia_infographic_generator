# Spec: iig3d skill
From: intent.md (2026-09-17). Status: accepted. Risk: low.

## Requirements
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
19. **Repository hygiene** (I-constraints). `.gitignore` lists `.env`, `.venv/`, `__pycache__/` and `infographic/` (render output; the user copies what they keep). Root `pyproject.toml` declares the same runtime deps plus `pytest` for the test suite; `.sdlc.toml` test command becomes `uv run pytest -q`.

20. **Brand palette from CSS** (product owner request 2026-09-17, extends the intent's "project palette override replaces the item colours only" rule). `--palette-css PATH` on `prompt` and `render`, or `palette_css: PATH` in the content spec, reads a CSS file from the user's repository and derives the item colours. Extraction: custom properties in declaration order (`--name: <colour>`) first, then any other `#hex`, `rgb()`, `hsl()` literal; values normalised to `#RRGGBB`; duplicates dropped; neutrals dropped (HSL saturation under 15 percent, lightness over 92 or under 10 percent); at most 8 kept. `--palette-vars a,b,c` restricts and orders extraction to named custom properties. Precedence: `--palette-css` flag over `palette_css` in the spec; `--palette-vars` over `palette_vars`. A relative `palette_css` resolves against the spec file's directory; a relative `--palette-css` against the current working directory. A missing file exits 1 naming the resolved path. Fewer than 3 usable colours exits 1 naming the file. The prompt's Style Guidelines gain a trailing paragraph: `Project palette override: cycle item colours in this order: <name> #RRGGBB, ...; never repeat a colour on adjacent items; keep the family backdrop, neutrals, shadows and typography unchanged.` The prompt frontmatter records `palette: {source: <path>, colours: [{name, hex}]}`. Backdrop, neutral and shadow values are never replaced. `palette --css PATH [--vars ...]` prints the extraction as JSON for preview.

21. **Clean replacement of watermarked refs** (Concern 1 resolution, 2026-09-17). The 9 source refs flagged `watermark` (`3d-disc-timeline` 01, 02, 04; `3d-capsule-hub` 01, 02; `3d-isometric-dark` 02, 03; `3d-isometric-light` 02; `3d-target-callout` 02; `3d-cylinder-column` 01; `3d-glass-layer` 01) are not vendored. Before the skill is declared built, each is replaced by a clean image produced by `render` from `templates/spec.example.yaml` content with the original as the only `--ref`, at 2K and the member's `aspect_default`, then registered through `add --meta` with `flags: [clean]`, `shows` written by Claude from the render, and the same pairings the original held. The originals are deleted from the working tree before the first commit that adds `refs/`. `check` fails if any vendored ref carries the `watermark` flag (`--allow-watermark` relaxes this for user-added refs only, recorded per ref as `source.user_added: true`). Cost: 11 Gemini Pro image calls. Two of the eleven (`3d-disc-timeline` 02, `3d-isometric-light` 02) are also `low-res`; their regenerations lift that flag too.

## Design
### Directory layout (new; nothing existing changes except `.sdlc.toml`, `justfile`)
```
skills/iig3d/
  SKILL.md                      # ≤80 lines: trigger, spec format, command table, two rules
  scripts/iig3d.py              # single CLI, PEP 723 header, stdlib argparse
  catalogue/family.yaml         # palette, typography, negative_list, aspect_map, text_budget, routing
  catalogue/members/3d-*.yaml   # 12 member files (R3)
  catalogue/schema.yaml         # member/meta schema used by check and add (hand-written, minimal)
  refs/<member>/ref-NN-*.jpg    # 30 files: 19 clean originals vendored from the baoyu fork, 11 clean regenerations replacing the watermarked originals (R21); industrial-3d's 6 refs are duplicates of member refs and are not copied
  templates/base-prompt.md      # slots per R8
  templates/spec.example.yaml   # content spec example
  docs/CATALOGUE.md, docs/members/*.md   # generated by `docs` (R14)
tests/                          # repo root, pytest
pyproject.toml, .gitignore, justfile (recipes added), .sdlc.toml (test command)
```

### Modules inside `scripts/iig3d.py` (one file, sectioned)
| Section | Responsibility | Interface |
|---------|----------------|-----------|
| `catalogue` | load `family.yaml` + members, schema validate | `load(root) -> Catalogue`, `Catalogue.member(name)`, `.layouts`, `.routing` |
| `routing` | R4 | `route(cat, layout, style) -> Route(member, alternates, reason)` |
| `refs` | R5 | `select_refs(cat, member, layout, user_refs) -> list[Path]` |
| `spec` | R6 | `load_spec(path) -> Spec` (dataclass), key validation |
| `aspect` | R7 | `snap(aspect, default) -> (ratio, snapped_from)` |
| `prompt` | R8, R9, R18 | `assemble(cat, spec, route, ratio) -> (text, frontmatter, warnings)`, `write_prompt(out_dir, ...) -> Path` |
| `palette` | R20 | `extract_palette(css_path, vars) -> list[Colour]`, `palette_paragraph(colours) -> str`; regex + HSL maths, no CSS parser dependency |
| `creds` | R10 | `api_key(cwd, explicit) -> (key, source)` |
| `render` | R11 | `render(prompt_path, refs, ratio, resolution, model, out_png, retries, dry_run) -> dict` |
| `add` | R13 | `add_ref(cat_root, image, meta) -> dict` |
| `docs` | R14 | `render_docs(cat_root) -> list[Path]` |
| `check` | R15 | `check(cat_root) -> list[str]` |
| `cli` | argparse subcommands `list route refs prompt render add docs check palette` | every subcommand prints one JSON object on stdout; diagnostics on stderr |

### Data flow (render path)
1. Claude reads the user's source, writes `spec.yaml` (R6) in the working directory or `infographic/<slug>/`.
2. Claude states member, aspect, language; user confirms (R12).
3. `uv run <skill>/scripts/iig3d.py render --spec spec.yaml --out-dir infographic/<slug> [--palette-css brand.css]`:
   `load_spec` → `route` (style/layout from spec or flags) → `snap` → `select_refs` → `extract_palette` (when a CSS path is given) → `assemble` → `write_prompt` → `api_key` → `render` → JSON line.
4. Claude reports path, warnings, and the prompt file.

### Data flow (add path)
1. User supplies an image. Claude views it, decides member or new member, writes `meta.yaml` (`shows`, `flags`, `pairings`, and for a new member the full block).
2. `iig3d.py add --image X --meta meta.yaml` → normalise JPEG → write YAML → `render_docs` → `check` → JSON.
3. Claude reviews `docs/members/<member>.md` and reports.

### Key data shapes
`family.yaml`
```yaml
palette: {items: [teal: "#1FB5C8", orange: "#F5851F", magenta: "#E4327A", royal_blue: "#2456C4", lime: "#8CC63F", purple: "#7B3FA0", red: "#E2312A", yellow: "#F7C11B"], light: ["#F4F6F9", "#E3E7ED"], blue_grey: ["#C9D3DC", "#E6ECF1"], dark: ["#1C2A4A", "#101A33"], neutrals: {...}}
typography: [ ...bullets... ]
negative_list: "No hand-drawn lines, no paper texture, no cartoon characters, no photographic realism, no watermarks, no placeholder or lorem ipsum text. Clean premium business-template 3D."
aspect_map: {landscape: "16:9", portrait: "9:16", square: "1:1"}
supported_ratios: ["1:1","3:2","2:3","3:4","4:3","4:5","5:4","9:16","16:9","21:9"]
text_budget: {landscape: 120, portrait: 160}
routing: {linear-progression: {primary: 3d-disc-timeline, alternates: [3d-arrow-ribbon, 3d-slab-stack, 3d-gradient-pedestal, 3d-cylinder-column]}, ...21 rows}
```
`members/3d-disc-timeline.yaml` (shape)
```yaml
name: 3d-disc-timeline
device: Rimmed bevelled discs on a track, ribbon or S-curve
backdrop: Light studio, ghosted world map
items: {min: 4, max: 8}
aspect_default: landscape
layout: {structure: [...], variants: [{name, focus, emphasis}], visual_elements: [...], text_placement: [...]}
style: {palette: [...], visual_elements: [...], typography: [...], composition: [...]}
prompt_fragment: |
  Render as a polished corporate 3D infographic where each item is ... Clean premium business-template 3D.
best_for: [...]
refs:
  - {id: "01", file: ref-01-rimmed-disc-timeline.jpg, shows: "...", flags: [watermark]}
  - {id: "02", file: ref-02-s-curve-ribbon-discs.jpg, shows: "...", flags: [watermark, low-res]}
  - {id: "03", file: ref-03-disc-chain-track.jpg, shows: "...", flags: [clean]}
  - {id: "04", file: ref-04-serpentine-ribbon.jpg, shows: "...", flags: [watermark]}
pairings: {linear-progression: ["03","01"], winding-roadmap: ["03","04"], circular-flow: ["03","04"], bridge: ["01","03"]}
alternates: [3d-arrow-ribbon, 3d-isometric-light]
source: {origin: "baoyu-infographic 2.1.0-lmc references/styles/3d-disc-timeline.md", added: "2026-09-17"}
```
Palette extraction (R20) is pure: `Colour(name, hex)`, `name` = custom property without the leading dashes or `colour-N` for bare literals. CSS is read as text; `@import` and `url()` are ignored. Render JSON (R11) and `add` JSON (`{status, member, ref_file, yaml, docs[], check: []}`) are the only stdout contracts Claude parses.

### Interfaces at the edges
- Gemini: `genai.Client(api_key).models.generate_content(model, contents=[*PIL refs, ref_note, prompt], config=GenerateContentConfig(response_modalities=["TEXT","IMAGE"], image_config=ImageConfig(image_size, aspect_ratio)))`; first `inline_data` part saved as PNG. Logic ported from the baoyu bundled runner with walk-up removed.
- Filesystem: prompt dir `prompts/`, output PNG, backups; catalogue and refs inside the skill dir (writable for `add`).
- Claude Code: SKILL.md only; commands are absolute `uv run` invocations resolved from the SKILL.md directory.

### Existing code touched
None. Repo currently has no source. `.sdlc.toml` `[commands].test` changes to `uv run pytest -q`; `justfile` gains `install-local`, `uninstall-local`, `iig3d-check`, `test` recipes.

## Concerns
1. **Stock-watermarked reference images in a shareable repository.** 11 of the 30 source refs carry 123RF, Shutterstock, Alamy, iStock or pngtree watermarks (flagged in the catalogue). Sharing the repo distributes them. Owner: Linus McManamey (product owner). **Resolved 2026-09-17: replace before build ships.** The watermarked originals are never committed. R21 covers the replacement: each is regenerated as a clean render through the skill's own `render` (original passed as a style-only ref, generic fixture content), added through `add` with flag `clean`, and the original deleted. The `watermark` flag and its selector rule stay in the code for user-added images. The 19 clean source refs are committed as-is.
2. **Secret in the calling directory.** `./.env` holding `GEMINI_API_KEY` sits next to user output. Owner: Linus. Mitigation in scope: root `.gitignore` ignores `.env`; script never echoes the key; SKILL.md tells Claude never to read or print `.env`. Conflict: none, but the source runner's walk-up discovery is removed, so repos that relied on a parent `.env` must copy or symlink it (decided in intent).
3. **Live API calls in tests.** `pytest -q` must not spend Gemini quota. Owner: Linus. Resolution: `render` tests run `--dry-run` and a mocked `genai` client; one live smoke test is skipped unless `IIG3D_LIVE=1`. The 12-render acceptance pass is manual and costs 12 Pro image calls at 2K.
4. **User-added images and rights.** `add` accepts any image; the skill records source path and date only. Owner: the user adding the image. No technical control; documented in SKILL.md.
5. **Behaviour drift from baoyu fork.** Prompt assembly reproduces the fork's sections but the Layout Guidelines slot now uses the member's device layout block instead of the general layout file (general layouts are routing aliases only). Owner: Linus. Accepted trade-off for standalone scope; the prompt-assembly test asserts the Style Guidelines fragment and text-label block match the two `sample-prompt.md` files exactly.

## Open questions
Scope addition after intent acceptance: R20 (brand palette from a local CSS file) was requested by the product owner on 2026-09-17 during design. It fits the intent's existing "project palette override replaces the item colours only" constraint and needs no intent change; recorded here so the build plan traces it. None carried forward; all four intent questions were decided on 2026-09-17 (location `skills/iig3d` plus symlinks; confirm gate with `--no-confirm`; YAML spec; vendored refs). One design-level decision recorded here: the repository ships a root `pyproject.toml` so `uv run pytest -q` resolves dependencies, while the script keeps its PEP 723 header for standalone installs. Both list identical runtime dependencies; `check` in CI asserts they match.

## Proof
Tests under `tests/` (pytest, repo root), importing the script as a module through `tests/conftest.py`:
- `tests/test_catalogue.py`: R3, R15, R21 — every member YAML loads and validates; 12 members present; every ref file exists and is ≤1600 px JPEG; no vendored ref carries `watermark`; pairings and routing rows resolve; fragments end with the negative list; `check()` returns `[]` on the shipped catalogue and reports a seeded violation.
- `tests/test_routing.py`: R4 — parametrised over all 21 routing rows plus the 12 device names and explicit member styles; unknown names exit 1.
- `tests/test_refs.py`: R5 — clean-first order, watermark pair rejection, low-res-alone rejection, user refs appended, cap 6, fallback when no pairing for the layout.
- `tests/test_spec.py`: R6 — example spec loads; missing title, missing items, unknown key each exit 1 naming the key.
- `tests/test_aspect.py`: R7 — presets, exact ratios, snapping (`2.35:1`→`21:9`, `4:1`→`21:9`, `1:2`→`9:16`), member default.
- `tests/test_prompt.py`: R8, R9, R18 — assembled prompt for `linear-progression` + `3d-disc-timeline` and `industrial-3d` contains the exact Style Guidelines and Text labels blocks of the two fork `sample-prompt.md` fixtures (copied under `tests/fixtures/`); frontmatter fields; NN numbering never overwrites; word-budget and item-range warnings; `--strict` exit 1; API-key pattern stripped.
- `tests/test_palette.py`: R20 — fixture CSS with `:root` custom properties, `rgb()`/`hsl()` values, greys and near-white; extraction order, normalisation, neutral filter, dedupe, cap 8, `--palette-vars` ordering, fewer-than-3 exit 1, override paragraph present in the assembled prompt, backdrop hex values untouched, frontmatter `palette` block.
- `tests/test_creds.py`: R10 — `./.env` wins, env var second, `--api-key` third, no walk-up (parent `.env` ignored), exact error message, key absent from all outputs.
- `tests/test_render.py`: R11 — `--dry-run` JSON shape; mocked client saves PNG, backup rename on rerun, retry then exit 2 on failure, exit 2 when no image part; live smoke test gated by `IIG3D_LIVE=1`.
- `tests/test_add.py`: R13, R14 — add to existing member (resize 3000 px fixture to 1600, JPEG, YAML appended, docs regenerated, check clean); add new member from meta (YAML created, routing alternates added, docs created); rejects meta that edits an existing ref.
- `tests/test_docs.py`: R14 — generated markdown has the expected sections; stale docs fail `check`.
- `tests/test_cli.py`: R16, R11 — every subcommand prints exactly one JSON object on stdout; `list` counts 12 members and 21 layouts.
- `tests/test_install.py`: R17 — `just install-local` in a temp HOME creates both symlinks, refuses a real directory, uninstall removes only its links (skipped when `just` absent).
- `tests/test_skill_md.py`: R1, R12 — frontmatter name/description present, line count ≤80, every command in the table exists as a subcommand, the confirmation rule and the "Load a CSS file for brand colours?" start-of-skill question are both present.
Manual checks: `sdlc build` records red→green per step; acceptance render of all 12 members from `templates/spec.example.yaml` reviewed by the product owner (Concern 3).
