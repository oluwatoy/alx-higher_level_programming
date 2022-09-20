#!/usr/bin/python3
for st in range(ord('z'), ord('a') - 1, -1):
    print("{:st}".format((st - (ord('a') - ord('A'))) if st % 2 else st), end='')
