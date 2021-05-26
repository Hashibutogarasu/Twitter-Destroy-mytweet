import sys
import time
import tweepy
import config

tweet_content_destroy = "" #ツイ消しする内容

if (len(tweet_content_destroy)==0):
	print("ツイ消しする内容を一文字以上入れてください。")
	sys.exit()

auth = tweepy.OAuthHandler(config.ck, config.cs)
auth.set_access_token(config.at, config.ats)
api = tweepy.API(auth)

me = api.me()

i = 0

while True:

    for status in api.user_timeline(me.screen_name,page=i):
	
            if ((tweet_content_destroy in status.text) == True):	
                print(status.text)
                print(status.id)
                api.destroy_status(status.id)
                print("ツイ消ししました。")
                i = i + 1
                time.sleep(300)
                
#5分間にiページ目のツイートを取得し、その文字列が含まれてる場合に削除します。iでページ数を変えています。
