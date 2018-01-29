#!/bin/python3

import sys

def repeatedString(s, n):
    count = 0
    for item in s:
        if item == 'a':
            count += 1
    if n%len(s) != 0:
        total = count * (n//len(s))
        for i in range(n%len(s)):
            if s[i] == 'a':
                total += 1
    else:
        total = count * (n//len(s))
    return total

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)
