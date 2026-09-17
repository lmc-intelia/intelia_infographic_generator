---
type: Module
title: UsageError
description: "Graphify community 39: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T02:38:32Z" }
stale_after: "2026-10-01T02:38:32Z"
source_commit: d8412565305a2fce317384d37b5816a2bf81c8ac
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T12:38:26+10:00", digest: 4be94854c4daa288 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .member() (skills/iig3d/scripts/iig3d.py:L105)
- .ref_path() (skills/iig3d/scripts/iig3d.py:L111)
- Route (skills/iig3d/scripts/iig3d.py:L202)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L209)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L214)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L329)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L336)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L337)
- pick_style_refs() (skills/iig3d/scripts/iig3d.py:L363)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L364)
- select_refs() (skills/iig3d/scripts/iig3d.py:L407)
- UsageError (skills/iig3d/scripts/iig3d.py:L41)
- Style refs as paths (see pick_style_refs), user refs appended, capped by… (skills/iig3d/scripts/iig3d.py:L414)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L42)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
