import math

t = int(input().strip())
for a0 in range(t):
    string = list('abcdefghijklm')
    n = int(input().strip())-1
    counter=1
    flag = len(string)
    fact=[]
    while flag>0:
        fact.append(str(n%counter))
        n = n//counter
        #print(fact,n)
        counter=counter+1
        flag=flag-1
    fact=fact[::-1]
    for i in range(len(fact)):
        print(''.join(string.pop(int(fact[i]))),end="")
    print()