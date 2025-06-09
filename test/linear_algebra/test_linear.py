import unittest
from io import StringIO
import sys
from src.linear_algebra.util import main,linear_algebra


class LinearAlgebraTestCase(unittest.TestCase):
    """test case for 2x2 matrix"""
    def test_determinant_2x2(self):
        input_matrix = 2
        expected_output = -2.0
        default_matrix = [
            [1.0, 2.0],
            [3.0, 4.0]
        ]
        actual_output= linear_algebra(default_matrix)
        self.assertEqual(actual_output, expected_output)
    """test case for 3x3 matrix"""
    def test_determinant_3x3(self):
        input_matrix = 3
        expected_output = 0.0
        default_matrix = [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ]
        actual_output = linear_algebra(default_matrix)
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()