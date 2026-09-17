---
type: Module
title: test_catalogue.py
description: "Graphify community 3: tests/test_catalogue.py, tests/test_routing.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T02:46:21Z" }
stale_after: "2026-10-01T02:46:21Z"
source_commit: e5487b438d2313f75c508e756548c657f7715926
sources:
  - { id: test_catalogue, resource: tests/test_catalogue.py, last_modified: "2026-09-17T12:19:34+10:00", digest: 395385c4ca4fb714 }
  - { id: test_routing, resource: tests/test_routing.py, last_modified: "2026-09-17T11:15:25+10:00", digest: 53a24b265e288942 }
---

# Files
- `tests/test_catalogue.py`
- `tests/test_routing.py`

# Symbols
- test_catalogue.py (tests/test_catalogue.py:L1)
- R3, R15: the YAML catalogue is complete, internally consistent and schema-valid. (tests/test_catalogue.py:L1)
- test_schema_rejects_missing_fragment() (tests/test_catalogue.py:L103)
- test_ref_files_on_disk() (tests/test_catalogue.py:L115)
- test_no_vendored_watermark() (tests/test_catalogue.py:L127)
- test_check_clean() (tests/test_catalogue.py:L133)
- test_check_reports_seeded_violations() (tests/test_catalogue.py:L137)
- test_check_dependency_parity() (tests/test_catalogue.py:L163)
- cat() (tests/test_catalogue.py:L40)
- test_twelve_members() (tests/test_catalogue.py:L44)
- test_member_keys() (tests/test_catalogue.py:L49)
- test_fragment_ends_with_negative_list() (tests/test_catalogue.py:L57)
- test_routing_rows() (tests/test_catalogue.py:L62)
- test_pairings_resolve() (tests/test_catalogue.py:L71)
- test_ref_flags() (tests/test_catalogue.py:L82)
- test_alternates_exist() (tests/test_catalogue.py:L90)
- test_family_constants() (tests/test_catalogue.py:L95)
- test_routing.py (tests/test_routing.py:L1)
- R4: industrial-3d routes by layout; a named member skips the table; unknown… (tests/test_routing.py:L1)
- cat() (tests/test_routing.py:L35)
- test_general_layout_routes_to_primary() (tests/test_routing.py:L41)
- test_device_layout_returns_member() (tests/test_routing.py:L51)
- test_explicit_member_style_skips_table() (tests/test_routing.py:L59)
- test_layout_defaults_to_member_device() (tests/test_routing.py:L66)
- test_no_layout_no_style_defaults_to_bento_grid() (tests/test_routing.py:L72)
- test_unknown_layout_lists_valid_names() (tests/test_routing.py:L78)
- test_unknown_style_lists_valid_names() (tests/test_routing.py:L84)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
