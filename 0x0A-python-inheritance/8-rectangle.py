#!/usr/bin/python3
"""
This module contains the Rectangle class that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with width and height
        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
