# -*- coding: utf-8 -*-
import praw
import re
from reddit_credentials import client_id, client_secret, password, user_agent, username
# the following line is not necessary if you have the subreddit names properly organised already in the text file. Since, I am copying from the internet, they have numbers and spaces and stuff, so i am using regex to properly extract the subreddit names.

subreddit = re.compile(r'[a-zA-Z]+')

reddit = praw.Reddit(client_secret=client_secret,
                     client_id=client_id,
                     password=password,
                     username=username,
                     user_agent=user_agent)

listt = []
filename = 'sause.txt'
with open(filename) as file:
    for line in file:
        found = subreddit.findall(line)
        # print(found)
        if found:
            if found[0] == 'i':
                continue
            elif len(found) > 1:
                found = "_".join(found)
                listt.append(found)
            else:
                listt.append(found[0])


for item in listt:
    # try is to pass the subreddits which arent properly named becuase of the numbers in their name. you can try adding them seperately or, changing the regex code.

    try:
        subreddit = reddit.subreddit('{}'.format(item))
        subreddit.subscribe()
        print('subscribed to : {}'.format(item))
    except Exception as e:
        print(e)
        print(item)
