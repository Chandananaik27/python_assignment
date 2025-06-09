import unittest
from unittest.mock import patch
from io import StringIO
from src.iterators.util import iterator

class TestIterator(unittest.TestCase):
    @patch('builtins.input', side_effect=['5', 'a a b a a', '3'])
    def test_iterator(self, mock_input):
        expected_output = 0.6
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = iterator()
            self.assertAlmostEqual(result, expected_output)
            self.assertAlmostEqual(float(fake_out.getvalue()), expected_output)

if __name__ == '__main__':
    unittest.main()