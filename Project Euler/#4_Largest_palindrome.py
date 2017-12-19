#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
	highest = 101101
	n = int(input().strip())
	for i in range(101101,n,11):
		if str(i)[0]==str(i)[5] and str(i)[1]==str(i)[4] and str(i)[2]==str(i)[3]:
			for item in range(100,1000):
				if i%item==0 and (i/item)<1000:
					highest = i
					continue
	print(highest)
