#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # create a new list to store the result
    new_list = []
    # loop through the original list
    for element in my_list:
        # if the element matches the search value,
        # append the replace value to the new list
        if element == search:
            new_list.append(replace)
        # otherwise, append the element itself to the new list
        else:
            new_list.append(element)
    # return the new list
    return new_list
