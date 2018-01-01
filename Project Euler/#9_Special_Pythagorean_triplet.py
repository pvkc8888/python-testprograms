#!/bin/python3

import sys,math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    prod = -1
    for number in range(1,int(n/2)): 
        a = number
        b = int(n*(n-2*a)/(2*n-2*a))
        c = n-a-b
        if (a*a)+(b*b) == (c*c):
            if (a*b*c)>prod:
                prod = a*b*c
    print(prod)
        