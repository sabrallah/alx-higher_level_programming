#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / pow(a, -b)
    elif b %2 == 0:
        return pow(a * a, b // 2)
    else:
        return a * pow(a, b - 1)
