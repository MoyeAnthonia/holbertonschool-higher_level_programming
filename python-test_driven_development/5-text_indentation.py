#!/usr/bin/python3
"""
This module contains a function that prints a text
with 2 new lines after each of these characters.
"""


def text_indentation(text):
    """
    Docstring for text_indentation

    Args:
    :param text: String (must be a string)

    Returns:
    text

    Raises:
    TypeError: If text is not string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char in ".?:":
            print()
