# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:53:37 2018

@author: kaleb
"""

import praw
import time
import random

reddit = praw.Reddit(client_id='-HGLGdigUxHTYA', client_secret='u_KwRmLl1sX1XXp86ehaDRWGnLE', password='awxdrv196^^', user_agent='A bot that speaks Yoda with users on reddit created by /u/KalebtheKraken', username='TheYodaBot')

lookforwords = ['star wars', 'yoda', 'the force', 'luke skywalker', 'tatooine', 'princess leah']
cache = []
block = []

total = len(cache)

def run():
    print('Getting subreddits..')
    subreddit = reddit.subreddit('all').hot(limit=None)
    comments = subreddit.replies
    print('Getting comments..')
    for comment in comments:
        comment_body = comment.body.lower()
        ismatch = any(string in comment_body for string in lookforwords)
        if comment.author not in block:
            if comment.id not in cache and ismatch:
                print("I have a match. ID: "+comment.id)
                comment.reply(mix_comment(comment_body+'\n\nCreated by [KalebtheKraken](https://www.reddit.com/u/kalebthekraken) this bot was. If annoying I am, ban me you will.'))
                print('Reply successful!!')
                cache.append(comment.id)
    print("Finished. Gonna rest a minute.")
            
            
            
def mix_comment(comment):
    commentlist = comment.split(' ')
    newcommentlist = random.shuffle(commentlist)
    newcomment = ' '.join(newcommentlist)
    return newcomment
    
def look_for_stop():
    print("Let's see here")
    for comment in reddit.inbox.unread(limit=None):
        naked = comment.body.strip().lower()
        if naked == 'stop':
            block.append(comment.author)
            comment.reply('The force is weak with this one.')
            print("User blacklisted")
            reddit.message.mark_read()
        else:
            pass
        
    
while True:
    try:
        run()
        look_for_stop()
        time.sleep(60)
    except:
        pass
