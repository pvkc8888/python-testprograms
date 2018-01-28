#!/bin/python3

import sys

def appendAndDelete(s, t, k):
    if s != t:
        sl,tl = len(s),len(t)
        count = 0
        if tl <= sl:
            for i in range(tl):
                if t[i] != s[i]:
                    count += sl+tl-2*i
                    break
            if count <= k:
                return 'Yes'
            else:
                return 'No'
        else:
            if s[:sl] != t[:sl]:
                for i in range(sl):
                    if t[i] != s[i]:
                        count += sl+tl-2*i
                        break
                if count <= k:
                    return 'Yes'
                else:
                    return 'No'
            else:
                if (k-(tl-sl)) % 2 == 0:
                    return 'Yes'
                else:
                    return 'No'
    else:
        if k % 2 == 0 or k >= len(s)+1:
            return 'Yes'
        else:
            return 'No'
if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
