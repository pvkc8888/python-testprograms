import sys
listt = [0]*3732450 #change the size according to your  needs.
#I am using 3732450 because after that the 
highest = [0]*3732450
listt[0] = 0
listt[1] = 0
listt[2] = 1

def collatz(n):
    temp = n
    counter = 0
    while n>1:
        if n%2==0:
            n = n//2
            counter = counter+1
            if n<3732449 and listt[n] != 0:
                counter += listt[n]
                listt[temp]=counter
                break
        else:
            n = 3*n+1
            counter = counter+1
            if n<3732449 and listt[n] != 0:
                counter += listt[n]
                listt[temp]=counter
                break
           
for i in range(3,3732430,1):
    collatz(i)
    
maxx = 0
for i in range(3732430):
    if listt[i]>=maxx:
        highest[i] = i
        maxx = listt[i]
    else:
        highest[i] = highest[i-1]
     
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n>=5649499 #this is actually not needed.
        print(5649499)
        continue  #continue the loop, dont break it like i did.
        
    if n>=3732423: #calculated already
        print(3732423)
        continue
    
    print(highest[n])
    #after 6hours finally!
