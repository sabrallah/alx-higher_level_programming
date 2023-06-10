#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # make a copy of my_list
    new_list = [x for x in my_list]
    # check if idx is valid
    if 0 <= idx < len(my_list):
        # assign element to new_list at idx position
        new_list[idx] = element
    # return new_list
    return new_list
