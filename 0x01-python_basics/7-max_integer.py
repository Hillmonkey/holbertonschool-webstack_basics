#!/usr/bin/python3
'''module: 7-max_integer
'''


def max_integer(my_list=[]):
    '''
    function: max_integer, returns largest integer in my_list
    '''
    if len(my_list) == 0:
        return None
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max
