def sieve():
    primelist = [1] * 1000000007
    for i in range(2, 1000000007):
        if primelist[i] == 1:
            for item in range(2 * i, 1000000007, i):
                primelist[item] = 0
    return primelist


primelist = sieve()
count = 0
for item in range(10000):
    if primelist[item * item * 2 - 1] == 1:
        count += 1
    # else:
    #     print(item * item * 2 - 1)
print(count)
