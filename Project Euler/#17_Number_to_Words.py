t = int(input('here').strip())
Dict0 = {1:'One',
         2:'Two',
         3:'Three',
         4:'Four',
         5:'Five',
         6:'Six',
         7:'Seven',
         8:'Eight',
         9:'Nine'}

Dict1 = {10:'Ten',
         11:'Eleven',
         12:'Twelve',
         13:'Thirteen',
         14:'Fourteen',
         15:'Fifteen',
         16:'Sixteen',
         17:'Seventeen',
         18:'Eighteen',
         19:'Nineteen'}

Dict2 = {1:'Ten',
         2:'Twenty',
         3:'Thirty',
         4:'Forty',
         5:'Fifty',
         6:'Sixty',
         7:'Seventy',
         8:'Eighty',
         9:'Ninety'}

#for a0 in range(t):
for n in range(1001):
    n = str(n)    
    length = len(n)
    if int(n)==0:
        print('Zero')
        continue    
    
    if int(n) == 1000000000000:
        print('Thousand Billion')
        continue
    
    if length<=1:
        print(Dict0[int(n)])
        continue
    
    if int(n) < 20:
        print(Dict1[int(n)])
        continue
    
    if int(n)>=20 and int(n)<100:
        
        if n[1]=='0':
            print(Dict2[int(n[0])])
            continue
        else:
            print(Dict2[int(n[0])]+' '+Dict0[int(n[1])])
            continue
        
    if int(n)<1000:
        if n[1]=='0' and n[2]=='0':
            print(Dict0[int(n[0])]+' Hundred')
            continue
        elif n[1]=='0':
            print(Dict0[int(n[0])]+' Hundred '+Dict0[int(n[2])])
            continue
        elif n[1]=='1':
            print(Dict0[int(n[0])]+' Hundred '+Dict1[int(n[1:3])])
            continue
        elif n[2]=='0':
            print(Dict0[int(n[0])]+' Hundred '+Dict2[int(n[1])])
            continue
        else:
            print(Dict0[int(n[0])]+' Hundred '+Dict2[int(n[1])]+' '+Dict0[int(n[2])])
            continue
        
        
    
    
    
    
        
    
