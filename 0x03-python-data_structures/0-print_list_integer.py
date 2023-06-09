#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # loop through the list
    for i in my_list:
        # use str.format() to print each integer
        print("{:d}".format(i))
