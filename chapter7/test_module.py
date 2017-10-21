import os.path


def get_ssh():  # pseudo application code
    return os.path.join(os.path.expanduser('~admin'), '.ssh')


def test_get_ssh(monkeypatch):
    monkeypatch.setattr(os.path, 'expanduser', lambda path: '/abc')
    assert get_ssh() == '/abc/.ssh'
