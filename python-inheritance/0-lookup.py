#!/usr/bin/python3
"""returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Gets every attribute from the object and puts it in a list"""
    return dir(obj)
