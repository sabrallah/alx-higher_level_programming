#!/usr/bin/python3
"""Module with the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry objects."""

    def area(self):
        """Raises an exception, as this method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value of the given name.

        Args:
            name (str): The name of the value to be validated.
            value (int): The value to be checked for validity.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
