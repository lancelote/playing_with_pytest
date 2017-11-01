import unittest

import pytest


class TestSample(unittest.TestCase):

    @pytest.fixture(autouse=True, name='init_dir')
    def fixture_init_dir(self, tmpdir):
        tmpdir.chdir()
        tmpdir.join('sample_file.ini').write('# test data')

    def test_method(self):
        with open('sample_file.ini') as sample_file:
            content = sample_file.read()
        assert 'test data' in content
