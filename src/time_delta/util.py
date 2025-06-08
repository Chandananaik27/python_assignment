import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )

from datetime import datetime


# Complete the time_delta function below.
def time_delta():
    t = int(input("Enter the number of test cases: "))

    for t_itr in range(t):
        t1 = input("Enter datetime string 1: ")
        t2 = input("Enter datetime string 2: ")

    format_str = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, format_str)
    dt2 = datetime.strptime(t2, format_str)

    time_diff_seconds = abs((dt1 - dt2).total_seconds())
    logging.debug(int(time_diff_seconds))
    return int(time_diff_seconds)