def SumOfFactors(n):
    summ = 0
    for i in range(1,int(n**0.5)+1):
        if n%i==0 and i!=n//i:
            summ = summ+i+n//i
            continue
        elif n%i==0 and i==n//i:
            summ = summ+i
            continue
        else:
            continue
    return summ-n  

abundant = [0]*100007
for i in range(2,100007):
    summ = SumOfFactors(i)
    if i>20161:
        abundant[i] = 1
        continue
    if summ>i:
        abundant[i] = 1
        
summabundant = [0]*28124
for i in range(28124):
    for item in range(i+1//2+1):
        if abundant[item]!=0 and abundant[i-item]!=0:
            summabundant[i] = 1
            break
        else:
            continue
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n>28123:
        print('YES')
        continue
    elif summabundant[n]==1:
        print('YES')
    else:
        print('NO')