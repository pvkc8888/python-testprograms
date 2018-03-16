#!/bin/python3

import sys


def funnyString(s):
    r = s[::-1]
    count = 0
    for i in range(0, len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) == abs(ord(r[i]) - ord(r[i + 1])):
            count += 1
        else:
            return 'Not Funny'
    if count == len(s) - 1:
        return 'Funny'


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
