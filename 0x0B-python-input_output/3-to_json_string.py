#!/usr/bin/python3
"""Module to convert an object to a JSON string."""

import json


def to_json_string(my_obj):
    """
    Function to return the JSON representation of an object.
    Args:
        my_obj: An object that can be serialized.
    Returns:
        The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
