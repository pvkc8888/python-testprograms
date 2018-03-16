#!/bin/python3

import sys


def stringConstruction(s):
    p = ''
    count = 0
    for item in s:
        if item not in p:
            p += item
            count += 1
    return count


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = stringConstruction(s)
        print(result)
