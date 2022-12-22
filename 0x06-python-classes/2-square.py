#!/usr/bin/python3
'''
Class Square that defines a square
'''


class Square:
    '''
    __init__ method for parameters of square
    args:
        param1 (int): describe the size in units
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
