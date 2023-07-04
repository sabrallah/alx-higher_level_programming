#!/usr/bin/python3
"""Module containing the LockedClass."""


class LockedClass:
    """A class that only allows creating a 'first_name' instance attribute."""

    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(name))
