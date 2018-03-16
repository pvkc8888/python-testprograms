#!/bin/python3

import sys


def alternatingCharacters(s):
    deletions = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            deletions += 1

    return deletions


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
