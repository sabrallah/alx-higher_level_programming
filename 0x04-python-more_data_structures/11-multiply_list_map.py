#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    # use map to apply a lambda function that multiplies each element by number
    return list(map(lambda x: x * number, my_list))
