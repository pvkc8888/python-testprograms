#!/bin/python3

import sys,itertools

def divisibleSumPairs(n, k, ar):
    counter = 0
    cases = itertools.combinations(ar,2)
    for item in cases:
        if (sum(item)/k) % 1 == 0:
            counter += 1
    return counter
        
        

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
