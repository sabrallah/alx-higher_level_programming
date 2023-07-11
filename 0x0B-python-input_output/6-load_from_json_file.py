#!/usr/bin/python3
"""This module defines a function that creates an object from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The resulting object.
    """
    with open(filename, 'r') as f:
        return json.load(f)
