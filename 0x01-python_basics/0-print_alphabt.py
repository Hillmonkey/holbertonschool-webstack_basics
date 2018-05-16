#!/usr/bin/python3
'''
this module contains code to print all lower case characters, except two
'''

for i in range(ord('a'), ord('z')):
    if i != ord('q') and i != ord('e'):
        print("{}".format(chr(i)), end='')
