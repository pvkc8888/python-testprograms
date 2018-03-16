#!/bin/python3

# So i had to sub divide the continuous letters and count them, and then display the results.


def substringcount(s):
    sett = set()
    temp = s[0]
    count = 0
    for item in range(len(s)):
        if s[item] == temp:
            count += 1
            sett.add((ord(s[item]) - 96) * count)
        else:
            count = 1
            temp = s[item]
            sett.add((ord(s[item]) - 96) * count)
    return sett


s = input().strip()
sett = substringcount(s)
n = int(input().strip())
for a0 in range(n):
    x = int(input().strip())
    if x in sett:
        print('Yes')
    else:
        print('No')
