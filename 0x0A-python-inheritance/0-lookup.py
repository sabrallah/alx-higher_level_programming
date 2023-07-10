#!/usr/bin/python3
"""
The lookup container functions
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to get the attributes and methods.

    Returns:
        list: A list containing the attributes and methods of the given object.
    """
    return dir(obj)
