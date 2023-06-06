#!/usr/bin/python3
for b in range(122, 96, -1):
    if b % 2:
        b = b - 32
    print("{:c}".format(b), end="")
