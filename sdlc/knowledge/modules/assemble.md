---
type: Module
title: assemble
description: "Graphify community 41: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T04:30:53Z" }
stale_after: "2026-10-05T04:30:53Z"
source_commit: 71c08107aa2dfcc1db57f7b3771bfd7713d219d0
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T14:30:49+10:00", digest: fe9bead68c7c4cae }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- _dry_assembly() (skills/iig3d/scripts/iig3d.py:L1640)
- Assemble a prompt for every member x pairing layout; report ref-rule violations. (skills/iig3d/scripts/iig3d.py:L1641)
- Route (skills/iig3d/scripts/iig3d.py:L228)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L235)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L253)
- Item (skills/iig3d/scripts/iig3d.py:L285)
- Spec (skills/iig3d/scripts/iig3d.py:L293)
- orientation() (skills/iig3d/scripts/iig3d.py:L400)
- ref_rule_violations() (skills/iig3d/scripts/iig3d.py:L446)
- The two selection invariants, stated once for the selector and the checker. (skills/iig3d/scripts/iig3d.py:L447)
- icon_guidance() (skills/iig3d/scripts/iig3d.py:L706)
- The Icon Set section: copy each numbered glyph from the sheet onto its item. (skills/iig3d/scripts/iig3d.py:L707)
- Prompt (skills/iig3d/scripts/iig3d.py:L728)
- redact() (skills/iig3d/scripts/iig3d.py:L734)
- content_block() (skills/iig3d/scripts/iig3d.py:L777)
- The content section; `icon_slots` maps item index to a sheet glyph note… (skills/iig3d/scripts/iig3d.py:L778)
- text_labels() (skills/iig3d/scripts/iig3d.py:L804)
- word_count() (skills/iig3d/scripts/iig3d.py:L816)
- reference_composition() (skills/iig3d/scripts/iig3d.py:L820)
- The Reference Composition section: reproduce reference image 1, swap in the… (skills/iig3d/scripts/iig3d.py:L821)
- assemble() (skills/iig3d/scripts/iig3d.py:L839)
- Fill templates/base-prompt.md; warnings for text budget and item range; strict… (skills/iig3d/scripts/iig3d.py:L853)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L924)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L925)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [.items](/modules/items.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
