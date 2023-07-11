#!/usr/bin/python3
"""
This module contains the function `from_json_string`.

The purpose of the function is to return a Python data structure
represented by a given JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns a Python object (data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
