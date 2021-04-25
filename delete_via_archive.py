import tweepy
import json
import os

auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_KEY'), os.getenv('ACCESS_SECRET'))
api = tweepy.API(auth)

with open('tweet.js', 'r') as file:
    tweets = json.loads(file.read())
    for tweet in tweets:
        tweet_id = int(tweet["tweet"]["id"])
        try:
            api.destroy_status(tweet_id)
            print(f"Deleted tweet {tweet_id}")
        except tweepy.TweepError as e:
            text = e.response.text
            print(text)
            print(f"Skipped tweet {tweet_id}")

