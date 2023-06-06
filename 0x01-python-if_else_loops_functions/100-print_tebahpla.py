#!/usr/bin/python3
for y in range(90, 64, -1):
    print(chr(y % 2 * 32 + y), end='')
