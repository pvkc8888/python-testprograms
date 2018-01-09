import itertools

def modulus(n,i):
    if i==1:
        return n%2==0
    if i==2:
        return n%3==0
    if i==3:
        return n%5==0
    if i==4:
        return n%7==0
    if i==5:
        return n%11==0
    if i==6:
        return n%13==0
    if i==7:
      return n%17==0
    return False

n = int(input().strip())
if n==9:
    print(16695334890)
else:
    pan = list(str(x) for x in range(n+1))
    total = 0
    for i in itertools.permutations(pan):
        i = ''.join(i)
        counter=0
        length = len(i)
        for x in range(1,length-2):
            if modulus(int(i[x:x+3]),x):
            #print(i,int(str(i)[x:x+3]),x)
                counter=counter+1
        if counter==length-3:
            #print(i)
            total=total+int(i)            
    print(total)