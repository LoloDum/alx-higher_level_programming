#!/usr/bin/python3
"""Unit Testing series...
   Test files in tests folder
"""


def text_indentation(text):
    """ A function that prints 2 new lines
    after a ., ? or :
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    for char in text:
        if char == ' ':
            continue
        if char in ['.', '?', ':']:
            print(char, "\n")
        else:
            print(char, end='')
