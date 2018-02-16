#!/bin/python3

import sys

def cavityMap(grid):
    string =''
    for item in range(len(grid)):
        for elem in range(len(grid[item])):
            if item == 0 or item == len(grid)-1 or elem == 0 or elem == len(grid)-1:
                string += grid[item][elem]
            elif grid[item][elem] > grid[item][elem-1] and grid[item][elem] > grid[item][elem+1] and grid[item][elem] > grid[item-1][elem] and grid[item][elem] > grid[item+1][elem]:
                string += 'X'
            else:
                string += grid[item][elem]
        string += '\n'
    return string

if __name__ == "__main__":
    n = int(input().strip())
    grid = []
    grid_i = 0
    for grid_i in range(n):
       grid_t = str(input().strip())
       grid.append(grid_t)
    result = cavityMap(grid)
    print (result)
