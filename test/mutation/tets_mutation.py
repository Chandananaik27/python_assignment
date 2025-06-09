import logging
import unittest
from src.mutations.util import mutate_string

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(mutate_string("chandu",2,"g"),"chgndu")
    def test_case_2(self):
        self.assertEqual(mutate_string("abcd",1,"k"),"akcd")
    def test_case_3(self):
        self.assertEqual(mutate_string("manu",1,"u"),"munu")
if __name__ == '__main__':
    unittest.main()