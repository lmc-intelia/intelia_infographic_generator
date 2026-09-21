---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T04:52:20Z" }
stale_after: "2026-10-05T04:52:20Z"
source_commit: 8ed9020fab339416db7371697fc62e238ae2042e
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T14:48:56+10:00", digest: 05b5aa06590e0558 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- text_labels() (skills/iig3d/scripts/iig3d.py:L1015)
- word_count() (skills/iig3d/scripts/iig3d.py:L1027)
- reference_composition() (skills/iig3d/scripts/iig3d.py:L1031)
- The Reference Composition section: reproduce reference image 1, swap in the… (skills/iig3d/scripts/iig3d.py:L1032)
- assemble() (skills/iig3d/scripts/iig3d.py:L1050)
- Fill templates/base-prompt.md; warnings for text budget and item range; strict… (skills/iig3d/scripts/iig3d.py:L1064)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L1135)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L1136)
- exit_code() (skills/iig3d/scripts/iig3d.py:L1197)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L1248)
- build_parser() (skills/iig3d/scripts/iig3d.py:L1584)
- dispatch() (skills/iig3d/scripts/iig3d.py:L1781)
- main() (skills/iig3d/scripts/iig3d.py:L1787)
- _dry_assembly() (skills/iig3d/scripts/iig3d.py:L1875)
- Assemble a prompt for every member x pairing layout; report ref-rule violations. (skills/iig3d/scripts/iig3d.py:L1876)
- Item (skills/iig3d/scripts/iig3d.py:L286)
- Spec (skills/iig3d/scripts/iig3d.py:L294)
- _str() (skills/iig3d/scripts/iig3d.py:L316)
- _opt_str() (skills/iig3d/scripts/iig3d.py:L320)
- load_spec() (skills/iig3d/scripts/iig3d.py:L324)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L325)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L379)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L386)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L387)
- orientation() (skills/iig3d/scripts/iig3d.py:L401)
- ref_rule_violations() (skills/iig3d/scripts/iig3d.py:L447)
- The two selection invariants, stated once for the selector and the checker. (skills/iig3d/scripts/iig3d.py:L448)
- _nums() (skills/iig3d/scripts/iig3d.py:L525)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L529)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L530)
- icon_guidance() (skills/iig3d/scripts/iig3d.py:L917)
- The Icon Set section: copy each numbered glyph from the sheet onto its item. (skills/iig3d/scripts/iig3d.py:L918)
- Prompt (skills/iig3d/scripts/iig3d.py:L939)
- redact() (skills/iig3d/scripts/iig3d.py:L945)
- content_block() (skills/iig3d/scripts/iig3d.py:L988)
- The content section; `icon_slots` maps item index to a sheet glyph note… (skills/iig3d/scripts/iig3d.py:L989)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)
- [resolve_icons](/modules/resolve-icons.md)

# Inferred
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)
- [resolve_icons](/modules/resolve-icons.md)

# Features
- [iig3d skill](/features/iig3d-skill.md)
