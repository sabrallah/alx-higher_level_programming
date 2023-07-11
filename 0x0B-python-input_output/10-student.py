#!/usr/bin/python3
"""
This module defines a Student class with public instance attributes and methods.
"""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes names contained in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if attrs is not None and isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
