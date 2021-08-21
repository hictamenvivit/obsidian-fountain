import pytest

from models import Vault


@pytest.fixture
def ChapterlessVault(monkeypatch):
    from models import Vault
    monkeypatch.setattr(Vault, "chapters", [])
    return Vault


class TestVault:

    def test_name_no_slash(self, ChapterlessVault):
        assert ChapterlessVault("/a/path").title == "path"

    def test_name_with_slash(self, ChapterlessVault):
        assert ChapterlessVault("/a/path/").title == "path"
