#!/usr/bin/python3
"""append a text file"""


def append_write(filename="", text=""):
    """append file function"""
    with open(filename, "a") as file:
        return file.write(text)
