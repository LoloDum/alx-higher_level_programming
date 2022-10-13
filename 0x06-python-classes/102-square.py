#!/usr/bin/python3
"""An empty 'class Square' here"""


class Square:
    """ A square is a four-sided shape"""
    def __init__(self, size=0):
        """Contructor set up goes here..."""

        self.size = size

    @property
    def size(self):
        """This retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A public intance method that
        returns area of the square"""
        return self.__size**2

    def __gt__(self, other):
        """defines greater than > """
        return self.area() > other.area()

    def __ge__(self, other):
        """defines greater than equal >= """
        return self.area() >= other.area()

    def __lt__(self, other):
        """defines less than < """
        return self.area() < other.area()

    def __le__(self, other):
        """defines less than > equals"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """defines equal to == """
        return self.area() == other.area()

    def __ne__(self, other):
        """defines not equal to != """
        return self.area() != other.area()
