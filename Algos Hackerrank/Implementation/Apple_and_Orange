#!/bin/python3

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple,orange = 0,0
    for item in apples:
        if item>0 and a+item >= s and a+item <= t:
            apple += 1
    print(apple)
    for item in oranges:
        if item<0 and b+item >= s and b+item <= t:
            orange += 1
    print(orange)
if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)
