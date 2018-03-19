# -*- coding: utf-8 -*-
import praw
from reddit_credentials import client_id, client_secret, password, user_agent, username

reddit = praw.Reddit(client_secret=client_secret,
                     client_id=client_id,
                     password=password,
                     username=username,
                     user_agent=user_agent)

subreddit = reddit.subreddit('books')
BigDict = {
    0: {},
    1: {},
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
    8: {},
    9: {},
    10: {},
    11: {},
    12: {},
    13: {},
    14: {},
    15: {},
    16: {}
}
excepted_list = []
submission = reddit.submission(url='https://www.reddit.com/r/books/comments/7orehn/what_is_the_one_book_you_read_which_made_you/?sort=top')
count = 0
submission.comment_sort = 'top'
temp = 0
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    count += 1
    parent = str(comment.parent())
    if parent == submission.id:
        BigDict[0][comment.id] = [comment.body, comment.ups]
    else:
        if parent not in BigDict[temp]:
            temp += 1
            BigDict[temp + 1][comment.id] = [comment.body, comment.ups, parent]
        else:
            BigDict[temp + 1][comment.id] = [comment.body, comment.ups, parent]

filename = 'sauce.txt'
# print(BigDict)
with open(filename, 'w') as file:
    for k, v in BigDict.items():
        if len(BigDict[k]) > 0:
            if k == 0:
                for items in v:
                    if BigDict[k][items][1] > 50:
                        try:
                            file.write(BigDict[k][items][0])
                            file.write('  Upvotes: {}\n'.format(BigDict[k][items][1]))
                            file.write('\n')
                        except Exception as e:
                            print(str(e))
            else:
                for items in v:
                    if BigDict[k][items][1] > 50:
                        try:
                            file.write(BigDict[k][items][0])
                            file.write('  Upvotes: {}\n'.format(BigDict[k][items][1]))
                            file.write('\n')
                            print()
                            file.write('The above comment is in reply to: {}\n '.format(BigDict[k - 1][BigDict[k][items][2]][0]))
                        except Exception as e:
                            print(str(e))
            file.write('------' * 20 + '\n')
            file.write('this is the end of level {} of comments \n'.format(k))
            file.write('------' * 20 + '\n')
