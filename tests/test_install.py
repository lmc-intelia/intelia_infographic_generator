"""R17: just install-local / uninstall-local manage the two symlinks and refuse real directories."""

from __future__ import annotations

import os
import shutil
import subprocess

import pytest

from tests.conftest import REPO

pytestmark = pytest.mark.skipif(shutil.which("just") is None, reason="just not installed")


@pytest.fixture
def repo_copy(tmp_path):
    copy = tmp_path / "repo"
    copy.mkdir()
    shutil.copy(REPO / "justfile", copy / "justfile")
    (copy / "skills" / "iig3d").mkdir(parents=True)
    (copy / "skills" / "iig3d" / "SKILL.md").write_text("---\nname: iig3d\n---\n")
    home = tmp_path / "home"
    home.mkdir()
    return copy, home


def just(copy, home, recipe):
    env = {**os.environ, "HOME": str(home)}
    return subprocess.run(["just", recipe], cwd=copy, env=env, capture_output=True, text=True)


def test_install_and_uninstall(repo_copy):
    copy, home = repo_copy
    result = just(copy, home, "install-local")
    assert result.returncode == 0, result.stderr
    user_link = home / ".claude" / "skills" / "iig3d"
    project_link = copy / ".claude" / "skills" / "iig3d"
    assert user_link.is_symlink() and user_link.resolve() == (copy / "skills" / "iig3d").resolve()
    assert project_link.is_symlink() and project_link.resolve() == (copy / "skills" / "iig3d").resolve()
    assert str(project_link.readlink()) == "../../skills/iig3d"
    assert just(copy, home, "install-local").returncode == 0  # idempotent
    result = just(copy, home, "uninstall-local")
    assert result.returncode == 0, result.stderr
    assert not user_link.exists() and not project_link.exists()


def test_refuses_real_directory(repo_copy):
    copy, home = repo_copy
    real = home / ".claude" / "skills" / "iig3d"
    real.mkdir(parents=True)
    result = just(copy, home, "install-local")
    assert result.returncode != 0
    assert real.is_dir() and not real.is_symlink()
    assert not (copy / ".claude" / "skills" / "iig3d").exists()
    assert just(copy, home, "uninstall-local").returncode == 0
    assert real.is_dir()
