---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T01:19:06Z" }
stale_after: "2026-10-01T01:19:06Z"
source_commit: c41d6d6a630903c77274cef3967923ec721af525
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T11:19:03+10:00", digest: 1d9a9c105f180b7c }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L100)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L105)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L111)
- Route (skills/iig3d/scripts/iig3d.py:L171)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L177)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L182)
- Item (skills/iig3d/scripts/iig3d.py:L224)
- Spec (skills/iig3d/scripts/iig3d.py:L232)
- _str() (skills/iig3d/scripts/iig3d.py:L248)
- load_spec() (skills/iig3d/scripts/iig3d.py:L252)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L253)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L305)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L312)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L313)
- orientation() (skills/iig3d/scripts/iig3d.py:L327)
- UsageError (skills/iig3d/scripts/iig3d.py:L33)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L34)
- select_refs() (skills/iig3d/scripts/iig3d.py:L343)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L350)
- Colour (skills/iig3d/scripts/iig3d.py:L407)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L411)
- _nums() (skills/iig3d/scripts/iig3d.py:L415)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L419)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L420)
- is_neutral() (skills/iig3d/scripts/iig3d.py:L448)
- Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10… (skills/iig3d/scripts/iig3d.py:L449)
- extract_palette() (skills/iig3d/scripts/iig3d.py:L455)
- Colours from a CSS file: custom properties in declaration order, then bare… (skills/iig3d/scripts/iig3d.py:L456)
- palette_paragraph() (skills/iig3d/scripts/iig3d.py:L502)
- build_parser() (skills/iig3d/scripts/iig3d.py:L510)
- main() (skills/iig3d/scripts/iig3d.py:L518)
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
