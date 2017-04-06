import praw
from time import sleep

bot = praw.Reddit(user_agent='SpreadHappiness v0.1',
	client_id='******',
	client_secret ='########',
	username ='insert_username_here',
	password ='insert_password_here')

subreddit = bot.subreddit('wholesomememes')

comments = subreddit.stream.comments()


for comment in comments:
	text = comment.body
	author = comment.author
	if(author!='username'):
		message = "I hope you have a wonderful day. u/{0}, I am a bot :-), My Aim in life is to Spread Happiness".format(author)
		comment.reply(message)
	sleep(10)