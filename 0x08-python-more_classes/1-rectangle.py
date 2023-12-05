#!/usr/bin/python3
class Rectangle:
    """
    Rectangle that defines a rectangle
    Params: width, height
    ...

    Attributes
    ---------
    height : int
        height of the rectangle
    width: int
        width of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        width: int
            must be >= 0
        height: int
            must be >=0
        """
        self.__height = height
        self.__width = width
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width
    
    @width.setter 
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
        