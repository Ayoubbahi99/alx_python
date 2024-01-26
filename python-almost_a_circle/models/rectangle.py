#!/usr/bin/python3

"""Import Base class from the base file"""
from models.base import Base

"""Defines a class Rectangle based on base.py"""
class Rectangle(Base):
    """Defines a class Rectangle inherit from base.py file class Base
        create methods for all the instance attributes 
    """
  

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
        """set width of rectangle to a new one.
            
            Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format(width))
        if width < 0:
            raise ValueError("{} must be greater than 0".format(width))
        self.__width = width
    
    """Getter method for height."""
    @property
    def height(self):
        """Get the height of rectangle."""
        return self.__height
    
    """setter method for height."""
    @height.setter
    def height(self, height):
        """set the height of a new value.
            
            Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format(height))
        if height < 0:
            raise ValueError("{} must be greater than 0".format(height))
        self.__height = height
    
    """Getter method for x."""
    @property
    def x(self):
        """Get the x value."""
        return self.__x
    
    """setter method for x."""
    @x.setter
    def x(self, x):
        """set the x value to a new one.
            
            Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(x, int):
            raise TypeError("{} must be an integer".format(x))
        if x <= 0:
            raise ValueError("{} must be greater than 0".format(x))        
        self.__x = x

    """Getter method for y."""
    @property
    def y(self):
        """Get the y value."""
        return self.__y

    """setter method for y."""
    @y.setter
    def y(self, y):
        """set the y value to a new one.

            Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format(y))
        if y <= 0:
            raise ValueError("{} must be greater than 0".format(y))
        self.__y = y


    """The area of each rectangle"""
    def area(self):
        """Multiply height with the width to get the area."""
        return self.__height * self.__width

