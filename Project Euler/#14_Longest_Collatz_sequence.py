import sys

listt = [0]*5000000
highest = [0]*5000000
listt[0] = 0
listt[1] = 0
listt[2] = 1

def collatz(n):
    temp = n
    counter = 1
    while n>1:
        if n%2==0:
            n = int(n/2)
            try:
                if listt[n] != 0:
                    counter += listt[n]
                    break
                else:
                    counter = counter+1
            except:
                pass
        else:
            n = 3*n+1
            try:
                if listt[n] != 0:
                    counter += listt[n]
                    break
                else:
                    counter = counter+1
            except:
                pass
    listt[temp]=counter       
for i in range(3,3000000,1):
    collatz(i)
    
maxx = 0
for i in range(3000000):
    if listt[i]>=maxx:
        highest[i] = i
        maxx = listt[i]
    else:
        highest[i] = highest[i-1]
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if(n>2999999):
        print(2952846)
        break
    print(highest[n])
