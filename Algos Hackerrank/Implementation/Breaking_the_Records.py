#!/bin/python3

import sys

def breakingRecords(score):
    best = score[0]
    worst = score[0]
    c1,c2 = 0,0
    for item in score:
        if item > best:
            best = item
            c1 += 1
        if item < worst:
            worst = item
            c2 += 1
    return (c1,c2)

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))


