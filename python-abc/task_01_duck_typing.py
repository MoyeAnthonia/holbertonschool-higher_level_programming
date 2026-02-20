#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Creating an abstract class"""


class Shape(ABC):
    """Abstract class method"""

    @abstractmethod
    def area(self):
        """Empty sound method"""
        pass

    @abstractmethod
    def perimeter(self):
        """Empty sound method"""
        pass


class Circle(Shape):
    """Rep circle class"""
    def __init__(self, radius):
        """insantitied"""
        super().__init__()
        self.radius = radius

    def area(self):
        """call the parent method"""
        A = 3.14 * (self.radius ** 2)
        return A

    def perimeter(self):
        """call the parent method"""
        C = 3.14 * (self.radius ** 2)
        return C


class Rectangle(Shape):
    """Rep rectangle class"""

    def __init__(self, width, height):
        """insantitied"""
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        """call the parent method"""
        A = self.width * self.height
        return A

    def perimeter(self):
        """call the parent method"""
        P = 2 * (self.width + self.height)
        return P


def shape_info(entity):
    """Duck typing function example"""
    print("Area:", entity.area())
    print("Perimeter:", entity.perimeter())
