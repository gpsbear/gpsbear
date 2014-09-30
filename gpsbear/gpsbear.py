import twitter
import picamera
from datetime import datetime
from random import choice
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

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
        GPIO.wait_for_edge(17, GPIO.FALLING)
        camera.capture(img)
        camera.stop_preview()
        twitter.tweet(message, img)

if __name__ == '__main__':
    main()
