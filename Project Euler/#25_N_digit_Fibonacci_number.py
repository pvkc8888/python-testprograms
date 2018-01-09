def fib(n):
    if fiblist[n]!=0:
        return fiblist[n]
    else:
        return fib(n-2)+fib(n-1)

fiblist = [0]*24007
fiblist[0] = 1
fiblist[1] = 1
lenlist = [0]*24007
lenlist[0]=1
lenlist[1]=1
counter = 2
for i in range(2,24007):
    fiblist[i] = fib(i)
    if counter==len(str(fiblist[i])):
        lenlist[counter]=i+1
        counter=counter+1
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((lenlist[n]))