---
type: Module
title: test_cli.py
description: "Graphify community 7: tests/test_cli.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:03:47Z" }
stale_after: "2026-10-05T05:03:47Z"
source_commit: b59f3451dc0b77b589cbafd9812f581df6f10352
sources:
  - { id: test_cli, resource: tests/test_cli.py, last_modified: "2026-09-21T15:03:44+10:00", digest: 642c971c2f3553fa }
---

# Files
- `tests/test_cli.py`

# Symbols
- test_cli.py (tests/test_cli.py:L1)
- R1, R11, R16: the script imports as a module and exposes the subcommand table. (tests/test_cli.py:L1)
- test_remaining_commands_print_one_json() (tests/test_cli.py:L104)
- test_refs_lists_pins_and_layout_optional() (tests/test_cli.py:L109)
- test_refs_with_pin() (tests/test_cli.py:L117)
- test_module_imports_and_has_main() (tests/test_cli.py:L12)
- test_prompt_with_pin_flag() (tests/test_cli.py:L123)
- test_prompt_pin_conflicting_style_exits_1() (tests/test_cli.py:L132)
- test_prompt_layout_member_style_ref() (tests/test_cli.py:L138)
- test_route_layout_member_style_ref() (tests/test_cli.py:L145)
- test_prompt_icon_pack_flag_builds_sheet() (tests/test_cli.py:L152)
- test_prompt_missing_icon_offline_exits_1() (tests/test_cli.py:L168)
- run() (tests/test_cli.py:L17)
- test_icons_command_suggests_and_searches() (tests/test_cli.py:L175)
- test_prompt_suggests_icons_from_labels() (tests/test_cli.py:L188)
- test_render_quality_from_spec_and_flag() (tests/test_cli.py:L202)
- test_list_reports_quality_levels() (tests/test_cli.py:L215)
- test_list_counts() (tests/test_cli.py:L25)
- test_route_shape() (tests/test_cli.py:L34)
- test_refs_shape() (tests/test_cli.py:L40)
- test_palette_shape() (tests/test_cli.py:L45)
- test_prompt_writes_file() (tests/test_cli.py:L50)
- test_render_dry_run() (tests/test_cli.py:L58)
- test_render_without_key_exits_1() (tests/test_cli.py:L71)
- test_render_with_fake_client() (tests/test_cli.py:L80)
- test_usage_error_is_json_exit_1() (tests/test_cli.py:L92)
- test_render_requires_out_dir() (tests/test_cli.py:L97)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
