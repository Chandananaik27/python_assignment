import numpy as np
import logging
logging.basicConfig(level=logging.DEBUG,format="%(message)s" )

def linear_algebra(matrix):
    # Convert the list of lists into a NumPy array
    matrix = np.array(matrix)

    # Calculate the determinant of the matrix
    determinant = np.linalg.det(matrix)

    # Round the determinant to 2 decimal places
    determinant = round(determinant, 2)

    # Return the determinant

    return determinant


def main():
    n = int(input("Enter the size of the square matrix: "))

    # Read the elements of the square matrix
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)

    # Call the function to calculate determinant
    determinant = linear_algebra(matrix)
    # Print the determinant
    logging.debug(f"Determinant:{determinant}")