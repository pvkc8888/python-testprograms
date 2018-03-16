#!/bin/python3

import sys


def separateNumbers(s):
    for i in range(len(s) // 2):
        num = int(s[:i + 1])
        temp = num
        string = ''
        while len(string) < len(s):
            string += str(num)
            num += 1
        if string == s:
            print('YES ' + str(temp))
            return 0
    print('NO')


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        separateNumbers(s)
