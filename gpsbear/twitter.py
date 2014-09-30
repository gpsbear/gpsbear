import tweepy
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def follower_count():
    followers = api.followers_ids()

    return len(followers)

def tweet(text):
    if len(text) <= 140:
        api.update_status(text)
    else:
        print ("error text too long")

def main():
    tweet("hello world from python")
    
if __name__ == '__main__':
    main()
