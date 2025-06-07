from collections import namedtuple
import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )
def named_tuple():
    num_students = int(input("Enter no. of students"))

    column_names = input("Enter the column name space-seperated").split()

    # Define the namedtuple for a row
    Row = namedtuple('Row', column_names)

    # Initialize variables to store the sum of marks and the index of the MARKS column
    total_marks = 0
    marks_index = -1

    # Find the index of the MARKS column
    for i, col_name in enumerate(column_names):
        if col_name == 'MARKS':
            marks_index = i
            break

    # Read the data for each student and calculate the sum of marks
    for _ in range(num_students):
        row_data = input().split()
        row = Row(*row_data)
        total_marks += int(row[marks_index])

    # Calculate the average marks
    average_marks = total_marks / num_students

    # Print the result with 2 decimal places
    logging.debug("{:.2f}".format(average_marks))