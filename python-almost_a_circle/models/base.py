#!/usr/bin/python3

class Base:
    """Class that defines properties of Base.

     Attributes:
        id (int): Identity of each instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Creates new instances of Base.

        Args:
            id (int, optional): Identity of each instance. Defaults to None.
        """
        if id is not None:
            # If an ID is provided, use it
            self.id = id
        else:
            # If no ID is provided, increment __nb_objects and assign the new value to the instance's ID
            Base.__nb_objects += 1
            self.id = Base.__nb_objects