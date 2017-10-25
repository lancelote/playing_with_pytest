import pytest


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Disable http requests from requests library."""
    monkeypatch.delattr('requests.sessions.Session.request')
