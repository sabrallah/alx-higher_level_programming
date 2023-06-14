#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # loop through a copy of the dictionary keys
    for key in list(a_dictionary.keys()):
        # check if the value of the key matches the value to be deleted
        if a_dictionary[key] == value:
            # delete the key from the dictionary
            del a_dictionary[key]
    # return the modified dictionary
    return a_dictionary
