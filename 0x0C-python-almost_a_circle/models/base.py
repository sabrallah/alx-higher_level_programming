#!/usr/bin/python3
"""
This module defines the `Base` class.
"""

import json


class Base:
    """
    This is the Base class that other classes will inherit from.

    Class Attributes:
        __nb_objects (int): The number of instances created from this class.

    Instance Attributes:
        id: The unique identifier for each instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): The unique identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        """
        Validates if the given value is a positive integer.

        Args:
            name (str): The name of the attribute to validate.
            value (int): The value of the attribute to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    def integer_validator2(self, name, value):
        """
        Validates if the given value is a non-negative integer.

        Args:
            name (str): The name of the attribute to validate.
            value (int): The value of the attribute to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not >= 0.
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): The list of dictionaries to convert.

        Returns:
            str: JSON string repr list dict or empty list if input is None.
        """
        return json.dumps(list_dictionaries or [])

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): The JSON string to convert.

        Returns:
            list: list of dict, or empty list if the input json_string is None.
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a list of instances to a file.

        Args:
            list_objs (list): The list of instances to write to file.
        """
        if list_objs:
            j = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        else:
            j = '[]'
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(j)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of the class with all attributes set.

        Args:
            dictionary (dict): A dictionary of attribute names and values.

        Returns:
            The new instance with all attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Reads from a JSON file and returns a list of instances.

        Returns:
            list: list instance. If file does not exist, returns an empty list.
        """
        try:
            filename = cls.__name__ + '.json'
            with open(filename, mode='r') as f:
                d = cls.from_json_string(f.read())
            return [cls.create(**x) for x in d]
        except FileNotFoundError:
            return []
