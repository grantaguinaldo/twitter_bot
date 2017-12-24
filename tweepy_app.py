#Imports
import tweepy
import json
import requests as r
import numpy as np
import time
from twitter_keys import Consumer_Key, Consumer_API_Secret, Access_Token, Access_Token_Secret

auth = tweepy.OAuthHandler(Consumer_Key, Consumer_API_Secret)
auth.set_access_token(Access_Token, Access_Token_Secret)
api = tweepy.API(auth, parser = tweepy.parsers.JSONParser())

#Get last tweet text and ID an store from twitter.
def tweet_check():
    print('Starting')
    public_tweets = api.search('@grantaguinaldo', result_type = 'recent')

    last_tweet_id = public_tweets['statuses'][0]['id']
    last_tweet_text = public_tweets['statuses'][0]['text']
    last_tweet_user = public_tweets['statuses'][0]['user']['screen_name']

    try:
        #Reply to last tweet with status_text in twitter.
        status_text = 'Thank you come again. This response is from a bot that I made in python!'
        public_tweets = api.update_status(status_text, in_reply_to_status_id = last_tweet_id)

    except:
        #If status has been replied to, then print to console.
        print('I already replied to this tweet!  I\'ll check in 15 seconds')

while(True):
    tweet_check()
    time.sleep(15)
