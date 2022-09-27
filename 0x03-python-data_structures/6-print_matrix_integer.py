#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for item in matrix:
        print(*("{:d}".format(t) for t in item))
