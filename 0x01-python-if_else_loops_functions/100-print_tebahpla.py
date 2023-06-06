#!/usr/bin/python3
print(''.join(chr(i % 2 * 32 + i) for i in range(90, 64, -1)), end='')
