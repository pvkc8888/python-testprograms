def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
    return True


n = int(input().strip())
maxxa,maxxb=0,0
maxcounter=0
for a in range(n):
    for b in range(n):
        counter=0
        for n1 in range(n):
            if isPrime(n1*n1-a*n1+b):
                #print(a,b)
                counter=counter+1
            else:
                break
        if counter>maxcounter:
            #print(counter,maxcounter,a,b)
            maxxa = a
            maxxb = b
            maxcounter=counter
print(-maxxa,maxxb)