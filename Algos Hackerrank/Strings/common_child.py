#!/bin/python3

# okay so i first thought ill do it by using itertools, but obviously its so lengthy and time taking.
# This problem is an important concept in cs, known as lcs problem, refer here https://en.wikipedia.org/wiki/Longest_common_subsequence_problem


def common_child(s1, s2):
    C = [[0] * 5001 for i in range(5001)]
    for i in range(0, m):
        for j in range(0, n):
            if s1[i] == s2[j]:
                C[i + 1][j + 1] = C[i][j] + 1
            else:
                C[i + 1][j + 1] = max(C[i + 1][j], C[i][j + 1])
    return C[m][n]


s1 = input().strip()
s2 = input().strip()
m = len(s1)
n = len(s2)
# also, I didnt write this in a function because, function call takes extra time and test case is failing. Sorry, I take it back, accessing a function variable is much faster than accessing a file variable. Hence, included the function again.

# got 5 case TO even after using the lcs method. python you noob?

# okay so I learnt somthing new with this problem, PyPy is a modded version of python which runs significantly faster than python, the code failes in 6 TC for python3, but finished compiling in less than 5sec in PyPY,

print(common_child(s1, s2))
