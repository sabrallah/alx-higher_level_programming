#!/usr/bin/python3
def uppercase(str):
    for y in str:
        if ord("a") <= ord(y) <= ord("z"):
            y = chr(ord(y) - 32)
        print("{:s}".format(y), end="")
    print()
