#!/bin/python3

import sys


def hackerrankInString(s):
    string = 'hackerrank'
    s = list(s)
    count = 0
    p = 0
    for i in string:
        if i in s:
            count += 1
            # so sub-string apparently means we have to include order also.
            s = s[s.index(i) + 1:]

    if count < 10:
        return 'NO'
    else:
        return 'YES'


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)
