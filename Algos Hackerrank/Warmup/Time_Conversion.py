#!/bin/python3

import sys

def timeConversion(s):
    if s[8]=='A':
        if s[0]=='1' and s[1]=='2':
            print('00'+s[2:8])
        else:
            print(s[:8])
    else:
        temp = int(s[0:2])
        if temp==12:
            print(s[:8])
        else:
            print(str(12+temp)+s[2:8])
s = input().strip()
result = timeConversion(s)
