import math
def Sieve():
    prime_list=[0]*500007
    prime_list[1]=1 
    prime_list[0]=1
    for item in range(len(prime_list)):
        if prime_list[item] == 0:
            Primelist.append(item)
            for i in range(item,len(prime_list),item):
                prime_list[i]=1
Primelist = []
Sieve()

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    counter=0
    for item in Primelist:
        if item<n:
            number = (n-item)/2
            if (math.sqrt(number)- int(math.sqrt(number)))==0:
                #print(number,item)
                counter=counter+1
        else:
            break
    print(counter)
