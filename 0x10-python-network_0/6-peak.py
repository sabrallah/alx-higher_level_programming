#!/usr/bin/python3
"""peak-finding."""


def find_peak(list_of_integers):
    """Return the lowest peak from a list."""
    if list_of_integers == []:
        return None

    isize = len(list_of_integers)
    if isize == 1:
        return list_of_integers[0]
    elif isize == 2:
        return max(list_of_integers)

    imid = int(isize / 2)
    peak = list_of_integers[imid]
    if peak > list_of_integers[imid - 1] and peak > list_of_integers[imid + 1]:
        return peak
    elif peak < list_of_integers[imid - 1]:
        return find_peak(list_of_integers[:imid])
    else:
        return find_peak(list_of_integers[imid + 1:])
