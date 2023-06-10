#!/usr/bin/python3
def element_at(my_list, idx):
    # check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return None
    # use list indexing to get the element at idx
    return my_list[idx]
