import math
def penta(listt):
    for i in range(1,len(listt)):
        listt[i] = i*(3*i-1)//2
listt=[0]*1000007
penta(listt)
listt[0]=-10000
n,k=map(int,input().split(' '))
for item in range(1,n):
    try:
        num1=listt[item]-listt[item-k]
        numm1=(math.sqrt(24*num1+1)+1)/6
    except:
        num1==-1
        numm1=0.1
    try:
        num2 = listt[item]+listt[item-k]
        numm2 = (math.sqrt(24*num2+1)+1)/6
    except:
        num2=-1
        numm2=0.1
    if numm1%1 ==0 or numm2%1==0:
        print(listt[item])
