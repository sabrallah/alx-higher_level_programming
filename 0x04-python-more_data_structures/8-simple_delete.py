#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # use the pop method to remove the key/value pair if the key exists
    a_dictionary.pop(key, None)
    # return the updated dictionary
    return a_dictionary
