#Python - Inheritance


_ 0. Exact same object
    * Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

        * Prototype: def is_same_class(obj, a_class):
        * are not allowed to import any module

_ 1. Same class or inherit from
    * Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

        * Prototype: def is_kind_of_class(obj, a_class):
        * You are not allowed to import any module

_ 2. Only sub class of
    * Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

    * Prototype: def inherits_from(obj, a_class):
    * You are not allowed to import any module
_ 3. Geometry module
    * Write an empty class BaseGeometry.
        *You are not allowed to import any module

_ 4. Improve Geometry
    * Write a class BaseGeometry (based on 3-base_geometry.py).

        * Public instance method: def area(self): that raises an Exception with the message area() is not implemented
        * You are not allowed to import any module

_ 5. Integer validator
    * Public instance method: def area(self): that raises an Exception with the message area() is not implemented
    * Public instance method: def integer_validator(self, name, value): that validates value:
        * you can assume name is always a string
        * if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
        * if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
_ 6. Rectangle
    * Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).

    * Instantiation with width and height: def __init__(self, width, height):
        * width and height must be private. No getter or setter
        * width and height must be positive integers, validated by integer_validator

_7. Full rectangle
    * Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py). (task based on 6-rectangle.py)

        * Instantiation with width and height: def __init__(self, width, height)::
            * width and height must be private. No getter or setter
            * width and height must be positive integers validated by integer_validator
        * the area() method must be implemented
        * print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>