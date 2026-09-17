---
type: Module
title: assemble
description: "Graphify community 41: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T03:14:52Z" }
stale_after: "2026-10-01T03:14:52Z"
source_commit: 08802b907cd4f8f7021c481a3d443d13812b6656
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T12:38:26+10:00", digest: 4be94854c4daa288 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- _split_vars() (skills/iig3d/scripts/iig3d.py:L1160)
- prepare() (skills/iig3d/scripts/iig3d.py:L1180)
- Shared front half of prompt and render: spec, route, aspect, refs, palette,… (skills/iig3d/scripts/iig3d.py:L1181)
- cmd_palette() (skills/iig3d/scripts/iig3d.py:L1229)
- orientation() (skills/iig3d/scripts/iig3d.py:L351)
- Colour (skills/iig3d/scripts/iig3d.py:L438)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L442)
- is_neutral() (skills/iig3d/scripts/iig3d.py:L479)
- Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10… (skills/iig3d/scripts/iig3d.py:L480)
- extract_palette() (skills/iig3d/scripts/iig3d.py:L486)
- Colours from a CSS file: custom properties in declaration order, then bare… (skills/iig3d/scripts/iig3d.py:L487)
- palette_paragraph() (skills/iig3d/scripts/iig3d.py:L529)
- Prompt (skills/iig3d/scripts/iig3d.py:L541)
- word_count() (skills/iig3d/scripts/iig3d.py:L626)
- assemble() (skills/iig3d/scripts/iig3d.py:L630)
- Fill templates/base-prompt.md; warnings for text budget and item range; strict… (skills/iig3d/scripts/iig3d.py:L641)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L691)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L692)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [_dry_assembly](/modules/dry-assembly.md)
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
