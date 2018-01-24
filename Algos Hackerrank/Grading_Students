#!/bin/python3

import sys

def solve(grades):
    ls = []
    for item in grades:
        if item%5 != 0 and ((item//5+1)*5-item)<3 and item >=38:
            ls.append((item//5+1)*5)
        else:
            ls.append(item)
    return ls

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
