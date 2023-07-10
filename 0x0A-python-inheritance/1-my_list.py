#!/usr/bin/python3
"""
This module contains the MyList class inherits the built-in list class
and provides a method to print list ascending order.
"""


class MyList(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        sorted_list = sorted(self)
        print(sorted_list)
