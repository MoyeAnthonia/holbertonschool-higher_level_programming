#!/usr/bin/python3
"""returns a json"""
import json


def load_from_json_file(filename):
    """json return function"""
    with open(filename, "r") as file:
        return json.load(file)
