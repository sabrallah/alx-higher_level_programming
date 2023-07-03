#!/usr/bin/python3
"""Module for Rectangle class"""


class Rectangle:
    """Rectangle class with width and height attributes"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize width and height of the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_rows = [str(self.print_symbol) * self.width
                          for _ in range(self.height)]
        return "\n".join(rectangle_rows)

    def __repr__(self):
        """Return a string representation for recreating an instance"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
