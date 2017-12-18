#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    number = int(input().strip())
    for item in range(2,int(number**(0.5))+1):
    	while number%item == 0:
    		number = number/item
    		prime = item
    		print(item,number,prime)
    if number>1:
    	prime = number
    print(int(prime))