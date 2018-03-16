#!/bin/python3

import sys

# making set of the smallest string and checking if each character in that set exists in all the strings


def gemstones(arr):

    minn = len(arr[0])
    temp = ''
    for item in arr:
        if len(item) < minn:
            minn = len(item)
            temp = item
    sett = set(temp)
    gems = 0
    for item in sett:
        count = 0
        for string in arr:
            if item in string:
                count += 1
        if count == len(arr):
            gems += 1
    return gems


n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
    arr_t = str(input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)
