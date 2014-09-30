import twitter

def main():
    follower_count = twitter.follower_count()
    print("You have %s followers" % follower_count)

if __name__ == '__main__':
    main()
