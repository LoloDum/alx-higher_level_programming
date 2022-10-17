#!/usr/bin/python3
"""Unit Testing series...
   Test files in tests folder
"""


def print_square(size):
    """ A function that prints a square """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise ValueError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
