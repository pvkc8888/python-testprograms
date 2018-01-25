#!/bin/python3

import sys

def Lcm(a):
    for i in range(1,max(b)+1):
        flag = 0
        for item in a:
            if (i/item) % 1 == 0:
                flag+=1
            else:
                continue
        if flag == n:
            return i

def getTotalX(a, b,n,m):
    counter = 0
    lcm = Lcm(a)
    #print(lcm)
    if lcm == None:
        return 0
    for i in range(lcm,101,lcm):
        flag = 0
        for item in b:
            if (item/i) % 1 == 0:
                flag += 1
            else:
                break
        if flag == m:
            #print(i)
            counter += 1
    return counter
        
        

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b,n,m)
    print(total)
