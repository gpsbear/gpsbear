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

def tweet(text, img=None):
    if len(text) <= 140:
        if img:
            api.update_with_media(img, text)
        else:
            api.update_status(text)
    else:
        print ("error text too long")

def main():
    img = "/home/pi/twitter/2014-09-30T13:25:45.793735.jpg"
    tweet("hello world with a picture", img)
    
if __name__ == '__main__':
    main()
