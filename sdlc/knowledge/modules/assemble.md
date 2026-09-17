---
type: Module
title: assemble
description: "Graphify community 41: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T02:19:39Z" }
stale_after: "2026-10-01T02:19:39Z"
source_commit: 1c44ce7af8f81c51eaf6b7d3b08e5cffeb7b73da
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T12:19:34+10:00", digest: 6abb96a301e9dd69 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- _split_vars() (skills/iig3d/scripts/iig3d.py:L1157)
- prepare() (skills/iig3d/scripts/iig3d.py:L1177)
- Shared front half of prompt and render: spec, route, aspect, refs, palette,… (skills/iig3d/scripts/iig3d.py:L1178)
- cmd_palette() (skills/iig3d/scripts/iig3d.py:L1226)
- Colour (skills/iig3d/scripts/iig3d.py:L435)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L439)
- is_neutral() (skills/iig3d/scripts/iig3d.py:L476)
- Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10… (skills/iig3d/scripts/iig3d.py:L477)
- extract_palette() (skills/iig3d/scripts/iig3d.py:L483)
- Colours from a CSS file: custom properties in declaration order, then bare… (skills/iig3d/scripts/iig3d.py:L484)
- palette_paragraph() (skills/iig3d/scripts/iig3d.py:L526)
- Prompt (skills/iig3d/scripts/iig3d.py:L538)
- word_count() (skills/iig3d/scripts/iig3d.py:L623)
- assemble() (skills/iig3d/scripts/iig3d.py:L627)
- Fill templates/base-prompt.md; warnings for text budget and item range; strict… (skills/iig3d/scripts/iig3d.py:L638)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L688)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L689)

# Depends on
- [add_ref](/modules/add-ref.md)
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
