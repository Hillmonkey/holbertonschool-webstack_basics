#!/usr/bin/python3
'''module: 11-safe_print_division'''


def safe_print_division(a, b):
    '''
    assume a & b are integers, return a / b or None
    in case of div by zero error
    '''
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        print("Inside result: {}".format(c))
        return c
