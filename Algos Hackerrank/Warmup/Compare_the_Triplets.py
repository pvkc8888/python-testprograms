#!/bin/python3

import sys
Alice = list(map(int,input().strip().split(' ')))
Bob = list(map(int,input().strip().split(' ')))
a,b=0,0
for i in range(3):
    if Alice[i]>Bob[i]:
        a += 1
    elif Bob[i]>Alice[i]:
        b += 1
print (a,b)
