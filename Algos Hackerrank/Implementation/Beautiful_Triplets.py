#!/bin/python3

import sys

def beautifulTriplets(d, arr):
    count = 0
    for item in arr:
        if item + d in arr and item + 2*d in arr:
            count += 1
    return count

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    arr = list(map(int, input().strip().split(' ')))
    result = beautifulTriplets(d, arr)
    print(result)
