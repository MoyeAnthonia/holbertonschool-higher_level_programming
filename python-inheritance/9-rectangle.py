#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class inheriting from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Returns the area of the geometry"""
        return self.__width * self.__height

    def __str__(self):
        """Prints the area in a nice format"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
