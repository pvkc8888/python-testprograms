#!/bin/python3

import sys


def theLoveLetterMystery(s):
    count = 0
    r = s[::-1]
    for i in range(len(s) // 2):
        count += abs(ord(s[i]) - ord(r[i]))
    return count


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)
