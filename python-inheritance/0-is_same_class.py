#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False."""
    if obj.isinstance(a_class):
        return True #return True as an isinstance
    else:
        return False #return False if is not an isinstance