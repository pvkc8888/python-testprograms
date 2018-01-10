fact_list=[0]*1007
fact_list[0] = 1
for i in range(1,1007):
    fact_list[i]=i*fact_list[i-1]
n,k=map(int,(input().split(' ')))
counter=0
for i in range(1,n+1):
    for j in range(1,i+1):
        number = (fact_list[i]//fact_list[j]//fact_list[i-j])
        if number>k:
            counter=counter+1
print(counter)
