#!/bin/python3

import sys

def formingMagicSquare(s):
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    total7 = 0
    total8 = 0
    
    magic1 = [[2,7,6],
             [9,5,1],
             [4,3,8]]
    
    magic2 = [[2,9,4],
             [7,5,3],
             [6,1,8]]
             
    magic3 = [[4,3,8],
             [9,5,1],
             [2,7,6]]
    
    magic4 = [[4,9,2],
             [3,5,7],
             [8,1,6]]
    
    magic5 = [[6,1,8],
             [7,5,3],
             [2,9,4]]
    
    magic6 = [[6,7,2],
             [1,5,9],
             [8,3,4]]
            
    magic7 = [[8,1,6],
             [3,5,7],
             [4,9,2]]
    
    magic8 = [[8,3,4],
             [1,5,9],
             [6,7,2]]
   
    for i in range(3):
        for j in range(3):
            if s[i][j] != magic1[i][j]:
                total1 += abs(s[i][j]-magic1[i][j])
                
            if s[i][j] != magic2[i][j]:
                total2 += abs(s[i][j]-magic2[i][j])
            
            if s[i][j] != magic3[i][j]:
                total3 += abs(s[i][j]-magic3[i][j])
            
            if s[i][j] != magic4[i][j]:
                total4 += abs(s[i][j]-magic4[i][j])
            
            if s[i][j] != magic5[i][j]:
                total5 += abs(s[i][j]-magic5[i][j])
            
            if s[i][j] != magic6[i][j]:
                total6 += abs(s[i][j]-magic6[i][j])
            
            if s[i][j] != magic7[i][j]:
                total7 += abs(s[i][j]-magic7[i][j])
            
            if s[i][j] != magic8[i][j]:
                total8 += abs(s[i][j]-magic8[i][j])
                
    return min(total1,total2,total3,total4,total5,total6,total7,total8)
if __name__ == "__main__":
    s = []
    for s_i in range(3):
       s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
       s.append(s_t)
    result = formingMagicSquare(s)
    print(result)
