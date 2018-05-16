#!/usr/bin/python3
'''module: 13-add_integer'''


def add_integer(a, b):
    '''
    adds a and b, has some protection for type errors
    '''
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
