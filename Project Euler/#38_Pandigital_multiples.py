n,k = map(int,input().split(' '))
#print(n,k)
check = [str(i) for i in range(1,k+1)]
#print(check)
for i in range(2,n+1):
    string=''
    for num in range(1,10):
        string = string + str(i*num)
        #print(string)
        if len(string)==k:
            string=list(string)
            string.sort()
            if string==check:
                print(i)
                break
            else:
                break
