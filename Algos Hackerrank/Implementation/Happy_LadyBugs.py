#!/bin/python3


Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    Dict = {}
    count = 0
    if len(b) == 1 and b != '_':
        print('NO')
        continue
    if '_' not in b:
        if b[0] != b[1] or b[len(b) - 1] != b[len(b) - 2]:
            print('NO')
            continue
        for item in range(1, len(b) - 1):
            if b[item] == b[item - 1] or b[item] == b[item + 1]:
                count += 1
        if count + 2 == len(b):
            print('YES')
        else:
            print('NO')
        continue
    for item in b:
        if item == '_':
            continue
        if item not in Dict:
            Dict[item] = 1
        else:
            Dict[item] += 1
    # print(Dict)
    if 1 not in Dict.values():
        print('YES')
    else:
        print('NO')
