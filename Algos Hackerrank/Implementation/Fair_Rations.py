#!/bin/python3

import sys

def fairRations(B):
    summ = sum(B)
    if summ % 2 != 0 :
        return 'NO'
    else:
        counter = 0
        for item in range(len(B)-1):
            if B[item] % 2 != 0:
                B[item] += 1
                B[item + 1] += 1
                counter += 2
    return counter

if __name__ == "__main__":
    N = int(input().strip())
    B = list(map(int, input().strip().split(' ')))
    result = fairRations(B)
    print(result)
