#!/usr/bin/python3
"""Unit Testing series...
   Test files in tests folder
"""


def matrix_divided(matrix, div):
    """Matrix division function"""
    if type(matrix) != list or not matrix:
        raise TypeError("must be a valid matrix")

    if not all([type(lst) == list for lst in matrix]):
        raise TypeError("all elements must be matrices")

    for lst in matrix:
        if not all([type(x) in [float, int] for x in lst]):
            raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")

    if len(set([len(lst) for lst in matrix])) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [float, int]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    res = [[round(x/div, 2) for x in lst] for lst in matrix]

    return res
