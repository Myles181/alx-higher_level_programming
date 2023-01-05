#!/usr/bin/python3
'''Rectangle class module'''


class Rectangle:
    '''
    Defines a Rectangle

    __init__(self, width, height)
    args:
        width (int)
        height (int)
    '''

    def __init__(self, width=0, height=0):
        '''Initialisation with args width and height'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''property getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width attribute'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''property getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height attribute'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''area of rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        '''returns rectangle with the char #'''
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))
