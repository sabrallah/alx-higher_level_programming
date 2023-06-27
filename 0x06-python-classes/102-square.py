#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if two squares are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares are not equal in area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare if one square is greater in area than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if one square is greater than or equal in area other."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compare if one square is less in area than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if one square is less than or equal in area to the other."""
        return self.area() <= other.area()
