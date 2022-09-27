#!/usr/bin/python3

def no_c(my_string):
    res = "".join([s for s in my_string if s not in "cC"])
    return res
