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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initialisation with args width and height'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        '''creates a square instance'''
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        '''returns rectangle with the char #'''
        sym = str(self.print_symbol)
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join([sym for i in range(self.__width)])
                for j in range(self.__height)]))

    def __repr__(self):
        '''return a string representation of the rectangle'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        if Rectangle.number_of_instances != 0:
            Rectangle.number_of_instances -= 1
