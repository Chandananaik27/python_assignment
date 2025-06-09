import unittest
import logging
from src.second_maximum_in_list.util import second_maximum

logging.basicConfig(level=logging.DEBUG, format="%(message)s" )

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        num= 5
        Input_values=[3,2,6,5,4]
        Expected_output=5
        second_max= second_maximum(num,Input_values)
        logging.debug(f"The second max value is : {Expected_output}")
        self.assertEqual(second_max,Expected_output)

    def test_case_2(self):
        num= 7
        Input_values=[3,2,5,7,8,70,9]
        Expected_output=9
        second_max= second_maximum(num,Input_values)
        logging.debug(f"The second max value is : {Expected_output}")
        self.assertEqual(second_max,Expected_output)
    def test_case_3(self):
        num= 10
        Input_values=[3,2,6,5,4,1,9,8,7,10]
        Expected_output=9
        second_max= second_maximum(num,Input_values)
        logging.debug(f"The second max value is : {Expected_output}")
        self.assertEqual(second_max,Expected_output)

if __name__ == '__main__':
    unittest.main()