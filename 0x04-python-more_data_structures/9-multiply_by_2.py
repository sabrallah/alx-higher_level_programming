#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # create a new dictionary to store the result
    new_dict = {}
    # loop through the keys and values of the original dictionary
    for key, value in a_dictionary.items():
        """ multiply the value by 2
        and assign it to the new dictionary with the same key """
        new_dict[key] = value * 2
    # return the new dictionary
    return new_dict
