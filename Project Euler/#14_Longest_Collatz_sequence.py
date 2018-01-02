import sys,time
tt = time.time()
listt = [0]*5000000
listt[0] = 1
listt[1] = 1
def collatz(n):
    temp = n
    counter = 1
    while n>1:
        if n%2==0:
            n = int(n/2)
            try:
                if listt[n-1] != 0:
                    counter += listt[n-1]
                    break
                else:
                    counter = counter+1
            except:
                pass
        else:
            n = 3*n+1
            try:
                if listt[n-1] != 0:
                    counter += listt[n-1]
                    break
                else:
                    counter = counter+1
            except:
                pass
    listt[temp-1]=counter       
for i in range(3,3000000,1):
    collatz(i)

t = int(input().strip())
for a0 in range(t):
    maxx,maxxnumber = 0,0
    n = int(input().strip())
    for i in range(n):
        if listt[i]>=maxx:
            maxx = listt[i]
            maxxnumber = i+1
    print(maxxnumber)
#print(time.time()-tt)
            