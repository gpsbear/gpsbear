import twitter
from dot3k import lcd, backlight
from random import random

def main():
    followers = twitter.follower_count()

    msg = "You have %-6i followers" % followers

    backlight.sweep(random())
    lcd.write(msg)

if __name__ == '__main__':
    main()
