#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    maxx = 0
    prod = 1
    for i in range(len(num)-k+1):
        temp = num[i:i+k]
        prod = 1
        for number in temp:
            prod = prod*int(number)
            #print(prod)
        if prod>maxx:
            #print(temp)
            maxx = prod
    print(maxx)
    