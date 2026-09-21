---
type: Module
title: prepare
description: "Graphify community 39: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:21:21Z" }
stale_after: "2026-10-05T05:21:21Z"
source_commit: 2efd6dab1b448f314234109aa7de72730da1239c
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:21:18+10:00", digest: 92e1dac7df45de37 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .member() (skills/iig3d/scripts/iig3d.py:L108)
- .resolve_ref() (skills/iig3d/scripts/iig3d.py:L121)
- A catalogue ref named by the user: `<member>/<id|file|stem>`, a… (skills/iig3d/scripts/iig3d.py:L122)
- resolve_logo() (skills/iig3d/scripts/iig3d.py:L1233)
- The logo to stamp: `--logo PATH`, else IIG3D_LOGO, else the bundled Intelia… (skills/iig3d/scripts/iig3d.py:L1234)
- prepare() (skills/iig3d/scripts/iig3d.py:L1745)
- Shared front half of prompt and render: spec, route, aspect, refs, palette,… (skills/iig3d/scripts/iig3d.py:L1746)
- cmd_render() (skills/iig3d/scripts/iig3d.py:L1786)
- cmd_refs() (skills/iig3d/scripts/iig3d.py:L1814)
- The refs a render would pass, plus every catalogue ref of the member with its… (skills/iig3d/scripts/iig3d.py:L1815)
- pick_style_refs() (skills/iig3d/scripts/iig3d.py:L417)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L418)
- pick_pinned_refs() (skills/iig3d/scripts/iig3d.py:L461)
- The pinned ref first, then the layout's style refs as company up to per_render… (skills/iig3d/scripts/iig3d.py:L462)
- select_refs() (skills/iig3d/scripts/iig3d.py:L479)
- Style refs as paths (see pick_style_refs), then the icon sheet, then user refs,… (skills/iig3d/scripts/iig3d.py:L488)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [resolve_icons](/modules/resolve-icons.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
