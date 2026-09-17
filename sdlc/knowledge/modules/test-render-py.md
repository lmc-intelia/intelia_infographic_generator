---
type: Module
title: test_render.py
description: "Graphify community 40: tests/conftest.py, tests/test_render.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T02:19:39Z" }
stale_after: "2026-10-01T02:19:39Z"
source_commit: 1c44ce7af8f81c51eaf6b7d3b08e5cffeb7b73da
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-17T11:22:55+10:00", digest: 889844ff3ec7d899 }
  - { id: test_render, resource: tests/test_render.py, last_modified: "2026-09-17T12:19:34+10:00", digest: d54b01519bd25a08 }
---

# Files
- `tests/conftest.py`
- `tests/test_render.py`

# Symbols
- png_bytes() (tests/conftest.py:L99)
- test_render.py (tests/test_render.py:L1)
- R11: dry-run shape, PNG save, backup rename, retries, exit codes; live smoke… (tests/test_render.py:L1)
- test_live_smoke() (tests/test_render.py:L105)
- test_bad_ref_image_is_error_not_traceback() (tests/test_render.py:L111)
- Review finding: failures before the API call must still yield the error record… (tests/test_render.py:L112)
- test_client_factory_failure_is_error() (tests/test_render.py:L120)
- prompt_file() (tests/test_render.py:L16)
- test_dry_run_shape_and_no_file() (tests/test_render.py:L23)
- test_saves_png_and_flattens_rgba() (tests/test_render.py:L32)
- test_refs_passed_as_images_with_style_note() (tests/test_render.py:L48)
- test_backup_rename_on_rerun() (tests/test_render.py:L60)
- test_retry_then_error() (tests/test_render.py:L70)
- test_retry_then_success() (tests/test_render.py:L79)
- test_no_image_part_is_error() (tests/test_render.py:L86)
- test_exit_codes() (tests/test_render.py:L93)
- test_bad_resolution_rejected() (tests/test_render.py:L99)

# Depends on
- [conftest.py](/modules/conftest-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
