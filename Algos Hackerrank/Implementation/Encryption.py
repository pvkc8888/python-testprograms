#!/bin/python3

import sys,math

def encryption(s):
    news = ''
    for item in s:
        if item != ' ':
            news += item
    rows = math.floor(math.sqrt(len(news)))
    colm = math.ceil(math.sqrt(len(news)))
    maxx = 100
    for i in range(rows,colm+1):
        for j  in range(rows,colm+1):
            if i * j >= len(news)and i * j < maxx:
                maxx = i * j
                nro = i
                ncol = j
    result = ''
    for i in range(ncol):
        for j in range(nro):
            try:
                result += news[i+ncol*j]
            except:
                pass
        result += ' '    
    return result
                

if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)
