---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
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
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- build_parser() (skills/iig3d/scripts/iig3d.py:L1112)
- dispatch() (skills/iig3d/scripts/iig3d.py:L1253)
- main() (skills/iig3d/scripts/iig3d.py:L1259)
- _dry_assembly() (skills/iig3d/scripts/iig3d.py:L1347)
- Assemble a prompt for every member x pairing layout; report ref-rule violations. (skills/iig3d/scripts/iig3d.py:L1348)
- Item (skills/iig3d/scripts/iig3d.py:L237)
- Spec (skills/iig3d/scripts/iig3d.py:L245)
- _str() (skills/iig3d/scripts/iig3d.py:L265)
- _opt_str() (skills/iig3d/scripts/iig3d.py:L269)
- load_spec() (skills/iig3d/scripts/iig3d.py:L273)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L274)
- _pairing() (skills/iig3d/scripts/iig3d.py:L355)
- Ref ids paired with the layout; the member's first pairing when the layout has… (skills/iig3d/scripts/iig3d.py:L356)
- pick_style_refs() (skills/iig3d/scripts/iig3d.py:L360)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L361)
- ref_rule_violations() (skills/iig3d/scripts/iig3d.py:L394)
- The two selection invariants, stated once for the selector and the checker. (skills/iig3d/scripts/iig3d.py:L395)
- _nums() (skills/iig3d/scripts/iig3d.py:L443)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L447)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L448)
- redact() (skills/iig3d/scripts/iig3d.py:L544)
- content_block() (skills/iig3d/scripts/iig3d.py:L587)
- text_labels() (skills/iig3d/scripts/iig3d.py:L611)
- exit_code() (skills/iig3d/scripts/iig3d.py:L750)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L801)

# Depends on
- [add_ref](/modules/add-ref.md)
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [normalise_image](/modules/normalise-image.md)
- [Path](/modules/path.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [Path](/modules/path.md)

# Features
- [iig3d skill](/features/iig3d-skill.md)
