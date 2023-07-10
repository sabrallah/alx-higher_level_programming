#!/usr/bin/python3
"""This is a module container function base_geometry
"""


class BaseGeometry:
    """A class with public instance methods area integer validator"""
    def area(self):
        """raise exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value is integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
