#!/usr/bin/python3
"""
This module defines the function add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    Adds 2 integers a and b.

    Args:
        a (int or float): The first integer or float to add.
        b (int or float): The second integer or float to add. Defaults to 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an int or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
