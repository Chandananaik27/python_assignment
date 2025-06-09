import unittest
from unittest.mock import patch
from io import StringIO
from src.text_alignment.util import text_alignment

class TestTextAlignment(unittest.TestCase):
    def test_text_alignment(self):
        # Adjusted expected output with correct formatting (including spaces)
        expected_result = (
            "  H  \n"
            " HHH \n"
            "HHHHH\n"
            " HHH         HHH        \n"
            " HHH         HHH        \n"
            " HHH         HHH        \n"
            " HHH         HHH        \n"
            " HHHHHHHHHHHHHHH  \n"
            " HHHHHHHHHHHHHHH  \n"
            " HHH         HHH        \n"
            " HHH         HHH        \n"
            " HHH         HHH        \n"
            " HHH         HHH        \n"
            "            HHHHH \n"
            "             HHH  \n"
            "              H   \n"
        )

        # Redirect stdout to capture output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # Provide an input of 3
            with patch('builtins.input', return_value='3'):
                text_alignment()

        # Get the output and compare
        actual_output = fake_out.getvalue()
        self.assertEqual(actual_output, expected_result)

if __name__ == '__main__':
    unittest.main()

