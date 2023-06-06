#!/usr/bin/python3
def print_numbers():
    for i in range(100):
        if i < 99:
            print("{:02d}, ".format(i), end="")
        else:
            print("{:02d}".format(i))

if __name__ == "__main__":
    print_numbers()
