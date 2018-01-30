#!/bin/python3

import sys,itertools

def acmTeam(topic):
    participants = len(topic)
    listt = [0]*(2*len(topic[0])+1)
    for item in range(participants):
        for item2 in range(item+1,participants):
            count = 0
            teamscore = int(topic[item])+int(topic[item2])
            for values in str(teamscore):
                if int(values) >= 1:
                    count += 1
            listt[count] += 1
    for i in range(len(listt)-1,0,-1):
        if listt[i] != 0:
            return i,listt[i]
        
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    topic = []
    topic_i = 0
    for topic_i in range(n):
       topic_t = str(input().strip())
       topic.append(topic_t)
    result = acmTeam(topic)
    print ("\n".join(map(str, result)))


