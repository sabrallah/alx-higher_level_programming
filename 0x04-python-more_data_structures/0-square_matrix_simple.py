#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # create a new empty matrix
    new_matrix = []
    # loop through each row of the input matrix
    for row in matrix:
        # create a new empty row
        new_row = []
        # loop through each element of the row
        for x in row:
            # append the square of the element to the new row
            new_row.append(x ** 2)
        # append the new row to the new matrix
        new_matrix.append(new_row)
    # return the new matrix
    return new_matrix
