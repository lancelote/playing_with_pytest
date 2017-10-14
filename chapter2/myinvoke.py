"""Calling pytest from Python script.
"""

import pytest


class MyPlugin:
    # noinspection PyMethodMayBeStatic
    def pytest_sessionfinish(self):
        print('*** test run reporting finishing')


pytest.main(['-qq'], plugins=[MyPlugin()])
