#!/usr/bin/python3
'''module: 9-print_sorted_dictionary'''


def print_sorted_dictionary(my_dict):
    '''
    prints dictionary in order, sorted by keys, which are
    guaranteed to be strings
    '''
    newD = sorted(my_dict.items())
    for item in newD:
        print("{}: {}".format(item[0], item[1]))
