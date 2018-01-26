#!/bin/python3

import sys

def solve(n, p):
    front = 0
    for i in range(1,n,2):
        if p == i or p == i-1:
            break
        else:
            front += 1
    back = 0
    if n%2 != 0:
        for i in range(n,1,-2):
            if p == i or p == i-1:
                break
            else:
                back += 1
    else:
        for i in range(n,1,-2):
            if p == i or p == i+1:
                break
            else:
                back += 1
    return min(front,back)

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
