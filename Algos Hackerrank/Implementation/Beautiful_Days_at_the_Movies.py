#!/bin/python3

import sys

def beautifulDays(i, j, k):
    count = 0
    for item in range(i,j+1):
        reversed = str(item)[::-1]
        if (item - int(reversed))%k == 0:
            count += 1
    return count

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)
