import unittest
from src.calender_module.util import calendar_module

class MyTestCase(unittest.TestCase):
    '''Test the correct date and input'''
    def test_case_1(self):
        date_str= "01-02-2000"
        actual_output=calendar_module(date_str)
        expected_output= "Sunday"
        self.assertEqual(actual_output, expected_output)  # add assertion here


    '''Testcase for different month ad year'''
    def test_case_2(self):

        date_str = "12-02-2015"
        actual_output = calendar_module(date_str)
        expected_output ="Wednesday"
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()