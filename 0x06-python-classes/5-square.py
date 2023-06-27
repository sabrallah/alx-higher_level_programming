#!/usr/bin/python3
"""
Module documentation: Square class
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance
        Args:
            size (int): The size of the square (default 0)
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square
        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        Args:
            value (int): The size of the square
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square
        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#'
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
