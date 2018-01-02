t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    number = str(2**n)
    total = 0
    for i in range(len(number)):
        total+=int(number[i])
    print(total)
