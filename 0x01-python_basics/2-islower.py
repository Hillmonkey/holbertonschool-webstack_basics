#!/usr/bin/python3

'''
module contains islower() function
'''


def islower(ch):
    '''
    accepts a character, if it is lower case, return true
    else return false
    '''
    return True if ord(ch) >= ord('a') and ord(ch) <= ord('z') else False
