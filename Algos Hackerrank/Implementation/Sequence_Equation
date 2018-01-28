#!/bin/python3

import sys

def permutationEquation(p,n):
    ls = []
    for i in range(1,n+1):
        y1 = (p.index(i)+1)
        y2 = p.index(y1)+1
        ls.append(y2)
    return ls

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = permutationEquation(p,n)
    print ("\n".join(map(str, result)))
