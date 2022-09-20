#!/usr/bin/python3
def islower(c):
    if (ord(c) > 96) and (ord(c) < 123):
        return True
    else:
        return False
i = input("Enter a string")
if islower(i):
    print("{:s}".format(i), "is lower")
else:
    print("{:s}".format(i), "is upper")
