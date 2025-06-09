import unittest
from unittest.mock import patch
from io import StringIO
import logging

from src.collections_namedtuple.util import named_tuple  # Adjust path as needed


class TestNamedTuple(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        "3",                    # Number of students
        "ID MARKS NAME",        # Column names
        "1 90 Alice",           # Student 1
        "2 80 Bob",             # Student 2
        "3 70 Charlie"          # Student 3
    ])
    def test_named_tuple_average_marks(self, mock_input):
        with self.assertLogs(level='DEBUG') as log:
            named_tuple()
        # Find the last log message and check if it contains "80.00"
        self.assertTrue(any("80.00" in message for message in log.output))


if __name__ == '__main__':
    unittest.main()

