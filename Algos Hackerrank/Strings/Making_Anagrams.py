#!/bin/python3

import sys


def makingAnagrams(s1, s2):
    count = 0
    Dict1 = {}
    Dict2 = {}
    # similar to the previous problem, form dictionaries and find the common terms
    for item in s1:
        if item not in Dict1:
            Dict1[item] = 1
        else:
            Dict1[item] += 1
    for item in s2:
        if item not in Dict2:
            Dict2[item] = 1
        else:
            Dict2[item] += 1
    #print(Dict1, Dict2)
    for k, v in Dict1.items():
        if k in Dict2:
            count += min(v, Dict2[k])
    return (len(s1) + len(s2) - (count * 2))


s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
