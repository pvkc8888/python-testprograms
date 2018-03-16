#!/bin/python3

# So to solve this, I first did the brute force and got 2 TO. So in this method, we find the first discrepancy and check by removing each letter one after the other.

def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    l = len(s)
    r = s[::-1]
    for i in range(l // 2):
        if s[i] != r[i]:
            ns = s[:i] + s[i + 1:]
            if ns == ns[::-1]:
                return i
            else:
                ns = s[:l - i - 1] + s[l - i:]
                if ns == ns[::-1]:
                    return l - i - 1
    return -1


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)
