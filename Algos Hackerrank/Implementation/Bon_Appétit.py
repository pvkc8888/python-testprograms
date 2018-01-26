#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    anna = ar[k]
    total = 0
    for item in ar:
        total += item
    shared = (total - anna)/2
    if b == shared:
       return 'Bon Appetit'
    else:
        return int(b - shared)
    
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
