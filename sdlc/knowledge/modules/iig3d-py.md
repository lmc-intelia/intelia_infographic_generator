---
type: Module
title: iig3d.py
description: "Graphify community 41: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:06:16Z" }
stale_after: "2026-10-05T05:06:16Z"
source_commit: 6ac4d77c7d0e6ad62e60d2fa01cebbade71dc4ca
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:06:12+10:00", digest: 755d0eccdd75a015 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L1139)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L1140)
- exit_code() (skills/iig3d/scripts/iig3d.py:L1209)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L1260)
- build_parser() (skills/iig3d/scripts/iig3d.py:L1599)
- _split_vars() (skills/iig3d/scripts/iig3d.py:L1654)
- cmd_palette() (skills/iig3d/scripts/iig3d.py:L1774)
- dispatch() (skills/iig3d/scripts/iig3d.py:L1797)
- main() (skills/iig3d/scripts/iig3d.py:L1803)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L383)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L390)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L391)
- Colour (skills/iig3d/scripts/iig3d.py:L521)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L525)
- _nums() (skills/iig3d/scripts/iig3d.py:L529)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L533)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L534)
- is_neutral() (skills/iig3d/scripts/iig3d.py:L562)
- Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10… (skills/iig3d/scripts/iig3d.py:L563)
- extract_palette() (skills/iig3d/scripts/iig3d.py:L569)
- Colours from a CSS file: custom properties in declaration order, then bare… (skills/iig3d/scripts/iig3d.py:L570)
- palette_paragraph() (skills/iig3d/scripts/iig3d.py:L612)
- Prompt (skills/iig3d/scripts/iig3d.py:L943)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [.items](/modules/items.md)
- [Member](/modules/member.md)
- [normalise_image](/modules/normalise-image.md)
- [Path](/modules/path.md)
- [resolve_icons](/modules/resolve-icons.md)

# Inferred
- [Catalogue](/modules/catalogue.md)

# Features
- [iig3d skill](/features/iig3d-skill.md)
