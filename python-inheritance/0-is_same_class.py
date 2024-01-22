#!/usr/bin/python3

"""Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False."""
def is_same_class(obj, a_class):
    if obj.isinstance(a_class):
        return True #return True as an isinstance
    else:
        return False #return False if is not an isinstance