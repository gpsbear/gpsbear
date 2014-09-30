import twitter
import picamera
from datetime import datetime
from random import choice

messages = [
    "Don't Touch me!",
    "Call Bear Line!",
     "I don't like it when you touch me that way!",
    "Help me!",
    "BABBAGE BEAR NO LIKEY!",
    "Why are you doing this?!",
]

def main():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        timestamp = datetime.now().isoformat()
        img = '/home/pi/twitter/%s.jpg' % timestamp
        message = choice(messages)
        camera.annotate_text = message
        camera.capture(img)
        camera.stop_preview()
        twitter.tweet(message, img)

if __name__ == '__main__':
    main()
