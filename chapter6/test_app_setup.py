"""

pytest -v test_app_setup.py

...
chapter6/test_app_setup.py::test_smtp_exists[smtp.gmail.com] PASSED
chapter6/test_app_setup.py::test_smtp_exists[mail.python.org] PASSED
...
"""

import pytest


class App:
    def __init__(self, smtp):
        self.smtp = smtp


@pytest.fixture(scope='module', name='app')
def fixture_app(smtp_param):
    return App(smtp_param)


def test_smtp_exists(app):
    assert app.smtp
