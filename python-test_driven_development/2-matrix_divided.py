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
    if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")
    if div == 0:
            raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    new_row.append(round(element / div, 2))
    new_matrix.append(new_row)
    return new_matrix