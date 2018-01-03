t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    factorial = 1
    for i in range(2,n+1):
        factorial = factorial*i
    factorial = str(factorial)
    summ=0
    for i in range(len(factorial)):
        summ = summ+int(factorial[i])
    print(summ)
