import itertools
listt = [0]*10**7
listt[0]=1
listt[1]=1
def Sieve():
  for item in range(len(listt)):
    if listt[item]== 0:
      for i in range(2*item,len(listt),item):
        listt[i]=1
Sieve()
Dict=[]
for i in range(1,8):
  perm  = itertools.permutations(list(str(x) for x in range(1,i+1)))
  for item in perm:
    item = int(''.join(item))
    if listt[item]==0:
      if item not in Dict:
        Dict.append(item)
t = int(input().strip())
for a0 in range(t):
  n = int(input().strip())
  if n>7652413:
    print(7652413)
    continue
  maxx=0
  for item in Dict:
    if item<=n:
      maxx=item
    else:
      break
  if maxx==0:
    print(-1)
  else:
    print(maxx)