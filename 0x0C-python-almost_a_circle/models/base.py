#!/usr/bin/python3
"""Module for the Base class"""


class Base:
    """Base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the Base class

        Args:
            id (int, optional): Assigns a specific id object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
