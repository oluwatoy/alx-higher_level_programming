#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(0, len(str)):
        if i == n:
            st = ""
            print(st, end="")
        else:
            print(str[i], end="")
        i += 1
remove_char_at("Best School", 3)
print()
remove_char_at("chicago", 2)
print()
remove_char_at("C is fun!", 0)
print()
remove_char_at("School", 10)
print()
remove_char_at("Python", -2)
