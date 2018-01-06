listt = [1]*1000007
listt[0] = 0
listt[1] = 0
trunct=[]
def primelist():
    for item in range(2,len(listt)):
        if listt[item] != 0:
            for i in range(2*item,1000007,item):
                    listt[i] = 0
        if item>10:
            counter=0
            n = len(str(item))
            for i in range(n):
                n1 = item%10**(n-i)
                n2 = item//10**(n-i-1)
                if listt[n1]!=0 and listt[n2]!=0:
                    counter = counter+1
                else:
                    break
            if counter==n:
                trunct.append(int(item))
                
primelist()
n= int(input().strip())
total=0
for item in trunct:
    if item<n:
        total = total+item
    else:
        break
print(total)