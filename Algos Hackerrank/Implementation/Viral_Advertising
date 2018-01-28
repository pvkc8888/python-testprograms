#!/bin/python3

import sys

def viralAdvertising(n):
    start = 2
    total = 2
    for i in range(n-1):
        new = (start*3)//2
        total += new
        start = new
        #print(start,new,total)
    return total          
        
        

if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
