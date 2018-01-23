#!/bin/python3

import sys

def simpleArraySum(n, ar):
    total=0
    for i in range(n):
        total = total+ar[i]
    return total

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
