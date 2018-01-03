t = int(input().strip())
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
    
def hundreds(n):
    if int(n)==0:
        return None
    if n[0]=='0':
        n = n[1:]
        print(n)
    if int(n)==0:
        return None
    if int(n)<10:
        string = Dict0[int(n)]
        return string
    
    elif int(n) < 20:
        string = Dict1[int(n)]
        return string

    elif int(n)>=20 and int(n)<100:
        if n[1]=='0':
            string = Dict2[int(n[0])]
            return string
        else:
            string = Dict2[int(n[0])]+' '+Dict0[int(n[1])]
            return string
    else:
        if n[1]=='0' and n[2]=='0':
            string = (Dict0[int(n[0])]+' Hundred')
        elif n[1]=='0':
            string = (Dict0[int(n[0])]+' Hundred '+Dict0[int(n[2])])
        elif n[1]=='1':
            string = (Dict0[int(n[0])]+' Hundred '+Dict1[int(n[1:3])])
        elif n[2]=='0':
            string = (Dict0[int(n[0])]+' Hundred '+Dict2[int(n[1])])
        else:
            string = (Dict0[int(n[0])]+' Hundred '+Dict2[int(n[1])]+' '+Dict0[int(n[2])])
    return string


for a0 in range(t):
    n = int(input().strip())
    n = str(n)    
    length = len(n)
    if int(n)==0:
        print('Zero')
        continue    
    
    if int(n) == 1000000000000:
        print('Thousand Billion')
        continue
    
    if int(n)<1000:        
        print(hundreds(n))
        continue
    
    if int(n)<1000000:
        if hundreds(n[-3:])!= None:
            print(hundreds(n[0:length-3])+' Thousand '+hundreds(n[-3:]))
            continue

        else:
            print(hundreds(n[0:length-3])+' Thousand ')
            continue
    
    if int(n)<1000000000:
        if hundreds(n[-3:])== None and hundreds(n[length-6:length-3]) == None:
            print(hundreds(n[0:length-6])+' Million ')
            continue

        elif hundreds(n[-3:])==None and hundreds(n[length-6:length-3]) != None:
            print(hundreds(n[0:length-6])+' Million '+hundreds(n[length-6:length-3])+' Thousand')
            continue

        elif hundreds(n[-3:])!=None and hundreds(n[length-6:length-3]) == None:
            print(hundreds(n[0:length-6])+' Million '+hundreds(n[-3:]))
            continue

        else:
            print(hundreds(n[0:length-6])+' Million '+hundreds(n[length-6:length-3])+' Thousand '+hundreds(n[-3:]))
            continue

    else:
        if hundreds(n[-3:])== None and hundreds(n[length-6:length-3]) == None and hundreds(n[length-9:length-6]) == None:
            print(hundreds(n[0:length-9])+' Billion ')
            continue

        elif hundreds(n[-3:])== None and hundreds(n[length-6:length-3]) == None and hundreds(n[length-9:length-6]) != None:
            print(hundreds(n[0:length-9])+' Billion '+hundreds(n[length-9:length-6])+' Million ')
            continue

        elif hundreds(n[-3:])== None and hundreds(n[length-6:length-3]) != None and hundreds(n[length-9:length-6]) == None:
            print(hundreds(n[0:length-9])+' Billion '+hundreds(n[length-6:length-3])+' Thousand ')
            continue

        elif hundreds(n[-3:])== None and hundreds(n[length-6:length-3]) != None and hundreds(n[length-9:length-6]) != None:
            print(hundreds(n[0:length-9])+' Billion '+hundreds(n[length-9:length-6])+' Million '+hundreds(n[length-6:length-3])+' Thousand ')
            continue

        elif hundreds(n[-3:])!= None and hundreds(n[length-6:length-3]) == None and hundreds(n[length-9:length-6]) == None:
            print(hundreds(n[0:length-9])+' Billion '+hundreds(n[-3:]))
            continue

        elif hundreds(n[-3:])!= None and hundreds(n[length-6:length-3]) == None and hundreds(n[length-9:length-6]) != None:
            print(hundreds(n[0:length-9])+' Billion '+hundreds(n[length-9:length-6])+' Thousand '+hundreds(n[-3:]))
            continue

        elif hundreds(n[-3:])!= None and hundreds(n[length-6:length-3]) != None and hundreds(n[length-9:length-6]) == None:
            print(hundreds(n[0:length-9])+' Billion '+hundreds(n[length-6:length-3])+' Thousand '+hundreds(n[-3:]))
            continue

        else:
            print(hundreds(n[0:length-9])+' Billion '+hundreds(n[length-9:length-6])+' Million '+hundreds(n[length-6:length-3])+' Thousand '+hundreds(n[-3:]))
            continue
