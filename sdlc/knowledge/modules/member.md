---
type: Module
title: Member
description: "Graphify community 33: skills/iig3d/scripts/iig3d.py"
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
- .member() (skills/iig3d/scripts/iig3d.py:L108)
- .resolve_ref() (skills/iig3d/scripts/iig3d.py:L121)
- A catalogue ref named by the user: `<member>/<id|file|stem>`, a… (skills/iig3d/scripts/iig3d.py:L122)
- cmd_refs() (skills/iig3d/scripts/iig3d.py:L1726)
- The refs a render would pass, plus every catalogue ref of the member with its… (skills/iig3d/scripts/iig3d.py:L1727)
- Route (skills/iig3d/scripts/iig3d.py:L229)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L236)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L254)
- _pairing() (skills/iig3d/scripts/iig3d.py:L408)
- Ref ids paired with the layout; the member's first pairing when the layout has… (skills/iig3d/scripts/iig3d.py:L409)
- pick_style_refs() (skills/iig3d/scripts/iig3d.py:L413)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L414)
- pick_pinned_refs() (skills/iig3d/scripts/iig3d.py:L457)
- The pinned ref first, then the layout's style refs as company up to per_render… (skills/iig3d/scripts/iig3d.py:L458)
- select_refs() (skills/iig3d/scripts/iig3d.py:L475)
- Style refs as paths (see pick_style_refs), then the icon sheet, then user refs,… (skills/iig3d/scripts/iig3d.py:L484)
- Member (skills/iig3d/scripts/iig3d.py:L55)
- .name() (skills/iig3d/scripts/iig3d.py:L59)
- .aspect_default() (skills/iig3d/scripts/iig3d.py:L67)
- .prompt_fragment() (skills/iig3d/scripts/iig3d.py:L71)
- .refs() (skills/iig3d/scripts/iig3d.py:L75)
- .pairings() (skills/iig3d/scripts/iig3d.py:L79)
- .alternates() (skills/iig3d/scripts/iig3d.py:L83)
- .__getitem__() (skills/iig3d/scripts/iig3d.py:L86)
- render_layout_block() (skills/iig3d/scripts/iig3d.py:L977)
- The member's device layout as the markdown block the Layout Guidelines slot… (skills/iig3d/scripts/iig3d.py:L978)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
