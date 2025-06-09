import unittest
from unittest.mock import patch
from src.mail.util import is_valid_email, fun


class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        # Test a valid email address
        self.assertTrue(is_valid_email("example@email.com"))
    def test_invalid_email(self):
        # Test an invalid email address
        self.assertFalse(is_valid_email("invalid.email.com"))



if __name__ == '__main__':
    unittest.main()