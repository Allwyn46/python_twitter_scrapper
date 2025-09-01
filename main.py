import tweepy
from tweepy import OAuthHandler
from dotenv import load_dotenv
import os

load_dotenv()

consumer_key = os.getenv("TW_CONSUMER_KEY")
consumer_secret = os.getenv("TW_CONSUMER_SECRET")
access_token = os.getenv("TW_ACCESS_TOKEN")
access_secret = os.getenv("TW_ACCESS_SECRET")

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

# READ TIMELINE
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)
