---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T01:21:04Z" }
stale_after: "2026-10-01T01:21:04Z"
source_commit: fa6e99be0b4fc2a31b39a5a34c91b557f3e9e9a9
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T11:21:00+10:00", digest: c0f06e72cfc5879e }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L100)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L105)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L111)
- Route (skills/iig3d/scripts/iig3d.py:L171)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L178)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L189)
- Item (skills/iig3d/scripts/iig3d.py:L231)
- Spec (skills/iig3d/scripts/iig3d.py:L239)
- _str() (skills/iig3d/scripts/iig3d.py:L255)
- load_spec() (skills/iig3d/scripts/iig3d.py:L259)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L260)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L312)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L319)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L320)
- UsageError (skills/iig3d/scripts/iig3d.py:L33)
- orientation() (skills/iig3d/scripts/iig3d.py:L334)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L34)
- select_refs() (skills/iig3d/scripts/iig3d.py:L350)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L357)
- Colour (skills/iig3d/scripts/iig3d.py:L414)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L418)
- _nums() (skills/iig3d/scripts/iig3d.py:L422)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L426)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L427)
- is_neutral() (skills/iig3d/scripts/iig3d.py:L455)
- Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10… (skills/iig3d/scripts/iig3d.py:L456)
- extract_palette() (skills/iig3d/scripts/iig3d.py:L462)
- Colours from a CSS file: custom properties in declaration order, then bare… (skills/iig3d/scripts/iig3d.py:L463)
- palette_paragraph() (skills/iig3d/scripts/iig3d.py:L509)
- Prompt (skills/iig3d/scripts/iig3d.py:L521)
- redact() (skills/iig3d/scripts/iig3d.py:L527)
- slugify() (skills/iig3d/scripts/iig3d.py:L531)
- _bullets() (skills/iig3d/scripts/iig3d.py:L535)
- render_layout_block() (skills/iig3d/scripts/iig3d.py:L539)
- The member's device layout as the markdown block the Layout Guidelines slot… (skills/iig3d/scripts/iig3d.py:L540)
- content_block() (skills/iig3d/scripts/iig3d.py:L556)
- text_labels() (skills/iig3d/scripts/iig3d.py:L580)
- word_count() (skills/iig3d/scripts/iig3d.py:L592)
- assemble() (skills/iig3d/scripts/iig3d.py:L596)
- Fill templates/base-prompt.md; warnings for text budget and item range; strict… (skills/iig3d/scripts/iig3d.py:L607)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L658)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L659)
- build_parser() (skills/iig3d/scripts/iig3d.py:L673)
- main() (skills/iig3d/scripts/iig3d.py:L681)
- Catalogue (skills/iig3d/scripts/iig3d.py:L76)
- .routing() (skills/iig3d/scripts/iig3d.py:L83)
- .layouts() (skills/iig3d/scripts/iig3d.py:L87)
- .member() (skills/iig3d/scripts/iig3d.py:L90)
- .ref_path() (skills/iig3d/scripts/iig3d.py:L96)

# Depends on
- [Member](/modules/member.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
