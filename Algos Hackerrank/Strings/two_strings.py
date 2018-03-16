#!/bin/python3

import sys


def twoStrings(s1, s2):
    string = 'abcdefghijklmnopqrstuvwxyz'
    for i in string:
        if i in s1 and i in s2:
            return 'YES'
    return 'NO'

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
