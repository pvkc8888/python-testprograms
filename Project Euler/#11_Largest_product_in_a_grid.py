#!/bin/python3

import sys


grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
prod = 0
for i in range(20):
    for j in range(20):
        try:
            if prod < (grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]):
                prod = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
        except:
            pass
        try:
            if prod < (grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]):
                prod = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
        except:
            pass
        try:
            if prod < (grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]):
                prod = (grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3])
        except:
            pass
        try:
            if j-1>=0 and j-2>=0 and j-3>=0  and prod < (grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]):
                    prod = (grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3])
        except:
            pass
print(prod)