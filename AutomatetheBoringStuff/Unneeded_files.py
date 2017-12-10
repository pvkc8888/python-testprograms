import os
os.chdir('C:\\')
ReqDir = os.getcwd()
max = 0
for folders,sub,files in os.walk(ReqDir):
	os.chdir(folders)
	for file in files:
		try:
			filesize = os.path.getsize(file)
			if filesize > 100000000:
				print(file,': ',filesize,'is located at ',folders)
		except FileNotFoundError as e:
			continue
