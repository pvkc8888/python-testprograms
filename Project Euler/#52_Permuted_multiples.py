n,k = map(int,input().split(' '))
for j in range(125874,n+1):
    counter=1
    given = list(str(j))
    given.sort() 
    for i in range(2,k+1):
        number = j*i
        newpan = list(str(number))
        newpan.sort()
        if given==newpan:
            counter=counter+1
        else:
            break
    if counter==k:
        for num in range(1,k+1):
            print(num*int(j),end=" ")
        print()