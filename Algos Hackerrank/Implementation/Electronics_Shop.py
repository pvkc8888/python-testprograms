#!/bin/python3

import sys,itertools

def getMoneySpent(keyboards, drives, s):
    if min(keyboards)+min(drives)>s:
        return (-1)
    else:
        maxx = 0
        cases = itertools.product(keyboards,drives)
        for item in cases:
            if maxx < sum(item) and sum(item)<=s:
                maxx = sum(item)
        return maxx
s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
