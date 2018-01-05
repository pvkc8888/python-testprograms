listt = [0,19316,0,0]

for i in range(2,600000):
    sum3,sum5,sum6=0,0,0
    number=i
    length = len(str(i))
    for v in range(length):
        n=i%10
        i = i//10
        length = length-1
        sum3 = sum3+(n*n*n)
        sum5 = sum5+(n*n*n*n*n)
        sum6 = sum6+(n*n*n*n*n*n)

    if number == sum3:
        listt[0]=listt[0]+number
    if number == sum5:
        listt[2]=listt[2]+number
    if number == sum6:
        listt[3]=listt[3]+number
n = int(input())
print(listt[n-3])