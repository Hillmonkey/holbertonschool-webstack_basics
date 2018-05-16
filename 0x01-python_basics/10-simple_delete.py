#!/usr/bin/python3

'''module: 10-simple_delete'''


def simple_delete(my_dict, key=""):
    '''
    delete key from my_dict
    '''
    ret = my_dict.get(key)
    if ret is not None:
        del my_dict[key]
    return my_dict
