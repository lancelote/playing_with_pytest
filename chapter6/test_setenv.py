import os

import pytest

# module level fixture
# pytestmark = pytest.mark.usefixtures('clean_dir')


# for all tests
# content of pytest.ini
# [pytest]
# usefixtures = cleandir


@pytest.mark.usefixtures('clean_dir')
class TestDirectoryInit:

    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open('my_file', 'w') as my_file:
            my_file.write('hello')

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
