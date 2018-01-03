def value(name):
    name = name.lower()
    total = 0
    for i in range(len(name)):
        total = total + ord(name[i])-96
    return total

t = int(input().strip())
names = []
Dict = {}
for a0 in range(t):
    name = input().strip()
    names.append(name)
    Dict[name] = a0
    
for keys,values in Dict.items():
    Dict[keys] = value(keys)
    
names = sorted(names,key = str.lower)

tt = int(input().strip())
for a1 in range(tt):
    counter = 1
    find = input().strip()
    for items in range(len(names)):
        if names[items] == find:
            break
        else:
            counter = counter+1
    print(counter*Dict[find])
