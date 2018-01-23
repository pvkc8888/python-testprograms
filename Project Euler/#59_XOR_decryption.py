import itertools,re
text = re.compile(r"[^a-zA-Z0-9-(;:,.?!)' ]")
t = int(input().strip())
n = input().split(' ')
#t=len(n)
passwordlist = itertools.permutations('abcdefghijklmnopqrstuvwxyz',3)
counter=0
for password in passwordlist: 
    string = ''
    passlist = password*(t//3+1)
    for item in range(len(n)):
        string = string + chr((int(n[item]) ^ ord(passlist[item])))
    if text.search(string)==None:
        print(''.join(password))
        break
