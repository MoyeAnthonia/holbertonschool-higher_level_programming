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
    for item in matrix:
        for item2 in item:
            if type(item2) is not int and type(item2) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError('division by zero')
    # print(round(item2 / div, 2), 'finail result')
    
    result = round(item2 / div, 2)
    matrix.clear()
    matrix.append(result)
    # print([matrix],"new list")
    return [matrix]