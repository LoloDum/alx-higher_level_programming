#!/usr/bin/python3
"""A class defining a rectangle
"""


class Rectangle:
    """A rectangle is defined by
    length multiplied by breadth
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width property"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the value, height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Evaluates the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Evaluates the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Handles string representation of the rectangle with a '#' """
        if self.__width == 0 or self.__height == 0:
            return ''
        res = ''
        for i in range(self.__height):
            for j in range(self.__width):
                res += '#'
            if i == self.__height - 1:
                break
            else:
                res += '\n'
        return res

    def __repr__(self):
        """return info of class an attributes"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Some other time"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
