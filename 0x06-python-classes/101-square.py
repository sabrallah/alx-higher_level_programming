#!/usr/bin/python3
"""
This module contains the Square class
"""


class Square:
    """
    A class named Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance

        Args:
            size (int): The size of the square (default: 0)
            position (tuple): The position of the square (default: (0, 0))
        """
        self.size = size
        self.position = position

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
            value (int): The new size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square

        Returns:
            tuple: The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square

        Args:
            value (tuple): The new position of the square

        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#'

        If the size is 0, it prints an empty line.
        The position is considered using spaces.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square

        Returns:
            str: The square represented by '#' characters
        """
        if self.__size == 0:
            return ""

        square_lines = []
        for _ in range(self.__position[1]):
            square_lines.append("\n")

        for _ in range(self.__size):
            square_lines.append(" " * self.__position[0])
            square_lines.append("#" * self.__size)
            square_lines.append("\n")

        return "".join(square_lines)


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
