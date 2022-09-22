#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if (len(sys.argv) == 1):
        print(len(sys.argv) - 1, "arguments.")
    elif (len(sys.argv) == 2):
        print(len(sys.argv) - 1, "argument:")
    else:
        print(len(sys.argv) - 1, "arguments:")
for i, arg in enumerate(sys.argv[1:]):
    print("{}: {}".format(i+1, arg))
