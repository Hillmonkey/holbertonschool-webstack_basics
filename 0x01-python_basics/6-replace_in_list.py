#!/usr/bin/python3

'''module: 6-replace_in_list'''


def replace_in_list(my_list, idx, element):
    '''
    replace element at idx with new element
    '''
    if idx not in range(len(my_list)):
        return my_list
    my_list[idx] = element
    return my_list
