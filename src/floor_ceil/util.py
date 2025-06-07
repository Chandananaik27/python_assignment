import numpy
import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )
def floor_ceil_rint():
    float_in = input("Enter the float value seperated  by space: ")

    float_list=[float(i) for i in float_in.split()]
    my_array=numpy.array([float_list])
    logging.debug(f"Floor,{numpy.floor(my_array)[0]}")
    logging.debug(f"Ceil,{numpy.ceil(my_array)[0]}")
    logging.debug(f"Rint,{numpy.rint(my_array)[0]}")
    return numpy.floor(my_array)[0], numpy.ceil(my_array)[0], numpy.rint(my_array)[0]