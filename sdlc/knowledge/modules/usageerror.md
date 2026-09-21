---
type: Module
title: UsageError
description: "Graphify community 39: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:30:03Z" }
stale_after: "2026-10-05T05:30:03Z"
source_commit: fae00c698effe61c7083ae8264ab6a14d68f8f09
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:29:58+10:00", digest: 4b4238bdfa8f4e38 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .member() (skills/iig3d/scripts/iig3d.py:L108)
- .resolve_ref() (skills/iig3d/scripts/iig3d.py:L121)
- A catalogue ref named by the user: `<member>/<id|file|stem>`, a… (skills/iig3d/scripts/iig3d.py:L122)
- cmd_refs() (skills/iig3d/scripts/iig3d.py:L1835)
- The refs a render would pass, plus every catalogue ref of the member with its… (skills/iig3d/scripts/iig3d.py:L1836)
- Route (skills/iig3d/scripts/iig3d.py:L229)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L236)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L254)
- _pairing() (skills/iig3d/scripts/iig3d.py:L414)
- Ref ids paired with the layout; the member's first pairing when the layout has… (skills/iig3d/scripts/iig3d.py:L415)
- pick_style_refs() (skills/iig3d/scripts/iig3d.py:L419)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L420)
- UsageError (skills/iig3d/scripts/iig3d.py:L44)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L45)
- pick_pinned_refs() (skills/iig3d/scripts/iig3d.py:L463)
- The pinned ref first, then the layout's style refs as company up to per_render… (skills/iig3d/scripts/iig3d.py:L464)
- select_refs() (skills/iig3d/scripts/iig3d.py:L481)
- Style refs as paths (see pick_style_refs), then the icon sheet, then user refs,… (skills/iig3d/scripts/iig3d.py:L490)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [prepare](/modules/prepare.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
