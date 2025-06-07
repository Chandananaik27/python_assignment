import numpy
import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )

def min_max(default_matrix=[[14]]):
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter no. of cols: "))
    if default_matrix is None:
        arr=[]
        for i in range(rows):
            row=[]
            for j in range(cols):
               cols_input= int(input(f"enter the value for row {i+1} and col {j+1}: "))
               row.append(cols_input)
            arr.append(row)
    else:
        arr=default_matrix

    # minimum of array
    min_axis0=numpy.min(arr, axis=0)# column comparison
    min_axis_1=numpy.min(arr, axis=1)# row comparison
    min_axis_none=numpy.min(arr, axis=None)# none_comprison
    min_axis=numpy.min(arr)

    # max of array
    max_axix_0 = numpy.max(arr, axis=0)
    max_axis_1 = numpy.max(arr, axis=1)
    max_axis_none=numpy.max(arr, axis=None)
    max_axis = numpy.max(arr)

    # The max of min along axis_1
    logging.debug(f"The max of min along axis_1 {numpy.max(min_axis_1, axis=0)}: ")
    return numpy.max(min_axis_1, axis=0)