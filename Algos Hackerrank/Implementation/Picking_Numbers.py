#!/bin/python3

import sys,itertools

def pickingNumbers(a,n):
    Dict = {}
    for i in range(n):
        if a[i] not in Dict:
            Dict[a[i]] = 1
        else:
            Dict[a[i]] += 1
    maxx = 0
    total = 0
    for key,value in Dict.items():
        if key+1 in Dict:
            total = Dict[key]+Dict[key+1]
            if total > maxx:
                maxx = total
        elif value > maxx:
            maxx = value
    if maxx == 0:
        return max(Dict.values())
    else:    
        return maxx


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a,n)
    print(result)
