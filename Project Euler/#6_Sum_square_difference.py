#!/bin/python3
def squares(n):
    total=0
    for i in range(1,n+1):
        total = total+(i*i)
        #print(total)
    return total

def summ(n):
    return ((n*(n+1))/2)*((n*(n+1))/2)

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if summ(n)>squares(n):
        print(int(summ(n)-squares(n)))
    else:
        print(int(squares(n)-summ(n)))
