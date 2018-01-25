#!/bin/python3

import sys

def solve(n, s, d, m):
    counter = 0
    for i in range(0,n-m+1):
        if d == sum(s[i:i+m]):
            counter += 1
    return counter
        

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
