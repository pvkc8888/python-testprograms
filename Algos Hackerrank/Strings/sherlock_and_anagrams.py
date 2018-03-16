#!/bin/python3

# simple function to calculate factorial of n


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * (n - 1)


def sherlockAndAnagrams(s):
    anagrams = 0
    Dict = {}
    for i in range(len(s)):
        for item in range(i, len(s)):
            # storing all the unique strings in dict and noting down how many of them exist
            try:
                string = s[i:item + 1]
                string = ''.join(sorted(string))
                if string in list(Dict.keys()):
                    Dict[string] += 1
                else:
                    Dict[string] = 1
            except IndexError:
                pass
    # calulating the different pairs posssible and summing them up to get the total number of anagrams.
    for values in Dict.values():
        if values > 1:
            anagrams += factorial(values) // 2

    return anagrams


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)
