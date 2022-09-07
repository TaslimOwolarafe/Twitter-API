import os, tweepy, dotenv, csv
import webbrowser
import dotenv

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('api_key')
api_key_secret = os.getenv("api_key_secret")
access_token = os.getenv('access_token')
access_token_secret = os.getenv("access_token_secret")

callback_uri = 'oob'
auth = tweepy.OAuthHandler(api_key, api_key_secret, callback=callback_uri)
redirect_url = auth.get_authorization_url()
print(redirect_url)
webbrowser.open(redirect_url)
print(auth.access_token, auth.access_token_secret)
user_pin = input("What is the pin? ")
print(user_pin)
auth.get_access_token(user_pin)

print(auth.access_token, auth.access_token_secret)

api = tweepy.API(auth)
