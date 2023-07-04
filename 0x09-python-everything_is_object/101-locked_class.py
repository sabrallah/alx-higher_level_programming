#!/usr/bin/python3
"""Define locked class."""


class LockedClass:
    """
    Prevent the user LockedClass attributes
    for anything attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
