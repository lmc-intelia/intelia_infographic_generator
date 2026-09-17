---
type: Module
title: test_creds.py
description: "Graphify community 20: tests/test_creds.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T03:13:15Z" }
stale_after: "2026-10-01T03:13:15Z"
source_commit: e5e99535de68b5513b2d805225a669510f6415dd
sources:
  - { id: test_creds, resource: tests/test_creds.py, last_modified: "2026-09-17T11:21:36+10:00", digest: 4c40dd0d7e15dc03 }
---

# Files
- `tests/test_creds.py`

# Symbols
- test_creds.py (tests/test_creds.py:L1)
- R10: GEMINI_API_KEY from ./.env in the calling directory, then the environment;… (tests/test_creds.py:L1)
- test_dotenv_in_cwd_wins_over_environment() (tests/test_creds.py:L14)
- test_google_key_accepted() (tests/test_creds.py:L23)
- test_environment_when_no_dotenv() (tests/test_creds.py:L29)
- test_explicit_key_wins() (tests/test_creds.py:L35)
- test_parent_dotenv_ignored() (tests/test_creds.py:L42)
- test_key_value_never_in_source() (tests/test_creds.py:L52)
- test_parse_env_file() (tests/test_creds.py:L59)
- clean_env() (tests/test_creds.py:L9)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
