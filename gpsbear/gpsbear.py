import twitter
from dot3k import lcd, backlight, joystick
from random import random

@joystick.on(joystick.UP)
def show_follower_count(pin):
    try:
        followers = twitter.follower_count()
        msg = "You have %-6i followers" % followers
    except:
        msg = "Twitter API     limit reached"

    backlight.sweep(random())
    lcd.clear()
    lcd.write(msg)

def main():
    while True:
        pass

if __name__ == '__main__':
    main()
