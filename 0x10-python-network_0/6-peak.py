#!/usr/bin/python3
"""my_peak-finding."""


def find_peak(list_of_integers):
    """Return the lowest peak from a list."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    my_peak = list_of_integers[mid]
    if my_peak > list_of_integers[mid - 1] and my_peak > list_of_integers[mid + 1]:
        return my_peak
    elif my_peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
