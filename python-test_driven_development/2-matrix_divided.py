#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Docstring for matrix_divided
    
    Args:
    :param matrix: Lists (must be lists of integers or floats)
    :param div: Number (must be a integer or float)
 
    Returns:
    a new matrix

    Raises:
    TypeError: If matrix is not an integer or float
    TypeError: If matrix row is not same size
    TypeError: If div is not an integer or float

    """
    
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = None
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if type(element) not in (int, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
            new_row.append(round(element / div, 2))

        new_matrix.append(new_row)

    return new_matrix