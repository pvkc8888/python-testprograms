#!/bin/python3


def super_reduced_string(s):
    item = 0
    s = list(s)
    while True:
        count = 0
        for item in range(len(s) - 1):
            if s[item] == s[item + 1]:
                s.pop(item)
                s.pop(item)
                count += 1
                break
        if count == 0 or len(s) == 0:
            break
    return s


s = input().strip()
result = super_reduced_string(s)
if result == []:
    print('Empty String')
else:
    print(''.join(result))
