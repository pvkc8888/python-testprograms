#!/bin/python3

import sys

def summ(number):
    return (number*(number+1))/2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(summ(n))
    print(3*summ(int(n/3))+5*summ(int(n/5))-15*summ(int(n/15)))
