#!/usr/bin/python3
# lst = ["{:02d}".format(a) for a in range(100)]
for a in range(10):
    for b in range(10):
        if a >= b:
            continue
        elif a == 8 and b == 9:
            print("{}{}".format(a, b))
        else:
            print("{}{}".format(a, b), end=", ")
