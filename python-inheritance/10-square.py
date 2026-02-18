#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This inherits from rectangle"""
    def __init__(self, size):
        """Rectangle Class inheriting from 9-rectangle"""
        self.___size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
