#!/bin/python3

import sys,itertools

t = int(input().strip())
for a0 in range(t):
    
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    sett = set(x for x in range(1,n+1))
    #print(sett)
    listt = []
    count = 0
    for i in range(1,n+1):
        if i - k in sett:
            count += 1
            listt.append(i-k)
            sett.remove(i-k)
        elif i + k in sett:
            count += 1
            listt.append(i+k)
            sett.remove(i+k)
    if count == n:
        for item in listt:
            print(item,end = ' ')
        print()
    else:
        print(-1)
