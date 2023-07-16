#!/usr/bin/python3
"""
This is a module for the Rectangle class which inherits from the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """
    A class to represent a Rectangle.

    ...

    Attributes
    ----------
    id : int
        an identifier for the Rectangle, inherited from Base class
    width : int
        width of the Rectangle
    height : int
        height of the Rectangle
    x : int
        x-coordinate of the Rectangle
    y : int
        y-coordinate of the Rectangle

    Methods
    -------
    area():
        Returns the area of the Rectangle.

    update(*args, **kwargs):
        Updates the Rectangle attributes.

    display():
        Prints the Rectangle using the # symbol.

    __str__():
        Returns a string representation of the Rectangle.

    to_dictionary():
        Returns the dictionary representation of the Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructs all the necessary attributes for the Rectangle object.

        Parameters
        ----------
            width : int
                width of the Rectangle
            height : int
                height of the Rectangle
            x : int, optional
                x-coordinate of the Rectangle (default is 0)
            y : int, optional
                y-coordinate of the Rectangle (default is 0)
            id : int, optional
                an identifier for the Rectangle, inherited from Base class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Calculates and returns the area of the Rectangle.

        Returns
        -------
        int
            area of the Rectangle
        """
        return self.width * self.height

    def update(self, *args, **kwargs):
        """
        Updates Rectangle attribute using either positional arg or keyw arg.

        Parameters
        ----------
        *args :
            Variable length argument list.
        **kwargs :
            Arbitrary keyword arguments.
        """
        if args:
            listme = ['id', 'width', 'height', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, listme[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def display(self):
        """
        Prints the Rectangle using the # symbol.
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns
        -------
        str
            string representation of the Rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle.

        Returns
        -------
        dict
            dictionary representation of the Rectangle
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    @property
    def width(self):
        """
        Gets the width of the Rectangle.

        Returns
        -------
        int
            width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle.

        Parameters
        ----------
        value : int
            new width of the Rectangle
        """
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the Rectangle.

        Returns
        -------
        int
            height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle.

        Parameters
        ----------
        value : int
            new height of the Rectangle
        """
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """
        Gets the x-coordinate of the Rectangle.

        Returns
        -------
        int
            x-coordinate of the Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the Rectangle.

        Parameters
        ----------
        value : int
            new x-coordinate of the Rectangle
        """
        self.integer_validator2('x', value)
        self.__x = value

    @property
    def y(self):
        """
        Gets the y-coordinate of the Rectangle.

        Returns
        -------
        int
            y-coordinate of the Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the Rectangle.

        Parameters
        ----------
        value : int
            new y-coordinate of the Rectangle
        """
        self.integer_validator2('y', value)
        self.__y = value
