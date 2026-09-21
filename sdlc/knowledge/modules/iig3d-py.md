---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:12:49Z" }
stale_after: "2026-10-05T05:12:49Z"
source_commit: 0dac1771abb0a241b787b37f99663e8da1c9a6f4
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:06:12+10:00", digest: 755d0eccdd75a015 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- text_labels() (skills/iig3d/scripts/iig3d.py:L1019)
- word_count() (skills/iig3d/scripts/iig3d.py:L1031)
- reference_composition() (skills/iig3d/scripts/iig3d.py:L1035)
- The Reference Composition section: reproduce reference image 1, swap in the… (skills/iig3d/scripts/iig3d.py:L1036)
- assemble() (skills/iig3d/scripts/iig3d.py:L1054)
- Fill templates/base-prompt.md; warnings for text budget and item range; strict… (skills/iig3d/scripts/iig3d.py:L1068)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L1139)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L1140)
- exit_code() (skills/iig3d/scripts/iig3d.py:L1209)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L1260)
- build_parser() (skills/iig3d/scripts/iig3d.py:L1599)
- dispatch() (skills/iig3d/scripts/iig3d.py:L1797)
- main() (skills/iig3d/scripts/iig3d.py:L1803)
- _dry_assembly() (skills/iig3d/scripts/iig3d.py:L1891)
- Assemble a prompt for every member x pairing layout; report ref-rule violations. (skills/iig3d/scripts/iig3d.py:L1892)
- Item (skills/iig3d/scripts/iig3d.py:L286)
- Spec (skills/iig3d/scripts/iig3d.py:L294)
- _str() (skills/iig3d/scripts/iig3d.py:L317)
- _opt_str() (skills/iig3d/scripts/iig3d.py:L321)
- load_spec() (skills/iig3d/scripts/iig3d.py:L325)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L326)
- orientation() (skills/iig3d/scripts/iig3d.py:L405)
- ref_rule_violations() (skills/iig3d/scripts/iig3d.py:L451)
- The two selection invariants, stated once for the selector and the checker. (skills/iig3d/scripts/iig3d.py:L452)
- _nums() (skills/iig3d/scripts/iig3d.py:L529)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L533)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L534)
- is_neutral() (skills/iig3d/scripts/iig3d.py:L562)
- Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10… (skills/iig3d/scripts/iig3d.py:L563)
- icon_guidance() (skills/iig3d/scripts/iig3d.py:L921)
- The Icon Set section: copy each numbered glyph from the sheet onto its item. (skills/iig3d/scripts/iig3d.py:L922)
- Prompt (skills/iig3d/scripts/iig3d.py:L943)
- redact() (skills/iig3d/scripts/iig3d.py:L949)
- slugify() (skills/iig3d/scripts/iig3d.py:L953)
- render_layout_block() (skills/iig3d/scripts/iig3d.py:L981)
- The member's device layout as the markdown block the Layout Guidelines slot… (skills/iig3d/scripts/iig3d.py:L982)
- content_block() (skills/iig3d/scripts/iig3d.py:L992)
- The content section; `icon_slots` maps item index to a sheet glyph note… (skills/iig3d/scripts/iig3d.py:L993)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)
- [resolve_icons](/modules/resolve-icons.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- [Catalogue](/modules/catalogue.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)
- [resolve_icons](/modules/resolve-icons.md)

# Features
- [iig3d skill](/features/iig3d-skill.md)
