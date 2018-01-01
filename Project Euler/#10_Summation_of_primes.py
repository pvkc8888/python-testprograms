#!/bin/python3

import sys
def primelist():
    prime_list = []
    total_list = [0]*1100000
    total_list[0] = 1
    total_list[1] = 1
    for i in range(2,len(total_list)):
        if total_list[i] == 0:
            prime_list.append(i)
            for item in range(i,1100000,i):
                total_list[item] = 1
    return prime_list
            
            
                

t = int(input().strip())
prime_list = primelist()
summ = []
total = 0
counter = 0
for item in range(1,1000000):    
    prime = prime_list[counter]
    if item == prime:
        total = total+item
        counter = counter+1
    summ.append(total)
#print(summ)
        
for a0 in range(t):
    n = int(input().strip())
    print(summ[n-1])