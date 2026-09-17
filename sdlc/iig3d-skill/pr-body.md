## iig3d skill

### Why
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

### Artifacts
- sdlc/iig3d-skill/intent.md, spec.md, plan.md (accepted)
- test-report: passed, tdd cycles: 16
- review: Important: 5, Nit: 5

### Proof
- `uv run pytest -q` → all tests pass; expected final count ≥ 90 tests, 1 skipped (`IIG3D_LIVE` smoke) plus `test_install.py` skipped only when `just` is absent.
- `uv run skills/iig3d/scripts/iig3d.py check` → `{"status":"ok","violations":[]}`; exit 0.
- `uv run skills/iig3d/scripts/iig3d.py list` → JSON with `members` length 12 and `layouts` length 21.
- `uv run skills/iig3d/scripts/iig3d.py route --layout hierarchical-layers` → `{"member":"3d-slab-stack","alternates":["3d-glass-layer","3d-isometric-light","3d-cylinder-column"],...}`.
- `uv run skills/iig3d/scripts/iig3d.py palette --css tests/fixtures/brand.css` → JSON `colours` list of 8 entries, no greys.
- `cd /tmp && mkdir -p nokey && cd nokey && uv run <abs>/skills/iig3d/scripts/iig3d.py render --spec <abs>/skills/iig3d/templates/spec.example.yaml --out-dir out --dry-run` → exit 1, stdout JSON `error` = `no API key: expected GEMINI_API_KEY in /tmp/nokey/.env or the environment`.
- With `./.env` present: `uv run skills/iig3d/scripts/iig3d.py render --spec skills/iig3d/templates/spec.example.yaml --out-dir infographic/smoke --dry-run` → `{"status":"dry-run",...,"prompt_file":".../prompts/01-infographic-openwiki-refresh-pipeline.md"}` and the prompt file exists; without `--dry-run` → `status: ok` and `infographic/smoke/infographic.png` exists.
- `ls skills/iig3d/refs/*/ | wc -l` → 30 JPEG files; `grep -rn -- '- watermark' skills/iig3d/catalogue/members/` → no output (prompt fragments legitimately contain the words "no watermarks").
- `wc -l skills/iig3d/SKILL.md` → ≤ 80.
- `ls -l ~/.claude/skills/iig3d .claude/skills/iig3d` → both symlinks resolve to `skills/iig3d`.
- `sdlc build sync` → `{"ok": true, "unplanned": []}` after every step; `sdlc build check` → `ok: true`.
- Acceptance: 12 PNGs under `infographic/acceptance/<member>/infographic.png` reviewed by the product owner.

### Knowledge
no knowledge changes under sdlc/knowledge against main

### Documents
- build: sdlc/iig3d-skill/docs/build.html (9/9 showcase, 0 errors, 0 warnings)
- design: sdlc/iig3d-skill/docs/design.html (9/9 showcase, 0 errors, 0 warnings)
- plan: sdlc/iig3d-skill/docs/plan.html (9/9 showcase, 0 errors, 0 warnings)
- test: sdlc/iig3d-skill/docs/test.html (9/9 showcase, 0 errors, 0 warnings)
