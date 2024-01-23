#!/usr/bin/python3
"""Defines a class BaseGeometry based on 7-rectangle.py"""



Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """Class Square.
    """

    def __init__(self, size):
        """Initialize a square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("width", size)
        self.__size = size
