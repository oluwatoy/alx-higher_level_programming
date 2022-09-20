#!/usr/bin/python3
for str in range(ord('a'), ord('z')+1):
    if chr(str) == 'e' or chr(str) == 'q':
        continue
    else:
        print("{:c}".format(str), end="")
