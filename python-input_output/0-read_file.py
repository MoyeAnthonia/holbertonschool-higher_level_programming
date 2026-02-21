#!/usr/bin/python3
"""Read a text file"""


def read_file(filename=""):
    """read file function"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
