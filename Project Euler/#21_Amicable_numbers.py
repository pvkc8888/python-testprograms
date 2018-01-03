def summfactors(n):
    total = 0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            total = total+i+n//i
    return total-n

listt = [0,0]
for i in range(2,100000):
    listt.append(summfactors(i))

amicable_list=[]

for item in range(len(listt)):
    try:
        number = listt[item] 
        if listt[number]==item and item!=number:
            amicable_list.append(item)
    except:
        pass
print(amicable_list)
t = int(input().strip())
for a0 in range(t):
    total=0
    n = int(input().strip())
    for item in amicable_list:
        if item<n:
            total = total+item
        else:
            break
    print(total)
