#!/usr/bin/python3
'''
Class Square that defines a square
'''


class Square:
    '''
    __init__ method for parameters of square
    args:
        param1 (int): size
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        '''
        Return(int): size
        '''
        return self.__size

    @size.setter
    def size(self, size):
        '''
        Set value for private attribute size

        args:
            param1 (int): size
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''
        Return(int): area of square
        '''
        x = int(self.__size)**2
        return int(x)
