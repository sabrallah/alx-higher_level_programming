#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    # use map to apply a lambda function that squares each element of each row
    return (list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix)))
