def binary(i,k):
    string = ''
    while i>0:
        if i%k!=0:
            string=string+str(i%k)
            i=i//k
        else:
            i=i//k
            string = string+'0'
    string = string[::-1]
    counter=0
    for i in range(len(string)//2):
        if string[i]==string[len(string)-1-i]:
            counter = counter+1
    if counter==len(string)//2:
        return True
    else:
        return False
    
    
def palin(i):
    string=str(i)
    if i<10:
        return True
    counter=0
    for i in range(len(string)//2):
        if string[i]==string[len(string)-1-i]:
            counter=counter+1
    if counter==len(string)//2:
        return True
    else:
        return False
        
n,k = map(int,input().split(' '))
summ=0
for i in range(1,n+1):
    if binary(i,k) and palin(i):
        summ=summ+i
print(summ)
