#!/bin/python3

import sys


def gameOfThrones(s):
    Dict = {}
    for item in s:
        if item not in Dict:
            Dict[item] = 1
        else:
            Dict[item] += 1
    count = 0
    for v in Dict.values():
        if (v % 2) != 0:
            count += 1
        if count > 1:
            return 'NO'
    return 'YES'


s = input().strip()
result = gameOfThrones(s)
print(result)
