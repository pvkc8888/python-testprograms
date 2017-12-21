#!/bin/python3
def primelist():
    primelistt = [2]
    for i in range(3,110000,2):
        counter = 0
        for item in primelistt:
            if i%item==0:
                #print(i,item)
                break
            else:
                counter = counter+1
        if counter==len(primelistt):
            primelistt.append(i)
    return primelistt

import sys
primelistt = primelist()
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primelistt[n-1])
