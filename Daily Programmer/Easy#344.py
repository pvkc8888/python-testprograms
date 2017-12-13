import re

#This function converts decimal number to binary and send as a list
def convert2binary(n):
	binary_number = []
	while True:
		if n%2 == 0:
			binary_number = [0] + binary_number			
			n = int(n/2)			
		elif n%2 == 1:
			binary_number = [1] + binary_number
			n = int(n/2)			
		if n == 0:
			#binary_number = [0] + binary_number
			break
	return binary_number

#regular expression for checking 0's
total = re.compile('0*')
numbers = input('Enter the number of numbers')
print("1",end = "")
for item in range(1,int(numbers)+1):
	binary = convert2binary(item)
	binary = list(map(str,binary))	
	binary = "".join(binary)
	find = total.findall(binary)
	find = list(map(len,find))
	for item in find:
		if item%2 != 0:
			number = 0
			break
		else:
			number = 1
	print(", ",number,end="")
