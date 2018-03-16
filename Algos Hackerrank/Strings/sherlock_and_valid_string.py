#!/bin/python3


def isValid(s):
    Dict = {}
    for item in s:
        if item not in Dict:
            Dict[item] = 1
        else:
            Dict[item] += 1
    print(Dict)
    # this is not dict values, it should be number of different numbers etc. So use keys and values.
    Dict1 = {}
    for item in Dict.values():
        if item not in Dict1:
            Dict1[item] = 1
        else:
            Dict1[item] += 1
    print(Dict1)
    # if there are more than 2 different values, its not valid
    if len(Dict1.keys()) > 2:
        return 'NO'
    # if the frequency is same then its valid
    elif len(Dict1.keys()) == 1:
        return 'YES'
    else:
        keys = list(Dict1.keys())
        for k, v in Dict1.items():
            # this is check for extra number occuring once
            if v == 1 and k == 1:
                return 'YES'
    # this line checks if we can make it valid by deleting just one key
            elif v == 1 and abs(keys[1] - keys[0]) == 1:
                return 'YES'

    return 'NO'


s = input().strip()
result = isValid(s)
print(result)
