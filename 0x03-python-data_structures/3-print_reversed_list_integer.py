#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # use reversed() function to get a reverse iterator of the list
    for i in reversed(my_list):
        # use str.format() to print integers
        print("{:d}".format(i))
