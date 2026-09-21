---
type: Module
title: test_render.py
description: "Graphify community 5: tests/conftest.py, tests/test_install.py, tests/test_render.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T02:47:44Z" }
stale_after: "2026-10-05T02:47:44Z"
source_commit: 2285898e55a2ed6720d292c1eb4bd34a1f6f1690
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-17T11:22:55+10:00", digest: 889844ff3ec7d899 }
  - { id: test_install, resource: tests/test_install.py, last_modified: "2026-09-17T11:38:15+10:00", digest: dccf82b998a27cee }
  - { id: test_render, resource: tests/test_render.py, last_modified: "2026-09-17T12:19:34+10:00", digest: d54b01519bd25a08 }
---

# Files
- `tests/conftest.py`
- `tests/test_install.py`
- `tests/test_render.py`

# Symbols
- conftest.py (tests/conftest.py:L1)
- Shared fixtures: import the single-file skill script as a module. (tests/conftest.py:L1)
- fake_client() (tests/conftest.py:L110)
- Return a factory(api_key) -> FakeClient with the given behaviour list; exposes… (tests/conftest.py:L111)
- load_module() (tests/conftest.py:L17)
- iig3d() (tests/conftest.py:L26)
- skill_root() (tests/conftest.py:L31)
- fixtures() (tests/conftest.py:L36)
- tmp_catalogue() (tests/conftest.py:L41)
- A copy of the shipped catalogue in a temp skill root with a small JPEG for… (tests/conftest.py:L42)
- FakeInline (tests/conftest.py:L61)
- .__init__() (tests/conftest.py:L62)
- FakePart (tests/conftest.py:L66)
- .__init__() (tests/conftest.py:L67)
- FakeResponse (tests/conftest.py:L72)
- .__init__() (tests/conftest.py:L73)
- FakeModels (tests/conftest.py:L77)
- Records generate_content calls; behaviour is a list consumed per call: bytes,… (tests/conftest.py:L78)
- .__init__() (tests/conftest.py:L80)
- .generate_content() (tests/conftest.py:L84)
- FakeClient (tests/conftest.py:L94)
- .__init__() (tests/conftest.py:L95)
- png_bytes() (tests/conftest.py:L99)
- test_install.py (tests/test_install.py:L1)
- R17: just install-local / uninstall-local manage the two symlinks and refuse… (tests/test_install.py:L1)
- repo_copy() (tests/test_install.py:L17)
- just() (tests/test_install.py:L28)
- test_install_and_uninstall() (tests/test_install.py:L33)
- test_refuses_real_directory() (tests/test_install.py:L48)
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
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
