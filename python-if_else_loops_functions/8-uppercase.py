#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return print("{}".format(result), end="\n")
    #     i = chr(ord(i) - 32)
    #     print("{}".format(i), end="")
    # print()