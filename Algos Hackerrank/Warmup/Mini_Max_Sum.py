#!/bin/python3

import sys,itertools,math

def miniMaxSum(arr):
    cases = itertools.combinations(arr,4)
    minn = math.inf
    maxx = 0
    for item in cases:
        total = sum(item)
        if total>maxx:
            maxx = total
        if total<minn:
            minn = total
    print(minn,maxx)        
            
            
if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
