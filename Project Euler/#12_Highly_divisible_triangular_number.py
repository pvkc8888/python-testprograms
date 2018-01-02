import math
def divisors(n):
    factors = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            factors +=2
        if i*i==n:
            factors -=1
    return factors
Triangle_list = []
factor_list = []
for n in range(1,100000):
    Triangle=(n*(n+1))/2
    Triangle_list.append(Triangle)
    if n%2==0:
        counter=divisors(n/2)*divisors(n+1)
    else:
        counter=divisors(n)*divisors((n+1)/2)
    factor_list.append(counter)
t=int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for item in range(len(Triangle_list)):
        if n<factor_list[item]:
            print(int(Triangle_list[item]))
            break