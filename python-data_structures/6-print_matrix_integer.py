#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for e in n:
            print("{:d}".format(e), end=" ")
        print("$")
