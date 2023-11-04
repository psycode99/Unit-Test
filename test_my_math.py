import my_math
import sys
import unittest

class TestAdd(unittest.TestCase):

    def test_add_integers(self):
        result = my_math.add(1, 2)
        assert result == 3

    def test_add_float(self):
        result = my_math.add(1.0, 2.1)
        assert result == 3.1

    @unittest.skip('Trial of skipping tests')
    def test_add_strings(self):
        result = my_math.add('hello ', 'world')
        assert result == 'hello world'

    @unittest.skipUnless(sys.platform.startswith('win'), 'requires windows')
    def test_add_on_windows(self):
        result = my_math.add(1, 2)
        assert result == 3