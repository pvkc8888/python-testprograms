#!/bin/python3

import sys

def timeInWords(h, m):
    words = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
                                                         11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'quarter',16:'sixteen',17:'seventeen',
             18:'eighteen',19:'nineteen',20:'twenty',21:'twenty one',22:'twenty two',23:'twenty three',24:'twenty four',25:'twenty five',26:'twenty six',27:'twenty seven',28:'twenty eight',29:'twenty nine',30:'half'        
    }
    if m > 30:
        if 60 - m == 15:
            return words[60 - m] + ' to ' + words[h+1]
        string = words[60 - m] + ' minutes to ' + words[h+1]
    else:
        if m == 0:
            return words[h] + " o' clock"
        elif m == 15 or m == 30:
                return words[m] + ' past ' + words[h]
        elif m==1:
            string = words[m] + ' minute past ' + words[h]
        else:
            string = words[m] + ' minutes past ' + words[h]
    return string

if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)
