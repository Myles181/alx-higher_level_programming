#!/usr/bin/python3
'''
A class that defines a Rectangle
'''
class Rectangle:
    '''Representaion of a Rectangle'''
    def __init__(self, width = 0, height = 0):
        '''Initialize the width and height'''
        self.width = width
        self.height = height

        @property
        def width(self):
            ''' getter for Private Instance attribute width'''
            return self.__width

        @width.setter
        def width(self, value):
            ''' setter for the privateinstance attribute width'''
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            ''' getter for the private attribute height'''
            return self.__height

        @height.setter
        def height(self, value):
            ''' setter for the private attribute height'''
            if not isinstance(height, int):
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
