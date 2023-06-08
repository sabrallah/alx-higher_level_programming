#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # get the arguments without the script name
    n = len(argv)  # get the number of arguments

    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))

    for i, arg in enumerate(argv, 1):  # loop through the arguments
        print("{}: {}".format(i, arg))  # print the position and the value
