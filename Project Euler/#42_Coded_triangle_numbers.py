import math
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if ((1+8*n)**0.5 % 1) == 0:
        print(int((-1+(1+8*n)**0.5)//2))
    else:
        print(-1)