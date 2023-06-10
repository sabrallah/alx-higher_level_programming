#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Initialize the result tuple with zeros
    result = (0, 0)
    # Loop through the first two elements of each tuple
    for i in range(2):
        # Add the corresponding elements of the tuples if they exist
        if i < len(tuple_a):
            result = (result[0] + tuple_a[i], result[1])
        if i < len(tuple_b):
            result = (result[0], result[1] + tuple_b[i])
    # Return the result tuple
    return result
