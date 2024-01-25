#!/usr/bin/python3

"""Import Base class from the base file"""
Base = __import__('base').Base

"""Defines a class Rectangle based on base.py"""
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

    """Getter method for width."""
    @property
    def width(self):
        """Return the width of rectangle."""
        return self.__width
    
    """setter method for width."""   
    @width.setter
    def width(self, width):
        """set width of rectangle to a new one."""
        self.__width = width
    
    """Getter method for height."""
    @property
    def height(self):
        """Get the height of rectangle."""
        return self.__height
    
    """setter method for height."""
    @height.setter
    def width(self, height):
        """set the height of a new value."""
        self.__height = height
    
    """Getter method for x."""
    @property
    def x(self):
        """Get the x value."""
        return self.__x
    
    """setter method for x."""
    @x.setter
    def x(self, x):
        """set the x value to a new one."""
        self.__x = x

    """Getter method for y."""
    @property
    def y(self):
        """Get the y value."""
        return self.__y

    """setter method for y."""
    @y.setter
    def width(self, y):
        """set the y value to a new one."""
        self.__y = y