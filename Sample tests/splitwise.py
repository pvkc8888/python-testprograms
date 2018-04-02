def splitwise(Dict, paidby):
    total = sum(Dict.values())
    for keys, values in Dict.items():
        if keys == 'd':
            share = Dict['d'] / 2
            Dict['a'] += share
            Dict['b'] += share
        if keys == 'e':
            share = Dict['e'] / 2
            Dict['a'] += share
            Dict['c'] += share
        if keys == 'f':
            share = Dict['f'] / 2
            Dict['c'] += share
            Dict['b'] += share
        if keys == 'g':
            share = Dict['g'] / 3
            Dict['a'] += share
            Dict['b'] += share
            Dict['c'] += share
    Dict[paidby] -= total
    print(Dict)
    print(''' The final break down of the bill is:
        total = {}$
        Vinay = {}$
        Ibraheem = {}$
        Jerry = {}$'''.format(total, Dict['a'], Dict['b'], Dict['c']))


Dict = {'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0}
count = 0
while True:
    if count == 0:
        print('Enter the price of first item in the list: ')
        price = float(input().strip())
        print('''Which of the following categories does that item belong to:
                    A: Vinay
                    B: Ibraheem
                    C: Jerry
                    D: Vinay + Ibraheem
                    E: Vinay + Jerry
                    F: Ibraheen + Jerry
                    G: All three!''')
        category = input().strip().lower()
        count += 1
    else:
        print('Enter the price of {} item in the list: '.format(count + 1))
        price = float(input().strip())
        print('''Which of the following categories does that item belong to:
                    A: Vinay
                    B: Ibraheem
                    C: Jerry
                    D: Vinay + Ibraheem
                    E: Vinay + Jerry
                    F: Ibraheen + Jerry
                    G: All three!''')
        category = input().strip().lower()
        count += 1
    Dict[category] += price
    print('Do you have more items in the list? Type y or n: ')
    more = input().strip().lower()
    if more == 'n':
        break

print('''who paid this bill?:
    Type a for vinay
         b for Ibraheem
         c for Jerry''')
paidby = input().strip()
print(Dict)
splitwise(Dict, paidby)
