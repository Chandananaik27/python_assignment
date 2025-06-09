import unittest
from src.min_max.util import min_max


class TestMinMax(unittest.TestCase):
    def test_min_max(self):
        # Test case 1: Minimum and maximum values in a 2x2 array
        default_matrix_1 = [[1, 2], [3, 4]]
        expect_out = 3
        self.assertEqual(min_max(default_matrix_1), expect_out)

        # Test case 2: Minimum and maximum values in a 3x3 array
        default_matrix_2 = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
        expect_out = 11
        self.assertEqual(min_max(default_matrix_2), expect_out)


        # Test case 3: Minimum and maximum values in a 1x1 array
        default_matrix_3 = [[14]]
        expect_out= 14
        self.assertEqual(min_max(default_matrix_3), expect_out)


if __name__ == '__main__':
    unittest.main()