import tweepy
from dot3k import lcd
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def main():
    followers = api.followers_ids()

    msg = "You have %-6i followers" % len(followers)

    lcd.write(msg)

if __name__ == '__main__':
    main()
