#!/usr/bin/python3
print(*["{:02d}".format(a) for a in range(100)], sep=", ")
