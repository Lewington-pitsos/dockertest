import unittest
from lol import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)
        
    def test_add_fail(self):
        self.assertEqual(add(2, 2), 2)