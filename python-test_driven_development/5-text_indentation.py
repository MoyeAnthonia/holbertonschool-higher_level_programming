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

    skip_space = False

    for idx, char in enumerate(text):
        if skip_space and char == " ":
            continue

        skip_space = False
        print(char, end="")

        if char in ".?:":
            if idx != len(text) - 1:
                print("\n")
                skip_space = True
