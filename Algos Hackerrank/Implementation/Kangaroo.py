#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1:
        return 'NO'
    if x1 > x2 and v1 > v2:
        return 'NO'
    if v1==v2 and x1 != x2:
        return 'NO'
    if v1==v2 and x1 == x1:
        return 'YES'
    n = (x2-x1)/(v1-v2)
    if n%1==0:
        return 'YES'
    return 'NO'

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
