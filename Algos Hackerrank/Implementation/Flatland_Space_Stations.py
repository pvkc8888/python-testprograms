#!/bin/python3

import sys

def flatlandSpaceStations(n, c):
    spacelist = []
    for i in range(n):
        distance = 10e5+7
        if i not in c:
            for item in c:
                if abs(item-i) < distance:
                    distance = abs(item-i)
            spacelist.append(distance)                    
        else:
            spacelist.append(0)
    #print(spacelist)
    return max(spacelist)
             
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))
    result = flatlandSpaceStations(n, c)
    print(result)


''' Solution from discussions. My solution T.O.E for 2 cases. :( 
n, m = input().split()
n, m = int(n), int(m)
stations = sorted(int(station) for station in input().split())
maximum = max(stations[0], n - stations[-1] - 1)
for i in range(1, m):
    d = stations[i] - stations[i-1]
    maximum = max(d//2, maximum)
print(maximum)
'''
