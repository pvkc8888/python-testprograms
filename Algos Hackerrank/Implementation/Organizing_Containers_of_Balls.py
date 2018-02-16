#!/bin/python3

import sys

def organizingContainers(container,n):
    listt = [0] * n
    clistt = [0] * n
    count = 0
    for balls in container:
        i = 0
        clistt[count] = sum(balls)
        count += 1 
        for item in balls:
            listt[i] += item
            i += 1
    listt.sort()
    clistt.sort()
    if listt == clistt:
        return 'Possible'
    else:
        return 'Impossible'
    
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
           container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
           container.append(container_t)
        result = organizingContainers(container,n)
        print(result)
