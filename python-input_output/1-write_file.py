#!/usr/bin/python3
"""write a text file"""


def write_file(filename="", text=""):
    """write file function"""
    with open(filename, "w") as file:
        return file.write(text)
