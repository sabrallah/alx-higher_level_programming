#!/usr/bin/python3

def uniq_add(my_list=[]):
    # create a set to store the unique elements
    unique_set = set()
    # loop through the list and add each element to the set
    for element in my_list:
        unique_set.add(element)
    # initialize a variable to store the sum
    sum = 0
    # loop through the set and add each element to the sum
    for element in unique_set:
        sum += element
    # return the sum
    return sum
