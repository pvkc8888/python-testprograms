import sys
total = 0
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    total = total+n
print(str(total)[:10])