def fact(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return n*fact(n-1)

counter=0
n=int(input().strip())
for i in range(10,n+1):
    total=0
    number=i
    for x in range(len(str(i))):
        temp=i%10
        i=i//10
        total = total+fact(temp)
    if total%number==0:
        counter = counter+number
print(counter)
