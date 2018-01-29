#!/bin/python3

import sys

def equalizeArray(arr):
    Dict = {}
    for item in arr:
        if item not in Dict:
            Dict[item] = 1
        else:
            Dict[item] += 1
    maxx = list(Dict.keys())[list(Dict.values()).index(max(Dict.values()))]
    #print(maxx)
    count = 0
    for keys,values in Dict.items():
        if keys != maxx:
            count += values
    return count

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
