#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    full_letters = chr(i)
    remove_map = str.maketrans('', '', 'eq')
    new_text = full_letters.translate(remove_map)
    print("{}".format(new_text), end="")
