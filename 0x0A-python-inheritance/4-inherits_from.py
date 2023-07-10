#!/usr/bin/python3
"""
    Function that checks if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class.
    """


def inherits_from(obj, a_class):
    """
    Function that checks if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
