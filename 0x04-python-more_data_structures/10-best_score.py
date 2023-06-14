#!/usr/bin/python3

def best_score(a_dictionary):
    # check if the dictionary is empty or None
    if not a_dictionary:
        # return None
        return None
    # initialize a variable to store the best key
    best_key = None
    # initialize a variable to store the best value
    best_value = 0
    # loop through the keys and values of the dictionary
    for key, value in a_dictionary.items():
        # check if the value is greater than the best value
        if value > best_value:
            # update the best key and value
            best_key = key
            best_value = value
    # return the best key
    return best_key
