#!/bin/python3

import sys

def countingValleys(n, s):
    sea = 0
    counter = 0
    for item in s:
        if sea == 0 and item == 'D':
            counter += 1
        if item == 'U':
            sea += 1
        if item == 'D':
            sea -= 1
    return counter

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
