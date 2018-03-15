#!/bin/python3

import itertools


def twoCharaters(s):
    Dict = {}
    for i in s:
        if i not in Dict:
            Dict[i] = 1
        else:
            Dict[i] += 1
    combinations = itertools.combinations(list(Dict.keys()), 2)
    maxx = 0
    final = ''
    for item in combinations:
        sample = ''
        count = 0

        for string in s:
            if string in list(item):
                sample += string
        for i in range(len(sample) - 1):
            if sample[i] != sample[i + 1]:
                count += 1
        if count == len(sample) - 1 and len(sample) > maxx:
            # print(sample)
            final = sample
            maxx = len(sample)
    return final


if __name__ == "__main__":
    l = int(input())
    s = input()
    result = twoCharaters(s)
    if result == '':
        print(0)
    else:
        print(len(result))
