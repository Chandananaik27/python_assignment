import unittest
from src.string_formatting.util import string_formatting

class MyTestCase(unittest.TestCase):
    def test_string_format(self):
        # For k = 4, max binary = '100' → width = 3
        expected_output = (
            "  1   1   1   1\n"
            "  2   2   2  10\n"
            "  3   3   3  11\n"
            "  4   4   4 100\n"
        )
        self.assertEqual(string_formatting(4), expected_output)

    def test_string_format_invalid_input(self):
        self.assertEqual(string_formatting(0), "")

if __name__ == '__main__':
    unittest.main()
