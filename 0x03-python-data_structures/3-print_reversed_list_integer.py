#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # loop through the list items in reverse order
    for number in reversed(my_list):
        # print each number using str.format()
        print("{:d}".format(number))
