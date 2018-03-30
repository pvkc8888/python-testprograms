import os
from shutil import copyfile

# set the directory path that you want
path = "D:\Open Source\Wallpapers\850 Amazing Nature\Wallpapers"
os.chdir(path)


count = 1
# walk through all the files in that directory
for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith((".jpg")):
            # copyfile(src, dst)
            print(os.sep.join([root, name]))
            # copyfile() is useful to copy files
            # os.sep.join(rootname with the name to get the abs path of the file)
            # second argument is just where you want to copy the file to.
            copyfile(os.sep.join([root, name]), "D:\Open Source\Wallpapers\850 Amazing Nature\\" + str(count) + ".jpg")
            count += 1
print(count)
