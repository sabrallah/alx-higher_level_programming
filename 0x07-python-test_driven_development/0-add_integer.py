#!/usr/bin/python3
""" 0-add_integers Modules """


def add_integer(a, b=98):
    """
    Adds twso integer

    Args:
        a: first integer
        b: second integer

    Returns:
        additions of two integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        new_a, new_b = int(a), int(b)
        return new_a + new_b
