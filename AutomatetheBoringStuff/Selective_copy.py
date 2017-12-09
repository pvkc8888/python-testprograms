import re, os, shutil

ReqfileName = re.compile(r'.*\.jpg$')

CurrentDir = "C:\\Users\\pvkc"
for folders, Sub, files in os.walk(CurrentDir):
        for items in files:
                if ReqfileName.match(items):
                        try:
                                shutil.copy(os.path.abspath(folders)+'\\'+items,'C:\\Users\\pvkc\\Desktop\\testfolder')
                        except:
                                print(folders,files)
                                print('File exists already!')
