#!/bin/python3

import sys


def countingSort(arr):
    listt = [0] * 100
    for item in arr:
        listt[item] += 1
    return listt


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print(" ".join(map(str, result)))
