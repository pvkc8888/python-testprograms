#!/bin/python3

import sys

def diagonalDifference(a,n):
    summ1,summ2=0,0
    for i in range(n):
        summ1 = summ1 + a[i][i]
        summ2 = summ2 + a[i][n-i-1]
    #print(summ1,summ2)
    return abs(summ1-summ2)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a,n)
    print(result)
