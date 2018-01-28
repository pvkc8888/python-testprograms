#!/bin/python3

import sys

def designerPdfViewer(h, word):
    maxx = 0
    for i in word:
        if h[ord(i)-97] > maxx:
            maxx = h[ord(i)-97]
    return maxx*len(word)

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
