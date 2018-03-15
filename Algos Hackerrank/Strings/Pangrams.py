s = input().strip()
string = 'abcdefghijklmnopqrstuvwxyz'
s = s.lower()
for item in string:
    if item in s:
        count += 1
if count == 26:
    print('pangram')
else:
    print('not pangram')
