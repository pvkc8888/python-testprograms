import re
match = re.compile(r'0{1}|1{1}|2{1}|3{1}|4{1}|5{1}|6{1}|7{1}|8{1}|9{1}')
n = int(input().strip())
subset = list(str(x) for x in range(1,n+1))
total=0
products=set()
for i in range(1,100):
    for j in range(1,2000):
        listt = match.findall(str(i)+str(j)+str(i*j))
        listt.sort()
        if subset==listt:
            if i*j not in products:
                total = total+(i*j)
                products.add(i*j)
print(total)