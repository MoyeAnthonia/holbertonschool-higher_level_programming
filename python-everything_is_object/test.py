#!/usr/bin/python3

with open("0-answer.txt", "r") as f:
    line_count = len(f.readlines())
    print(line_count)