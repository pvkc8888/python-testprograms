#!/usr/bin/env python
#def comma code
def comma_code(GivenList):
    print("'",end = '');
    for x in range(len(GivenList)-1):
        print(GivenList[int(x)]+ ', ',end = '');
    print('and '+ GivenList[len(GivenList)-1]+"'");


print("Enter the elements in the list or enter empty string to continue")
userlist = []
while True:
    element = input()
    if element == "":
        break
    else:
        userlist.append(element)
comma_code(userlist)
