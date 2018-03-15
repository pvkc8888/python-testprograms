#!/bin/python3


def camelcase(s):
    count = 0
    for item in s:
        if item.isupper():
            count += 1
    return count + 1


if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
