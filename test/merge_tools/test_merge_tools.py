import unittest
import logging
from src.merge_the_tools.util import merge_tools

# Set up the logging configuration
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# Define a test case class
class TestMergeTools(unittest.TestCase):
    def test_case_1(self):
        input_string = "AABCAAADA"
        k = 3
        expected_output = "AB\nCA\nAD\n"
        output = merge_tools(input_string, k)
        self.assertEqual(output, expected_output)
    def test_case_2(self):
        input_string = "bbcgfghjh"
        k = 3
        expected_output = "bc\ngf\nhj\n"
        output = merge_tools(input_string, k)
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()