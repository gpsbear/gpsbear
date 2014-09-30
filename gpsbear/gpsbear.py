import twitter
import picamera
from datetime import datetime
from random import choice
import adxl345

messages = [
    "Don't Touch me!",
    "Call Bear Line!",
     "I don't like it when you touch me that way!",
    "Help me!",
    "BABBAGE BEAR NO LIKEY!",
    "Why are you doing this?!",
]

def take_picture_and_tweet():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        timestamp = datetime.now().isoformat()
        img = '/home/pi/twitter/%s.jpg' % timestamp
        message = choice(messages)
        camera.annotate_text = message
        camera.capture(img)
        camera.stop_preview()
        twitter.tweet(message, img)

def main():
    accel = adxl345.ADXL345()
    accel.setRange(adxl345.RANGE_16G)
    xold = 0
    yold = 0
    zold = 0
    while True:
        axes = accel.getAxes(True)
        xnew = axes["x"]
        ynew = axes["y"]
        znew = axes["z"]

        if float(xnew) - float(xold) > 2 or float(xnew) - float(xold) < - 2:
            take_picture_and_tweet()
        elif float(ynew) - float(yold) > 2 or float(ynew) - float(yold) < - 2:
            take_picture_and_tweet()
        elif float(znew) - float(zold) > 2 or float(znew) - float(zold) < - 2:
            take_picture_and_tweet()

        xold = xnew
        yold = ynew
        zold = znew

if __name__ == '__main__':
    main()
