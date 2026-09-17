"""R10: GEMINI_API_KEY from ./.env in the calling directory, then the environment; no walk-up."""

from __future__ import annotations

import pytest


@pytest.fixture
def clean_env(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)


def test_dotenv_in_cwd_wins_over_environment(iig3d, tmp_path, monkeypatch, clean_env):
    (tmp_path / ".env").write_text("# comment\nexport GEMINI_API_KEY='from-file'\n")
    monkeypatch.setenv("GEMINI_API_KEY", "from-env")
    monkeypatch.chdir(tmp_path)
    key, source = iig3d.api_key(None)
    assert key == "from-file"
    assert source == f"{tmp_path / '.env'}:GEMINI_API_KEY"


def test_google_key_accepted(iig3d, tmp_path, monkeypatch, clean_env):
    (tmp_path / ".env").write_text('GOOGLE_API_KEY="g-key"\n')
    monkeypatch.chdir(tmp_path)
    assert iig3d.api_key(None) == ("g-key", f"{tmp_path / '.env'}:GOOGLE_API_KEY")


def test_environment_when_no_dotenv(iig3d, tmp_path, monkeypatch, clean_env):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("GEMINI_API_KEY", "from-env")
    assert iig3d.api_key(None) == ("from-env", "env:GEMINI_API_KEY")


def test_explicit_key_wins(iig3d, tmp_path, monkeypatch, clean_env):
    (tmp_path / ".env").write_text("GEMINI_API_KEY=from-file\n")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("GEMINI_API_KEY", "from-env")
    assert iig3d.api_key("explicit") == ("explicit", "--api-key")


def test_parent_dotenv_ignored(iig3d, tmp_path, monkeypatch, clean_env):
    (tmp_path / ".env").write_text("GEMINI_API_KEY=parent\n")
    child = tmp_path / "child"
    child.mkdir()
    monkeypatch.chdir(child)
    with pytest.raises(iig3d.UsageError) as err:
        iig3d.api_key(None)
    assert str(err.value) == f"no API key: expected GEMINI_API_KEY in {child / '.env'} or the environment"


def test_key_value_never_in_source(iig3d, tmp_path, monkeypatch, clean_env):
    (tmp_path / ".env").write_text("GEMINI_API_KEY=supersecretvalue\n")
    monkeypatch.chdir(tmp_path)
    key, source = iig3d.api_key(None)
    assert key == "supersecretvalue" and "supersecretvalue" not in source


def test_parse_env_file(iig3d, tmp_path):
    env = tmp_path / ".env"
    env.write_text("A=1\n# c\nexport B = 'two'\nC=\"three\"\nbroken\n")
    assert iig3d.parse_env_file(env) == {"A": "1", "B": "two", "C": "three"}
    assert iig3d.parse_env_file(tmp_path / "missing") == {}
