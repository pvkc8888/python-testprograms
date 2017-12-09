import re
print("Enter the new password:")
string = input()
lowercase = re.compile(r'''(
	([a-z]+)
		)''',re.VERBOSE)
uppercase = re.compile(r'''(
	([A-Z]+)
		)''',re.VERBOSE)
numericl = re.compile(r'''(
	([0-9]+)
		)''',re.VERBOSE)

if len(string)>8:
	if lowercase.search(string):
		if uppercase.search(string):
			if numericl.search(string):
				print('Password is strong!')
			else:
				print('No number :(')
		else:
			print('No Uppercase characters!')
	else:
		print('No lowercase characters!')
else:
	print('Less than 8 characters long!')