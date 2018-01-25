#!/bin/python3

import sys

def migratoryBirds(n, ar):
    Dict = {1:0,
            2:0,
           3:0,
           4:0,
           5:0}
    for item in ar:
        Dict[item] += 1
    maxx = max(list(Dict.values()))
    return(list(Dict.keys())[list(Dict.values()).index(maxx)])
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
