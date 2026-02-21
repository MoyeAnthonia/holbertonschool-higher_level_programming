#!/usr/bin/python3
"""returns a json"""
import json


def save_to_json_file(my_obj, filename):
    """json return function"""
    with open(filename, "w") as file:
        return json.dump(my_obj, file, indent=4)
