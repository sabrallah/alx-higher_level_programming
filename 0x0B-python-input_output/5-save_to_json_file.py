#!/usr/bin/python3
"""
This module contains a function that writes an object to a text file,
using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj (object): The object to be written to the file.
        filename (str): The name of the file where the object will be written.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
