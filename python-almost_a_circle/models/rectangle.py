#!/usr/bin/python3
"""Defines a class Rectangle based on base.py"""

Base = __import__('base').Base

class Rectangle(Base):    

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates new instances of Rectangle.

        Args:
            id (int, optional): Identity of each instance. Getting from Base class.
            width (int): Give the width of each rectangle.
            height (int): Give the height of each rectangle.
            x (int): Give the place of the rectangle.
            y (int): Give the place of the rectangle.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


    @property
    def width(self):
        """Getter method for width."""
        return self.__width
    
    @width.setter
    def width(self, width):
        """setter method for width."""
        self.__width = width
    
    @property
    def height(self):
        """Getter method for height."""
        return self.__height
    
    @height.setter
    def width(self, height):
        """setter method for height."""
        self.__height = height
    
    @property
    def x(self):
        """Getter method for x."""
        return self.__x
    
    @x.setter
    def x(self, x):
        """setter method for x."""
        self.__x = x

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def width(self, y):
        """setter method for y."""
        self.__y = y