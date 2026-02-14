#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """The public variable"""
    number_of_instances = 0
    print_symbol = "#"
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize rectangle width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def print(self):
        """Prints the rectangle"""
        if self.height == 0 or self.width == 0:
            return ""
        for i in range(self.height):
            if i < self.height - 1:
                print("#" * self.width)
            else:
                print("#" * self.width, end="")

    def __str__(self):
        """Prints all the invisible text"""
        if self.height == 0 or self.width == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.width
                         for _ in range(self.height))

    def __repr__(self):
        """Returns the copied version of the function"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance is deleted"""
        print("Bye rectangle...")
