import numpy
import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def calculate_statistics():
    n, m = map(int, input("Enter the dimensions of the array (space-separated): ").split())

    print("Enter the elements of the array:")
    elements = list(map(int, input().split()))
    my_array = numpy.array(elements).reshape(n, m)

    mean_along_rows = numpy.mean(my_array, axis=1)
    variance_along_columns = numpy.var(my_array, axis=0)
    standard_deviation = numpy.std(my_array)
    rounded_std_dev = round(standard_deviation, 11)

    logging.debug(f"Mean along rows:, {mean_along_rows}")
    logging.debug(f"Variance along columns:, {variance_along_columns}")
    logging.debug(f"Standard Deviation:, {standard_deviation}")

    return mean_along_rows, variance_along_columns, rounded_std_dev
