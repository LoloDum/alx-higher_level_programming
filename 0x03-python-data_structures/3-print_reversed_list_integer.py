#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    print(*["{:d}".format(n) for n in my_list[::-1]], sep="\n")
