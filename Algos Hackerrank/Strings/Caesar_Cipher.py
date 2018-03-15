#!/bin/python3

import sys


def caesarCipher(s, k):
    s1 = ''
    for item in s:
        if item.islower():
            new = ord(item) + k
            if new > 122:
                new -= 26
                s1 += chr(new)
            else:
                s1 += chr(new)
        elif item.isupper():
            new = ord(item) + k
            if new > 90:
                new -= 26
                s1 += chr(new)
            else:
                s1 += chr(new)
        else:
            s1 += item
    return s1


if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    if k > 26:
        k = k % 26
    result = caesarCipher(s, k)
    print(result)
