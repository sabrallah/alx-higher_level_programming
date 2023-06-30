#!/usr/bin/python3
"""
    4-print_square Modules
"""


def print_square(size):
    """
        Print a squares with the character '#'

        Args:
            size: size lengths of the squar
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
