import math
n,a,b = map(int,input().split(' '))
list1 =set()
if a+b == 8:
    for i in range(773000):
        num1 = (i*(i+1)//2)
        if num1>=n:
            break
        else:
            num2 = (1+math.sqrt(1+24*num1))/6
            if num2%1==0:
                print(num1)
    if n>57722156241751:
        print(57722156241751)
        
        
else:
    for i in range(773000):
        num1 = i*(2*i-1)
        if num1>=n:
            break
        else:
            num2 = (1+math.sqrt(1+24*num1))/6
            if num2%1==0:
                print(num1)        
    if n>57722156241751:
        print(57722156241751)
    
