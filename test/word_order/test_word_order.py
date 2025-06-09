import unittest
from src.word_order.util import word_order

class TestWordOrder(unittest.TestCase):
    def test_word_order_with_three_words(self):
        # Arrange
        n = 3
        # Act
        result = word_order(n)
        # Assert
        self.assertIsNotNone(result)

    def test_word_order_with_five_words(self):
        # Arrange
        n = 5
        # Act
        result = word_order(n)
        # Assert
        self.assertIsNotNone(result)

    def test_word_order_with_empty_input(self):
        # Arrange
        n = 0
        # Act
        result = word_order(n)
        # Assert
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()