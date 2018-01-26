#!/bin/python3

import sys

def sockMerchant(n, ar):
    Dict = {}
    counter = 0
    for item in ar:
        if item not in Dict:
            Dict[item] = 1
        else:
            Dict[item] += 1
    for keys,values in Dict.items():
        counter += values//2
    return counter
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
