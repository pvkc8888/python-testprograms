def collatz(number):
    if number%2 == 0:
        number = number/2
    else:
        number = number*3+1
    return(number)
try:
    InputNumber = int(input())
    while(InputNumber != 1):
        InputNumber = collatz(InputNumber)
        print(InputNumber)
except:
    print("Enter an integer you >.<")

