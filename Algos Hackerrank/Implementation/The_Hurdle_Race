#!/bin/python3

import sys

def hurdleRace(k, height):
    if k > max(height):
        return 0
    else:
        return max(height)-k

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)
