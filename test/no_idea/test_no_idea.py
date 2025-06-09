import sys
import unittest
from src.no_idea.util import calculate_happiness
from io import StringIO
from unittest.mock import patch


class TestCalculateHappiness(unittest.TestCase):
    def setUp(self):
        self.saved_stdin = sys.stdin
        self.mock_stdin = StringIO()

    def tearDown(self):
        sys.stdin = self.saved_stdin

    def test_happiness_with_same_lists(self):
        # Test when A and B are same as b
        input_values = "3\n1 2 3\n3 2 1\n3 2 1\n"
        expected_result = 0
        with patch('sys.stdin', self.mock_stdin):
            self.mock_stdin.write(input_values)
            self.mock_stdin.seek(0)
            self.assertEqual(calculate_happiness(), expected_result)

    def test_happiness_with_different_lists(self):
        # Test when A and B are different from b
        input_values = "3\n1 2 3\n3 2 1\n1 2 3\n"
        expected_result = 0
        with patch('sys.stdin', self.mock_stdin):
            self.mock_stdin.write(input_values)
            self.mock_stdin.seek(0)
            self.assertEqual(calculate_happiness(), expected_result)


if __name__ == '__main__':
    unittest.main()