import tweepy
import dotenv

import csv

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('api_key')
api_key_secret = os.getenv("api_key_secret")
access_token = os.getenv('access_token')
access_token_secret = os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

new_status = api.update_status("Ohayo!")

public_tweets = api.home_timeline()

header = ["USERNAME", "TWEET", "TIME"]
tweets = []

for tweet in public_tweets:
    tweets.append([tweet.user.screen_name, tweet.text, tweet.created_at])

with open('tweets.csv', 'w', encoding='UTF8', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(tweets)
