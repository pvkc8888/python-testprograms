#!/bin/python3

import sys


def pairs(k, arr):
    numbers = set()
    count = 0
    for n in arr:
        if n + k in numbers:
            count += 1
        if n - k in numbers:
            count += 1
        numbers.add(n)
    return count


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pairs(k, arr)
    print(result)
