#!/usr/bin/python3
def roman_to_int(roman_string):
    x = 0
    if (type(roman_string) != str) or (roman_string is None):
        return 0
    pairs = {"I": 1, "V": 5, "X": 10,
             "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in range(len(roman_string)):
        if x > pairs[roman_string[i]]:
            x += pairs[roman_string[i]]
        else:
            x = pairs[roman_string[i]] - x
    return x
