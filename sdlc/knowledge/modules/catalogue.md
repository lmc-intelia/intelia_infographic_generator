---
type: Module
title: Catalogue
description: "Graphify community 39: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:03:47Z" }
stale_after: "2026-10-05T05:03:47Z"
source_commit: b59f3451dc0b77b589cbafd9812f581df6f10352
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:03:44+10:00", digest: 1eab83aa7c95cc71 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .member() (skills/iig3d/scripts/iig3d.py:L108)
- .ref_path() (skills/iig3d/scripts/iig3d.py:L114)
- .is_layout() (skills/iig3d/scripts/iig3d.py:L117)
- A general routing layout or a member's own device name. (skills/iig3d/scripts/iig3d.py:L118)
- .resolve_ref() (skills/iig3d/scripts/iig3d.py:L121)
- A catalogue ref named by the user: `<member>/<id|file|stem>`, a… (skills/iig3d/scripts/iig3d.py:L122)
- .pin_token() (skills/iig3d/scripts/iig3d.py:L142)
- .flag_values() (skills/iig3d/scripts/iig3d.py:L151)
- prepare() (skills/iig3d/scripts/iig3d.py:L1677)
- Shared front half of prompt and render: spec, route, aspect, refs, palette,… (skills/iig3d/scripts/iig3d.py:L1678)
- cmd_render() (skills/iig3d/scripts/iig3d.py:L1718)
- cmd_route() (skills/iig3d/scripts/iig3d.py:L1738)
- cmd_refs() (skills/iig3d/scripts/iig3d.py:L1745)
- The refs a render would pass, plus every catalogue ref of the member with its… (skills/iig3d/scripts/iig3d.py:L1746)
- cmd_icons() (skills/iig3d/scripts/iig3d.py:L1760)
- Name search and text-based suggestion in one call, so Claude can pick or verify… (skills/iig3d/scripts/iig3d.py:L1761)
- cmd_check() (skills/iig3d/scripts/iig3d.py:L1782)
- check() (skills/iig3d/scripts/iig3d.py:L1843)
- Every catalogue rule in one pass; empty list means clean. (skills/iig3d/scripts/iig3d.py:L1844)
- Route (skills/iig3d/scripts/iig3d.py:L229)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L236)
- split_style() (skills/iig3d/scripts/iig3d.py:L240)
- (style, pin) after reading a ref name out of `style`: with `layout` naming a… (skills/iig3d/scripts/iig3d.py:L241)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L254)
- select_refs() (skills/iig3d/scripts/iig3d.py:L479)
- Style refs as paths (see pick_style_refs), then the icon sheet, then user refs,… (skills/iig3d/scripts/iig3d.py:L488)
- Catalogue (skills/iig3d/scripts/iig3d.py:L91)
- .routing() (skills/iig3d/scripts/iig3d.py:L98)
- has_negative_list() (skills/iig3d/scripts/iig3d.py:L988)

# Depends on
- [assemble](/modules/assemble.md)
- [iig3d.py](/modules/iig3d-py.md)
- [.items](/modules/items.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [resolve_icons](/modules/resolve-icons.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
