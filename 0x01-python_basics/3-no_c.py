#!/usr/bin/python3
'''module: 3_no_c
'''


def no_c(s):
    '''
    returns s with all 'c' and 'C' removed
    '''
    return "".join([c for c in s if c != 'c' and c != 'C'])
