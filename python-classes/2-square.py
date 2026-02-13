#!/usr/bin/python3
"""a private square attribute"""


class Square:
    """initial class"""
    def __init__(self, size=0):
        """private square attribute"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
