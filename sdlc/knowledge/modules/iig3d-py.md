---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T01:47:43Z" }
stale_after: "2026-10-01T01:47:43Z"
source_commit: 1d771a6e54b0997d70b05103a6a7a41fe3de7b8b
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T11:47:39+10:00", digest: 8cd1197f28e29ede }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- build_parser() (skills/iig3d/scripts/iig3d.py:L1104)
- _split_vars() (skills/iig3d/scripts/iig3d.py:L1149)
- prepare() (skills/iig3d/scripts/iig3d.py:L1169)
- Shared front half of prompt and render: spec, route, aspect, refs, palette,… (skills/iig3d/scripts/iig3d.py:L1170)
- cmd_palette() (skills/iig3d/scripts/iig3d.py:L1218)
- cmd_check() (skills/iig3d/scripts/iig3d.py:L1223)
- dispatch() (skills/iig3d/scripts/iig3d.py:L1245)
- main() (skills/iig3d/scripts/iig3d.py:L1251)
- Spec (skills/iig3d/scripts/iig3d.py:L244)
- orientation() (skills/iig3d/scripts/iig3d.py:L347)
- Colour (skills/iig3d/scripts/iig3d.py:L434)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L438)
- _nums() (skills/iig3d/scripts/iig3d.py:L442)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L446)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L447)
- is_neutral() (skills/iig3d/scripts/iig3d.py:L475)
- Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10… (skills/iig3d/scripts/iig3d.py:L476)
- extract_palette() (skills/iig3d/scripts/iig3d.py:L482)
- Colours from a CSS file: custom properties in declaration order, then bare… (skills/iig3d/scripts/iig3d.py:L483)
- palette_paragraph() (skills/iig3d/scripts/iig3d.py:L525)
- Prompt (skills/iig3d/scripts/iig3d.py:L537)
- redact() (skills/iig3d/scripts/iig3d.py:L543)
- slugify() (skills/iig3d/scripts/iig3d.py:L547)
- content_block() (skills/iig3d/scripts/iig3d.py:L586)
- text_labels() (skills/iig3d/scripts/iig3d.py:L610)
- word_count() (skills/iig3d/scripts/iig3d.py:L622)
- assemble() (skills/iig3d/scripts/iig3d.py:L626)
- Fill templates/base-prompt.md; warnings for text budget and item range; strict… (skills/iig3d/scripts/iig3d.py:L637)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L687)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L688)
- exit_code() (skills/iig3d/scripts/iig3d.py:L749)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L800)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [_dry_assembly](/modules/dry-assembly.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- [Path](/modules/path.md)

# Features
- [iig3d skill](/features/iig3d-skill.md)
