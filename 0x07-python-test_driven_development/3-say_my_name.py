#!/usr/bin/python3
"""Unit Testing series...
   Test files in tests folder
"""


def say_my_name(first_name, last_name=""):
    """First and last names printing function"""
    if first_name.strip() == '' or last_name.strip() == '':
        raise ValueError("names cannot be empty")

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if not first_name.isalpha():
        raise ValueError("first_name must be between a-z")
    if not last_name.isalpha():
        raise ValueError("last_name must be between a-z")

    if not first_name.istitle():
        raise ValueError("first_name must must start with uppercase")
    if not last_name.istitle():
        raise ValueError("last_name must start with uppercase")
    if len(first_name) == 1 or len(last_name) == 1:
        raise ValueError("Name too short, can't be a name")

    print(f"My name is {first_name} {last_name}")
