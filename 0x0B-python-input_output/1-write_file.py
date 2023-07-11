#!/usr/bin/python3
"""Module for write_file function."""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and returns the number of
    characters written.

    Args:
        filename (str): Name of the file to write to.
        text (str): Text to be written to the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
