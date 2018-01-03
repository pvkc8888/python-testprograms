#Refer to the following article for detailed explanation of the formula
#https://www.mathsisfun.com/combinatorics/combinations-permutations.html


from math import factorial
t = int(input().strip())
for a0 in range(t):
    row,col = map(int,input().split(' '))
    matrix = [[0 for x in range(col)] for y in range(row)]
    print((factorial(row + col) // (factorial(row) * factorial(col))) % 1000000007)
