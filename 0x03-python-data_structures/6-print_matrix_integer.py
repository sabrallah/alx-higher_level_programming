#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # check if matrix is empty or None
    if not matrix or not matrix[0]:
        print()
        return
    # loop through each row in matrix
    for row in matrix:
        # loop through each element in row except the last one
        for i in range(len(row) - 1):
            # print element with space after it, formatted as integer
            print("{:d}".format(row[i]), end=" ")
        # print last element of row with newline after it, formatted as integer
        print("{:d}".format(row[-1]))
