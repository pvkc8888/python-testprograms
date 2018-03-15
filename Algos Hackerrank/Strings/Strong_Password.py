#!/bin/python3


def minimumNumber(n, password):
    check1, check2 = 0, 0
    upper, lower, special, number = 0, 0, 0, 0
    for i in password:
        if i.isupper():
            upper = 1
        elif i.islower():
            lower = 1
        elif i in "!@#$%^&*()-+":
            special = 1
        elif i.isdigit():
            number = 1
    check1 = 4 - upper - lower - special - number
    if len(password) < 6:
        check2 = 6 - len(password)
    return max(check1, check2)


if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
