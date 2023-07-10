#!/usr/bin/python3
"""
This module contains a class MyInt that inherits from int.

MyInt is a rebel. Its '==' and '!=' operators are inverted.
"""


class MyInt(int):
    """
    MyInt class that inherits from int.

    This class has inverted '==' and '!=' operators.
    """

    def __eq__(self, other):
        """
        Invert the '==' operator.

        Args:
            other: The other integer to compare.

        Returns:
            True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Invert the '!=' operator.

        Args:
            other: The other integer to compare.

        Returns:
            True if equal, False otherwise.
        """
        return super().__eq__(other)
