#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	if n==1:
		print(1)
		continue
	for i in range(2,1000000000000):
		lcm = 1
		for item in range(2,n+1):
			if(i%item==0):
				lcm = lcm+1
			else:
				break
		if lcm==n:
			print(i)
			break
