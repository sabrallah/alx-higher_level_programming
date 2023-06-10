#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # loop through the list from the last element to the first
    for y in range(len(my_list) - 1, -1, -1):
        # print the current element using str.format()
        print("{:d}".format(my_list[y]))
