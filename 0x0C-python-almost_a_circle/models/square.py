#!/usr/bin/python3
"""
Module for managing geometric shapes, specifically squares.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Represents square with certain size, position defined by x and y coordinat.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the Square instance.

        Parameters:
            size (int): Side length of the square.
            x (int): The x-coordinate of the square's position. Defaults to 0.
            y (int): The y-coordinate of the square's position. Defaults to 0.
            id (int, optional): The unique identifier of square. Defaults None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a formatted string representation of the Square instance.

        Returns:
            str: String representation of the square.
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x,
                                              self.y, self.width))

    @property
    def size(self):
        """
        Property getter for the size of the square.

        Returns:
            int: The side length of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Property setter for the size of the square.

        Parameters:
            value (int): The new side length for the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square instance with new values.

        If args provided, they will interp the order 'id', 'size', 'x', 'y'.
        If kwargs provided, they used to update attrib of square by name.

        Parameters:
            *args (tuple): Ordered arguments to update attributes.
            **kwargs (dict): Keyword arguments to update attributes by name.
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Convert the Square instance to a dictionary.

        Returns:
            dict: dictionary repr square, with key 'id', 'x', 'size', and 'y'.
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
