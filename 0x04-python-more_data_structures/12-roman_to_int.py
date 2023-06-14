#!/usr/bin/python3

def roman_to_int(roman_string):
    # check if the roman_string is a string and not None
    if not isinstance(roman_string, str) or roman_string is None:
        # return 0
        return 0
    # create a dictionary to store the values of each roman numeral
    roman_values =\
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # initialize a variable to store the result
    result = 0
    # loop through the characters of the roman_string from left to right
    for i in range(len(roman_string)):
        # get the value of the current character
        current = roman_values[roman_string[i]]
        # check if we are not at the last character
        # and the next character is larger than the current one
        if i < len(roman_string) - 1 \
                and roman_values[roman_string[i + 1]] > current:
            # subtract the current value from the result
            result -= current
        else:
            # add the current value to the result
            result += current
    # return the result
    return result
