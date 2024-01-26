#!/usr/bin/python3
"""Import Rectangle class from rectangle file"""
from rectangle import Rectangle

class Square(Rectangle):
    """The Square class inherits from the Rectangle class""" 

    def __init__(self, size, x=0, y=0, id=None):
        """"Constructor for the Square class
             Calls the constructor of the base class (Rectangle) with the provided arguments
             Size is used for both width and height since Square has equal sides
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the Square object
        Displays information about the Square, including its ID, position, and size
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}"
