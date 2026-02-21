#!/usr/bin/python3
"""returns a json"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    
def add_item():
    """Adding items"""
    args = sys.argv[1:]
    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []

    for x in args:
        data.append(x)

    save_to_json_file(data, "add_item.json")


if __name__ == "__main__":
    add_item()
