#!/usr/bin/python3
"""Defines a rectangle class."""

from models.base import Base

class Rectangle(Base):
    """Represent a rectangle."""
    def __init__(self, width, height, x = 0, y = 0, id=None):
        """Initialize a new Rectangle.
            Args:
                width (int): The width of the new Rectangle.
                height (int): The height of the new Rectangle.
                x (int): The x coordinate of the new Rectangle.
                y (int): The y coordinate of the new Rectangle.
                id (int): The identity of the new Rectangle.
            Raises:
                TypeError: If either of width or height is not an int.
                ValueError: If either of width or height <= 0.
                TypeError: If either of x or y is not an int.
                ValueError: If either of x or y < 0.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """ getter of width of Rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """ setter of width of Resctangle """
            if not isinstance(value, int):
                raise TypeError("weight must be an integer")
            if value < 0:
                raise ValueError("width must > 0")
            self.__width = value

        @property
        def height(self):
            """ getter of the height of Rectangle """
            return  self.__width

        @height.setter
        def height(self, value):
            """ setter of the height of Rectangle """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """ getter of x of Rectangle """
            return self.__x

        @x.setter
        def x(self, value):
            """ setter of x of Rectangle """
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must > 0")
            self.__x = value

        @property
        def y(self):
            """ getter of y of Rectangle """
            return self.__y

        @y.setter
        def y(self, value):
            """ setter of y of Rectangle """
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be > 0")
            self.__y = value
