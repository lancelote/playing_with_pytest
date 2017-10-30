import unittest

import pytest


@pytest.mark.usefixtures('db_class')
class TestSample(unittest.TestCase):

    def test_db_attribute_is_set(self):
        assert hasattr(self, 'db')
