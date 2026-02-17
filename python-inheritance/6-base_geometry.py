#!/usr/bin/python3
"""fill base class"""


class BaseGeometry():
    """Base Geometry"""
    def area(self):
        """returns the area of the geometric shape"""
        raise Exception("area() is not implemented")
