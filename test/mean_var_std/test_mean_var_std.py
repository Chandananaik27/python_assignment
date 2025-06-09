import unittest
from src.mean_var_std.util import calculate_statistics
from unittest.mock import patch


class TestCalculateStatistics(unittest.TestCase):
    def test_calculate_statistics(self):
        # Test with a simple 2x3 array
        with patch('builtins.input', side_effect=["2 3", "1 2 3 4 5 6"]):
            mean_rows, var_columns, std_dev = calculate_statistics()

        # Expected values for the input array [[1, 2, 3], [4, 5, 6]]
        expected_mean_rows = [2.0, 5.0]
        expected_var_columns = [2.0, 2.0, 2.0]
        expected_std_dev = 1.70782512766

        # Asserting the calculated values match the expected values
        self.assertEqual(mean_rows.tolist(), expected_mean_rows)
        self.assertEqual(var_columns.tolist(), expected_var_columns)
        self.assertAlmostEqual(std_dev, expected_std_dev, places=11)

    def test_calculate_statistics_single_element(self):
        # Test with a single-element array
        with patch('builtins.input', side_effect=["1 1", "42"]):
            mean_rows, var_columns, std_dev = calculate_statistics()

        # Expected values for the input array [[42]]
        expected_mean_rows = [42.0]
        expected_var_columns = [0.0]
        expected_std_dev = 0.0

        # Asserting the calculated values match the expected values
        self.assertEqual(mean_rows.tolist(), expected_mean_rows)
        self.assertEqual(var_columns.tolist(), expected_var_columns)
        self.assertAlmostEqual(std_dev, expected_std_dev, places=11)


if __name__ == '__main__':
    unittest.main()