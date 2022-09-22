#!/usr/bin/python3
print("".join(["{}".format(chr(a)) for a in range(97, 123) if chr(a) not in "eq"]), end="")
