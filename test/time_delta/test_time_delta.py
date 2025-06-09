import unittest
import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )
from src.time_delta.util import time_delta
class MyTestCase(unittest.TestCase):
    def test_case3(self):
        t1 = "Sat 02 May 2015 19:54:36 +0530"
        t2 = "Fri 01 May 2015 13:54:36 -0000"
        expected_output= 88200
        self.assertEqual(time_delta(t1, t2), expected_output)# add assertion here
    def test_case2(self):
        t1 ="Sun 10 May 2015 13:54:36 -0700"
        t2 ="Sun 10 May 2015 13:54:36 -0000"
        expected_output= 25200
        self.assertEqual(time_delta(t1, t2), expected_output)

if __name__ == '__main__':
    unittest.main()