#!/usr/bin/python3

def weight_average(my_list=[]):
    # check if the list is empty
    if not my_list:
        # return 0
        return 0
    """initialize a variable to store
        the sum of the products of scores and weights"""
    sum_product = 0
    # initialize a variable to store the sum of the weights
    sum_weight = 0
    # loop through the tuples in the list
    for score, weight in my_list:
        # multiply the score and weight and add to the sum_product
        sum_product += score * weight
        # add the weight to the sum_weight
        sum_weight += weight
    """ calculate the weighted average
        by dividing the sum_product by the sum_weight"""
    weighted_average = sum_product / sum_weight
    # return the weighted average
    return weighted_average
