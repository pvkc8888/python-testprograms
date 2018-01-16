n=int(input().strip())
for i in range(1000000):
    if len(str(i**n))==n:
        print(i**n)
