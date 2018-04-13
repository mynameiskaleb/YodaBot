# -*- coding: utf-8 -*-
"""

	File name: YodaBot.py
	Description: A reddit bot that scans comments for keywords
		then replies to those comments with a mixed up version
		of original comment.
	Author: Kaleb Keith
	Email: kalebkeith@pm.me
	Date Created: Tue Apr 10 2018
	Date Last Modified: Thur Apr 12 2018
	Python Version: 3.5
	
"""

import praw
import time
import sys
import random

reddit = praw.Reddit(client_id='CLIENT_ID', client_secret='CLIENT_SECRET', password='PASSWORD', user_agent='USER_AGENT', username='USERNAME')	# reddit instance

lookforwords = ['star wars', 'yoda', 'the force', 'luke skywalker', 'tatooine', 'princess leah']	# words to look for
cache = []	# if reply successful, add comment id here so not to repeat
block = []	# if reply to comment is stop, add user to this list

def run():
	print('Getting subreddit..')
	sub = reddit.subreddit('all').comments(limit=1000)	# finds 1000 comments in /r/all
	for thing in sub:	# for each comment in comment list
		print('Getting comments..')
		comment_body = thing.body.lower()	# changes all case to lower in comment
		ismatch = any(string in comment_body for string in lookforwords)	# looks for matching words from wordlist
		if thing.id not in cache and ismatch and thing.author not in block:	# makes sure comment id isnt used, a word matches, and author doesn't want stop
				print("I have a match. ID: " + comment.id)	# find match
				thing.reply(mix_comment(comment_body) + '\n\nCreated by [KalebtheKraken](https://www.reddit.com/u/kalebthekraken) this bot was. If annoying I am, reply stop me you will.')	# reply with new mixed comment
				print('Reply successful!!')
				cache.append(thing.id)	# add comment id to list
	print("Finished. Gonna rest a minute.")
                        
#takes a comment and mixes up all the words            
def mix_comment(comment):
	commentlist = comment.split(' ')
	newcommentlist = random.shuffle(commentlist)
	newcomment = ' '.join(newcommentlist)
	return newcomment

#scans inbox for "stop" keyword and adds user to block list    
def look_for_stop():
	print("Let's see here")
	for comment in reddit.inbox.unread(limit=None):
		naked = comment.body.strip().lower()
		if 'stop' in naked:
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
		break
		
sys.exit()
>>>>>>> Updated README. Made a few changes to quit program, program creator info, etc.
