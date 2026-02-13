#!/usr/bin/python3
"""a private square attribute"""


class Square:
    """initial class"""
    def __init__(self, size=0):
        """private square attribute"""
        self.__size = size

    """Getter to retrieve the size"""
    @property
    def size(self):
        """Returns the size"""
        return self.__size

    """Setter to get real value"""
    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Prints the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        size = int(self.__size)
        if size == 0:
            print()
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
