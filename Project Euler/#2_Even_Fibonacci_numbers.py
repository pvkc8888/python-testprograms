#!/bin/python3

import sys

def fibonacci():
	summ = []
	summ.append(1)
	summ.append(2)
	for i in range(2,10000):
		summ.append((summ[i-1]+summ[i-2]))
	return summ

t = int(input().strip())
summ = fibonacci()
for a0 in range(t):
    n = int(input().strip())
    total = 0
    for i in range(len(summ)):
    	if summ[i]<n and summ[i]%2==0:
    		total = total+summ[i]
    	elif summ[i]>=n:
    		break
    print(total)


