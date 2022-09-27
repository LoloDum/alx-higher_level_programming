#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        temp = my_list[0]
        for num in my_list[1:]:
            if num > temp:
                temp = num
        return temp
    return None
