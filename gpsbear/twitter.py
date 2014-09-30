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

def main():
    followers = follower_count()

    print("You have %-6i followers" % followers)

if __name__ == '__main__':
    main()
