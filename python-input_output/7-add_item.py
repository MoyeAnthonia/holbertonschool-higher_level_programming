#!/usr/bin/python3
"""Script that adds all arguments to a Python list
and saves them to a JSON file.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Try to load existing list from the file
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Add new command-line arguments (excluding script name)
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
