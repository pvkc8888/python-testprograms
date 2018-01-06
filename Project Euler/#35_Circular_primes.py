listt = [1]*1000007
listt[0] = 0
listt[1] = 0
trunct=[]
def primelist():
    for item in range(2,len(listt)):
        if listt[item] != 0:
            for i in range(2*item,1000007,item):
                    listt[i] = 0
circular_prime = []
primelist()
for i in range(len(listt)):
    if listt[i]==1:
        i=str(i)
        n = len(i)
        counter = 0
        flag=0
        for j in range(n):
            number = i[counter:n+1]+i[0:counter]
            if listt[int(number)]==1:
                flag=flag+1
                counter=counter+1
            else:
                break
        if flag==n:
            circular_prime.append(int(i))
n = int(input().strip())
total=0
for item in circular_prime:
    if item<n:
        total = total+item
    else:
        break
print(total)