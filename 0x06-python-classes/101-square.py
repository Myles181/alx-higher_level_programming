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
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int)\
                or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def position(self):
        '''Return (tuple): position'''
        return self.__position

    @property
    def size(self):
        '''Return(int): size'''
        return self.__size

    @position.setter
    def position(self, value):
        '''
        Set value for private attribute

        args:
            param1 (tuple): possition, (len): 2 (int)
        '''
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int)\
                or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        '''
        Set value for private attribute size

        args:
            param1 (int): size
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''
        Return(int): area of square
        '''
        x = int(self.__size)**2
        return int(x)

    def my_print(self):
        '''
        prints square in stdout with character #
        '''
        if self.__size == 0:
            print()
        else:
            if self.__position[1] != 0:
                for i in range(self.__position[1]):
                    print()

            for i in range(self.__size):
                if self.__position[0] != 0:
                    for k in range(self.__position[0]):
                        print(end=" ")

                for j in range(self.__size):
                    print('#', end='')
                print()

    def __str__(self):
        '''
        prints square in stdout with character #
        '''
        if self.__size != 0:
            if self.__position[1] != 0:
                for i in range(self.__position[1]):
                    print('')

            for i in range(self.__size):
                if self.__position[0] != 0:
                    for k in range(self.__position[0]):
                        print(end=" ")

                for j in range(self.__size):
                    print('#', end='')
                if i != self.__size - 1:
                    print('')
        return ("")
