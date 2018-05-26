import os
import re
from shutil import copyfile

episode = re.compile(r'E\d\d')

os.chdir('D:\\Open Source\\Riverdale.S02')
folder = os.getcwd()
for items in os.listdir(folder):
    print(items)
    episode_number = episode.findall(items)
    print(episode_number)
    os.rename(items, 'S02 ' + episode_number[0] + '.mkv')
