import re, os, shutil

ReqfileName = re.compile(r'.*\.jpg')

CurrentDir = "C:\\Users\\pvkc"
for folders, Sub, files in os.walk(CurrentDir):
        for items in files:
                if ReqfileName.match(items):
                        print(folders,items)
                        #shutil.copy(folders,'C:\\Users\\pvkc\\Desktop\\testfolder')
				
