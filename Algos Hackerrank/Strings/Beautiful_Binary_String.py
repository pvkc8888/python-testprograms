#!/bin/python3

import sys

# we just have to find the instances of '010', since that is the number of corrections we have to make.


def beautifulBinaryString(b):
    return b.count('010')


if __name__ == "__main__":
    n = int(input().strip())
    b = input().strip()
    result = beautifulBinaryString(b)
    print(result)
