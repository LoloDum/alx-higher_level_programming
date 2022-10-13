#!/usr/bin/python3
"""An empty 'class Square' here"""


class Square:
    """ A square is a four-sided shape"""
    def __init__(self, size=0, position=(0, 0)):
        """Contructor set up goes here..."""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves postion"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2\
         or not all(isinstance(x, int) for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """A public intance method that
        returns area of the square"""
        return self.__size**2

    def my_print(self):
        """prints out the square"""

        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()

        for i in range(self.__size):
            if self.__position[0] > 0:
                for i in range(self.__position[0]):
                    print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()

    def __str__(self):
        """represenrs Sqaure"""
        if self.__size != 0:
            [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end='') for j in range(self.__position[0])]
            [print("#", end='') for k in range(self.__size)]
            if i != self.__size - 1:
                print("")
        return ''
