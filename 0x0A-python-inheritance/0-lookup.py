#!/usr/bin/python3

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to get the attributes and methods.

    Returns:
        list: A list containing the attributes and methods of the given object.
    """
    return dir(obj)
