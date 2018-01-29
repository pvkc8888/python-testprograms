#!/bin/python3

import sys

def serviceLane(width,cases):
    listt = []
    for item in cases:
        minn = min(width[item[0]:item[1]+1]) 
        listt.append(minn)
    return listt

if __name__ == "__main__":
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    width = list(map(int, input().strip().split(' ')))
    cases = []
    for cases_i in range(t):
       cases_t = [int(cases_temp) for cases_temp in input().strip().split(' ')]
       cases.append(cases_t)
    result = serviceLane(width, cases)
    print ("\n".join(map(str, result)))
