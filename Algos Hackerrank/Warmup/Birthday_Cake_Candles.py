#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    tallest = max(ar)
    temp = 0
    for item in ar:
        if item == tallest:
            temp += 1
    return temp

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
