#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <=122:
            st = ord(str[i]) - 32
            print(chr(st), end='')
        else:
            print(str[i], end='')
    i += 1
uppercase("best")
print()
uppercase("Best School 98 Battery street")
