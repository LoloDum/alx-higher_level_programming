#!/usr/bin/python3
def uppercase(str):
    for s in str:
        s = ord(s)
        if s >= 97 and s <= 122:
            s -= 32
        print("{}".format(chr(s)), end='')
    print('')
