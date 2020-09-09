import tweepy
from time import sleep
from credentials import *
from config import QUERY, LIKE, SLEEP_TIME

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q=QUERY).items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print("retweet done")

        if LIKE:
            tweet.favorite()
            print("like done")

        sleep(SLEEP_TIME)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break