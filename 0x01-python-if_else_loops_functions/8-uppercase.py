#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <=122:
            st = ord(str[i]) - 32
            print("{:s}".format(chr(st)), end='')
        else:
            print("{:s}".format(str[i]), end='')
    i += 1
