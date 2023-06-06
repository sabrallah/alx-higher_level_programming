#!/usr/bin/python3

result = ""

for i in range(26):
    if i % 2 == 0:
        result += chr(122 - i)
    else:
        result += chr(90 - i)

print(result, end="")
