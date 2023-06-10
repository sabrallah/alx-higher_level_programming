#!/usr/bin/python3

def no_c(my_string):
    # initialize an empty string
    result = ""
    # loop through each character in my_string
    for char in my_string:
        # if the character is not c or C, append it to result
        if char not in "cC":
            result += char
    # return result
    return result
