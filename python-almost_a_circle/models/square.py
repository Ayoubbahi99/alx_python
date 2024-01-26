#!/usr/bin/python3
"""Import Rectangle class from rectangle file"""



from rectangle import Rectangle

"""Square Class"""
class Square(Rectangle):
    """The Square class inherits from the Rectangle class

     Attributes:
        width (int): width of rectangle.
        height (int): height of rectangle.
        x (int): x.
        y (int): y.   
    """ 

    def __init__(self, size, x=0, y=0, id=None):
        """"Constructor for the Square class
            Get them(Properties) all from Rectangle Class
        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): Identity number of rectangle. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print info of a Square.

        Returns:
            print id, x, y, width, and height of each rectangle.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}"
