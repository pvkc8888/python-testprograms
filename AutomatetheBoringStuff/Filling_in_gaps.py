import re, os,shutil
allfiles = {}
ReqName = re.compile(r'(vinay(\d)*?.txt)')
for folders,subs,files in os.walk("C:\\Users\\pvkc\\Desktop\\test"):
	for file in files:
		#print(file)
		if ReqName.match(file):
			isfile =  ReqName.findall(file)	
			allfiles[folders+'\\'+file] = isfile[0][1]			
number ='1'
for keys,values in allfiles.items():
	if allfiles[keys] == number:
		number = str(int(number)+1)
		shutil.move(keys,"C:\\Users\\pvkc\\Desktop\\test\\vinay"+allfiles[keys]+'.txt')
		continue
	else:
		allfiles[keys] = number
		shutil.move(keys,"C:\\Users\\pvkc\\Desktop\\test\\vinay"+allfiles[keys]+'.txt')
	number = str(int(number)+1)
print(allfiles)