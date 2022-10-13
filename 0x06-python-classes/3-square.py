#!/usr/bin/python3
"""An empty 'class Square' here"""


class Square:
    """ A square is a four-sided shape"""
    def __init__(self, size=0):
        """Contructor set up goes here..."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """A public intance method that
        returns area of the square"""
        return self.__size**2
