import unittest
from src.floor_ceil.util import floor_ceil_rint

class MyTestCase(unittest.TestCase):
    """The test case verifies the correctness of the floor_ceil_rint function from the util.py """
    def test_case_1(self):
        float_in = "1.1 2.2 3.3"
        expected_output = "(array([1.0, 2.0, 3.0]), array([2.0, 3.0, 4.0]), array([1.0, 2.0, 3.0]))"
        output = floor_ceil_rint(float_in)
        string_output = "(" + ", ".join([f"array({arr.tolist()})" for arr in output]) + ")"
        self.assertEqual(string_output, expected_output)


    """ensures that the function handles negative floats correctly"""
    def test_negative_floats(self):
        float_in = "-1.1 -2.2 -3.3"
        expected_output = "(array([-2. -3. -4.]), array([-1. -2. -3.]), array([-1. -2. -3.]))"
        output = floor_ceil_rint(float_in)
        string_output = "(" + ", ".join([f"array({arr})" for arr in output]) + ")"
        self.assertEqual(string_output, expected_output)


if __name__ == '__main__':
    unittest.main()