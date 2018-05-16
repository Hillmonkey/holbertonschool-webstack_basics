#!/usr/bin/python3

'''module: 5-args
'''

from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        print("0 argument.")
    else:
        if len(argv) == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(len(argv)))
        for idx, el in enumerate(argv[1:]):
            print("{}: {}".format(idx + 1, el))
