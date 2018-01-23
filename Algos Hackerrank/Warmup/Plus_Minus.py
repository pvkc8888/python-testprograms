#!/bin/python3

import sys

def plusMinus(arr,n):
    temp1,temp2=0,0
    for item in arr:
        if item>0:
            temp1 += 1
        elif item<0:
            temp2 += 1
    print(temp1/n,temp2/n,(n-temp1-temp2)/n,sep='\n')

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr,n)
