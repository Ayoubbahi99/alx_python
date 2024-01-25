#!/usr/bin/python3

"""Defines a class Base"""
class Base:
    __nb_objects = 0

    """Check if id is not None to assign the argument of the object to ID
        Or  increment __nb_objects and assign it to ID
    """
    def __init__(self, id=None):
        """Creates new instances of Base.

        Args:
            size: id of the Base.
        """
        if id != None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects