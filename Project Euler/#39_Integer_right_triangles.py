def triangularsets(n):
    sets = set()
    for a in range(1,n//3+1):
        b = (n*n-2*n*a)//(2*n-2*a)
        c = n-a-b
        if a*a + b*b == c*c and {a,b,c} not in sets:
            sets.add((a,b,c))
    return len(sets)
maxxlist=[0]*500007
counter=0
flag=0
for i in range(12,500007):
    value = triangularsets(i)
    if value > flag:
        maxxlist[i] = i
        counter = i
        flag=value
        print(counter,i,value)
    else:
        maxxlist[i] = counter
t=int(input('done').strip())
for _ in range(t):
    n = int(input().strip())
    print(maxxlist[n])        
        
