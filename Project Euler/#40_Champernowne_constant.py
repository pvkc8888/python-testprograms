string=''
for i in range(1,10000007):
    string = string+str(i)
t = int(input())
for a0 in range(t):
  listt = list(map(int,input().split(' ')))
  total=1
  for i in listt:
    total = total*int(string[i-1])
  print(total)
