#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    total = 0
    for i in range(n):
        total = total + ar[i]
    return total

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
