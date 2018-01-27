#!/bin/python3

import sys

def climbingLeaderboard(scores, alice):
    ls = []
    scores = list(set(scores))
    scores.sort()
    length = len(scores)
    counter = 0
    for item in alice:
        for i in range(counter,length):
            if scores[i] > item:
                ls.append(length-counter+1)
                counter = i
                break
            else:
                counter += 1
        if counter == length:
            ls.append(1)
    return ls
    

if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    result = climbingLeaderboard(scores, alice)
    print ("\n".join(map(str, result)))
