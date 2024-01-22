#!/usr/bin/python3

"""Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False."""

def is_same_class(obj, a_class):
    """Function that returns True or False
    Args:
        obj : object
        class : a_class
    Returns:
        True: is an instance
        False: is not an instance
    """
    if obj.isinstance(a_class):
        return True 
    else:
        return False