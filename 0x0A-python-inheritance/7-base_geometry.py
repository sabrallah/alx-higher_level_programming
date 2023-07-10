#!/usr/bin/python3
"""A class representing a basic geometry object."""


class BaseGeometry:
    """A class representing a basic geometry object."""

    def area(self):
        """Calculate the area of the geometry object.

        Raises:
            Exception: Always raised since area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the value is a positive integer.

        Args:
            name (str): The name of the value being checked.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
