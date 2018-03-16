#!/bin/python3

import sys


def anagram(s):
    if len(s) % 2 != 0:
        return -1
    else:
        s1 = s[:len(s) // 2]
        s2 = s[len(s) // 2:]
        count = 0
        Dict1 = {}
        Dict2 = {}
        # I thought i ll make two seperate dictionaries and count the common elements and subrtact it from the total count.
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
        finalDict = {}
        for k, v in Dict1.items():
            if k in Dict2:
                minn = min(v, Dict2[k])
                finalDict[k] = minn
        for k, v in finalDict.items():
            count += v
        return ((len(s1)) - count)


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)
