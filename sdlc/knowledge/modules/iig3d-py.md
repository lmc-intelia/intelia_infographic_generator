---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:21:21Z" }
stale_after: "2026-10-05T05:21:21Z"
source_commit: 2efd6dab1b448f314234109aa7de72730da1239c
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:21:18+10:00", digest: 92e1dac7df45de37 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- word_count() (skills/iig3d/scripts/iig3d.py:L1031)
- reference_composition() (skills/iig3d/scripts/iig3d.py:L1035)
- The Reference Composition section: reproduce reference image 1, swap in the… (skills/iig3d/scripts/iig3d.py:L1036)
- assemble() (skills/iig3d/scripts/iig3d.py:L1054)
- Fill templates/base-prompt.md; warnings for text budget and item range; strict… (skills/iig3d/scripts/iig3d.py:L1068)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L1139)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L1140)
- exit_code() (skills/iig3d/scripts/iig3d.py:L1209)
- drop_shadow() (skills/iig3d/scripts/iig3d.py:L1244)
- A blurred black copy of the logo's alpha, shifted by `offset`; the layer is… (skills/iig3d/scripts/iig3d.py:L1245)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L1322)
- build_parser() (skills/iig3d/scripts/iig3d.py:L1668)
- _split_vars() (skills/iig3d/scripts/iig3d.py:L1725)
- cmd_palette() (skills/iig3d/scripts/iig3d.py:L1846)
- _check_type() (skills/iig3d/scripts/iig3d.py:L185)
- Walk one schema node: a bare type name or {type, keys|items|values}. (skills/iig3d/scripts/iig3d.py:L186)
- dispatch() (skills/iig3d/scripts/iig3d.py:L1869)
- main() (skills/iig3d/scripts/iig3d.py:L1875)
- Route (skills/iig3d/scripts/iig3d.py:L229)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L236)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L254)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L383)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L390)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L391)
- orientation() (skills/iig3d/scripts/iig3d.py:L405)
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
- icon_guidance() (skills/iig3d/scripts/iig3d.py:L921)
- The Icon Set section: copy each numbered glyph from the sheet onto its item. (skills/iig3d/scripts/iig3d.py:L922)
- Prompt (skills/iig3d/scripts/iig3d.py:L943)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [_dry_assembly](/modules/dry-assembly.md)
- [Member](/modules/member.md)
- [normalise_image](/modules/normalise-image.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)
- [resolve_icons](/modules/resolve-icons.md)
- [suggest_icon](/modules/suggest-icon.md)

# Inferred
- [Catalogue](/modules/catalogue.md)
- [prepare](/modules/prepare.md)
- [suggest_icon](/modules/suggest-icon.md)

# Features
- [iig3d skill](/features/iig3d-skill.md)
