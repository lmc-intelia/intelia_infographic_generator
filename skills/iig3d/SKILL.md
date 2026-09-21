---
name: iig3d
version: 0.2.0
description: Render 3D corporate-family infographics (industrial 3d look, fifteen 3d-* members such as disc timelines, slab stacks, capsule hubs, glass layers, winding roads) with Google Nano Banana Pro through one Python CLI. Use when the user asks for a "3d infographic", "industrial 3d", "iig3d", a corporate 3D timeline, stack, hub, target or isometric map, or wants to add a reference image to the 3D catalogue.
---

# iig3d

`<skill>` = this file's directory. Run every command from the user's working directory with `uv run <skill>/scripts/iig3d.py ...`; each prints one JSON line. Full catalogue: `<skill>/docs/CATALOGUE.md`; one page per member under `<skill>/docs/members/`.

## Start of skill

1. Credentials: the user keeps `GEMINI_API_KEY=...` in `./.env` in the directory they call from (or exported). Never read or print `.env`; the script reports the source and exits 1 with the expected path when missing.
2. Once per session, before reading the source, ask: **"Load a CSS file for brand colours?"** (AskUserQuestion: a path, or "no, family palette"). On a path run `palette --css PATH`, show the colours, and put `palette_css:` in every spec this session. Skip the question when the request already names a CSS file, sets `palette_css`, or says `--no-confirm`.

3. Once per session, before the first render, ask: **"Render quality?"** (AskUserQuestion, one of four; each row is the exact Gemini model and `image_size` used):
   | Level | Gemini parameters | Use |
   |-------|-------------------|-----|
   | `draft` | `gemini-2.5-flash-image`, no `image_size` (about 1024 px) | fastest and cheapest; layout checks |
   | `1K` | `gemini-3-pro-image`, `image_size: "1K"` | slides, chat |
   | `2K` | `gemini-3-pro-image`, `image_size: "2K"` | documents, web (default) |
   | `4K` | `gemini-3-pro-image`, `image_size: "4K"` | print, posters |
   Put the answer in every spec this session as `quality:`. Skip the question when the request names a level, sets `quality`, or says `--no-confirm` (then use `2K`).

## Workflow

1. Read the user's source. Write `spec.yaml` (shape below; copy `<skill>/templates/spec.example.yaml`). Items are verbatim from the source; strip secrets.
2. Pick `style`: a `3d-*` member, or `industrial-3d` to route by `layout` (`route --layout L` shows the member and alternates; `list` shows all).
   To reproduce one catalogue JPEG with the user's content: `layout: <member>` (the `<skill>/refs/` folder name) and `style: <ref id or file>` from that folder (`refs --member M` lists them). Same thing as `pin: <member>/<ref>`. The image goes first to the model.
3. Icons: set `icon_pack: lucide` and give each item an `icon:` from its label and detail (a concrete Lucide name such as `rocket`, `users`, `database`). Unsure: `icons --pack lucide --query WORD` lists names, `--label TEXT` suggests one. Items left without `icon:` get the script's own suggestion from their text; none fits, no icon.
4. **Confirm member, layout, aspect and language once before render** (AskUserQuestion), unless the request says `--no-confirm` or equivalent. Then state the assumed choices.
5. `render --spec spec.yaml --out-dir infographic/<slug> [--no-confirm]`. Read the JSON: `status`, `path`, `prompt_file`, `warnings`. Report path and warnings. Do not read the PNG back unless asked.
6. Text wrong or garbled: fix the spec, render again (new `prompts/NN-*.md`, old PNG kept as `infographic-backup-*.png`). Never paint over rendered text with code. Never emit SVG, HTML or canvas as a substitute for the raster image.

```yaml
title: OPENWIKI REFRESH PIPELINE      # required
subtitle: Five steps from commit to published wiki
language: en
layout: linear-progression            # general layout or 3d-* device name (a refs/ folder)
style: industrial-3d                  # or a 3d-* member; or a ref id/file when layout names a member
aspect: landscape                     # landscape | portrait | square | W:H
quality: 2K                           # draft | 1K | 2K | 4K, from the session question
palette_css: ./brand.css              # optional; brand colours replace item colours only
items:                                # 3 to 10 depending on member; one per step/tier/cell
  - {label: COMMIT, detail: Developer pushes to main, icon: git-branch}
stats: [{value: "73%", caption: pages refreshed}]   # optional
notes: keep the world map faint       # optional design instructions
icon_pack: lucide                     # optional; item `icon: rocket` (or tabler:rocket) then comes from an icon sheet the model copies
pin: 3d-capsule-hub/06               # optional; same as layout: 3d-capsule-hub + style: 06
```

## Commands

| Command | Purpose |
|---------|---------|
| `iig3d.py list` | members (device, item range, aspect default, refs), the 21 general layouts with their primary member, the four quality levels |
| `iig3d.py route --layout L [--style S]` | which member renders this layout; alternates; `pin` when style names a ref |
| `iig3d.py refs --member M [--layout L] [--pin P]` | the 2 to 3 reference images the render will pass, plus every pin of the member |
| `iig3d.py icons [--pack P] [--query WORD] [--label TEXT]` | glyph names matching a word; the suggestion for an item's text |
| `iig3d.py palette --css PATH [--vars a,b]` | preview brand colours extracted from a CSS file |
| `iig3d.py prompt --spec F --out-dir D [...]` | write `prompts/NN-infographic-<slug>.md` without calling the API |
| `iig3d.py render --spec F --out-dir D [--dry-run] [--quality draft\|1K\|2K\|4K] [--aspect A] [--style S] [--layout L] [--palette-css P] [--ref IMG] [--pin M/ID] [--icon-pack P] [--strict]` | prompt file, then Gemini `gemini-3-pro-image`, then `infographic.png` |
| `iig3d.py add --image IMG --meta meta.yaml` | register a user image as a reference (below) |
| `iig3d.py docs` | regenerate `docs/` markdown from the YAML catalogue |
| `iig3d.py check` | validate catalogue, refs, docs; exit 1 with every violation |

Exit codes: 0 ok, 1 usage or credentials (JSON `error`), 2 API or output failure.

## Add a reference image

1. View the image. Decide: existing member (`member:`) or a new `3d-<name>` (`new_member:` full block; copy a member YAML from `<skill>/catalogue/members/` and drop `refs`, `pairings`, `source`).
2. Write `meta.yaml` from `<skill>/templates/meta.example.yaml`: `shows` (what the image shows), `flags` (`clean`, `watermark`, `low-res`), `pairings` (layouts this ref suits), optional `variant` (a name from the member's `layout.variants`) and `item_count` (items the image holds; a pinned render warns on a mismatch).
3. `iig3d.py add --image PATH --meta meta.yaml`; the script resizes to 1600 px JPEG, appends the YAML entry, regenerates docs and runs `check`. Rights for the image stay with the user. The JSON `pin` (`<member>/<id>`) is what a spec's `pin:` takes to reproduce this image straight away.
4. Review `<skill>/docs/members/<member>.md` and report. Vendored entries are never edited by `add`, only extended.
