#!/bin/python3


def marsExploration(s):
    count = 0
    expected = 'SOS' * (len(s) // 3)  # had to check for each character instead of one word. Hence the error

    for i in range(len(s)):
        if s[i] != expected[i]:
            count += 1
    return count


if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)
