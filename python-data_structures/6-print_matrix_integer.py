#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for e in n:
            print("{0}".format(e), end=" ")
        print("$")
