def prod(listt):
    temp = 1
    for item in listt:
        temp *= item
    return temp


def do_the_thing(listt):
    for i in range(len(listt)):
        listt[i] = prod(listt[i])
    return listt


listt = [[1, 1, 1], [1, 2, 3]]

listt = do_the_thing(listt)

print(listt)
