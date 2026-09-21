---
type: Module
title: normalise_image
description: "Graphify community 50: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:06:16Z" }
stale_after: "2026-10-05T05:06:16Z"
source_commit: 6ac4d77c7d0e6ad62e60d2fa01cebbade71dc4ca
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:06:12+10:00", digest: 755d0eccdd75a015 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- to_rgb() (skills/iig3d/scripts/iig3d.py:L1213)
- Flatten any PIL mode to RGB; alpha composites onto `background`. (skills/iig3d/scripts/iig3d.py:L1214)
- _image_from_response() (skills/iig3d/scripts/iig3d.py:L1227)
- First inline image part of a Gemini response as an RGB PIL image; None when… (skills/iig3d/scripts/iig3d.py:L1228)
- normalise_image() (skills/iig3d/scripts/iig3d.py:L1371)
- Copy `src` to `dest` as an RGB JPEG no larger than `max_edge` on its long side. (skills/iig3d/scripts/iig3d.py:L1372)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
