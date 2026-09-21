---
type: Module
title: conftest.py
description: "Graphify community 5: tests/conftest.py, tests/test_install.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:30:03Z" }
stale_after: "2026-10-05T05:30:03Z"
source_commit: fae00c698effe61c7083ae8264ab6a14d68f8f09
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-17T11:22:55+10:00", digest: 889844ff3ec7d899 }
  - { id: test_install, resource: tests/test_install.py, last_modified: "2026-09-17T11:38:15+10:00", digest: dccf82b998a27cee }
---

# Files
- `tests/conftest.py`
- `tests/test_install.py`

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
- test_install.py (tests/test_install.py:L1)
- R17: just install-local / uninstall-local manage the two symlinks and refuse… (tests/test_install.py:L1)
- repo_copy() (tests/test_install.py:L17)
- just() (tests/test_install.py:L28)
- test_install_and_uninstall() (tests/test_install.py:L33)
- test_refuses_real_directory() (tests/test_install.py:L48)

# Depends on
- [test_render.py](/modules/test-render-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
