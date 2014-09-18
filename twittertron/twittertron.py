import twitter
from dot3k import lcd

def main():
    followers = twitter.follower_count()

    msg = "You have %-6i followers" % followers

    lcd.write(msg)

if __name__ == '__main__':
    main()
