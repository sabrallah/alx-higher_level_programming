#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # use the sorted function to get a list of keys in alphabetic order
    sorted_keys = sorted(a_dictionary.keys())
    # loop through the sorted keys and print the key and value pair
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
