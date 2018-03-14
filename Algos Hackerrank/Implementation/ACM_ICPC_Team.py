#!/bin/python3

import itertools


def acmTeam(topic, n):
    Dict = {}
    teams = itertools.combinations(range(n), 2)
    for item in teams:
        count = 0
        teamtotal = int(topic[item[0]]) + int(topic[item[1]])
        teamtotal = str(teamtotal)
        for value in range(len(teamtotal)):
            if teamtotal[value] == '1' or teamtotal[value] == '2':
                count += 1
        # print(teamtotal,count)
        if count not in Dict:
            Dict[count] = 1
        else:
            Dict[count] += 1
    return [max(Dict), Dict[max(Dict)]]


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    topic = []
    topic_i = 0
    for topic_i in range(n):
        topic_t = str(input().strip())
        topic.append(topic_t)
    result = acmTeam(topic, n)
    print("\n".join(map(str, result)))
