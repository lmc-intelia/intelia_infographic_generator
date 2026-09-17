---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T01:21:39Z" }
stale_after: "2026-10-01T01:21:39Z"
source_commit: 646c305c3cf5097475ddbd17e3f8940ff9f1afdb
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T11:21:36+10:00", digest: 3e8fad61a293ed20 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L101)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L106)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L112)
- Route (skills/iig3d/scripts/iig3d.py:L172)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L179)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L190)
- Item (skills/iig3d/scripts/iig3d.py:L232)
- Spec (skills/iig3d/scripts/iig3d.py:L240)
- _str() (skills/iig3d/scripts/iig3d.py:L256)
- load_spec() (skills/iig3d/scripts/iig3d.py:L260)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L261)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L313)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L320)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L321)
- orientation() (skills/iig3d/scripts/iig3d.py:L335)
- UsageError (skills/iig3d/scripts/iig3d.py:L34)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L35)
- select_refs() (skills/iig3d/scripts/iig3d.py:L351)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L358)
- Colour (skills/iig3d/scripts/iig3d.py:L415)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L419)
- _nums() (skills/iig3d/scripts/iig3d.py:L423)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L427)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L428)
- is_neutral() (skills/iig3d/scripts/iig3d.py:L456)
- Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10… (skills/iig3d/scripts/iig3d.py:L457)
- extract_palette() (skills/iig3d/scripts/iig3d.py:L463)
- Colours from a CSS file: custom properties in declaration order, then bare… (skills/iig3d/scripts/iig3d.py:L464)
- palette_paragraph() (skills/iig3d/scripts/iig3d.py:L510)
- Prompt (skills/iig3d/scripts/iig3d.py:L522)
- redact() (skills/iig3d/scripts/iig3d.py:L528)
- slugify() (skills/iig3d/scripts/iig3d.py:L532)
- _bullets() (skills/iig3d/scripts/iig3d.py:L536)
- render_layout_block() (skills/iig3d/scripts/iig3d.py:L540)
- The member's device layout as the markdown block the Layout Guidelines slot… (skills/iig3d/scripts/iig3d.py:L541)
- content_block() (skills/iig3d/scripts/iig3d.py:L557)
- text_labels() (skills/iig3d/scripts/iig3d.py:L581)
- word_count() (skills/iig3d/scripts/iig3d.py:L593)
- assemble() (skills/iig3d/scripts/iig3d.py:L597)
- Fill templates/base-prompt.md; warnings for text budget and item range; strict… (skills/iig3d/scripts/iig3d.py:L608)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L659)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L660)
- parse_env_file() (skills/iig3d/scripts/iig3d.py:L676)
- Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments… (skills/iig3d/scripts/iig3d.py:L677)
- api_key() (skills/iig3d/scripts/iig3d.py:L697)
- (key, source). Order: --api-key, ./.env in the calling directory, process… (skills/iig3d/scripts/iig3d.py:L698)
- build_parser() (skills/iig3d/scripts/iig3d.py:L716)
- main() (skills/iig3d/scripts/iig3d.py:L724)
- Catalogue (skills/iig3d/scripts/iig3d.py:L77)
- .routing() (skills/iig3d/scripts/iig3d.py:L84)
- .layouts() (skills/iig3d/scripts/iig3d.py:L88)
- .member() (skills/iig3d/scripts/iig3d.py:L91)
- .ref_path() (skills/iig3d/scripts/iig3d.py:L97)

# Depends on
- [Member](/modules/member.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
