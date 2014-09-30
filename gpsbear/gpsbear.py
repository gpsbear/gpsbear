import twitter
import picamera
from datetime import datetime

def main():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        timestamp = datetime.now().isoformat()
        img = '/home/pi/twitter/%s.jpg' % timestamp
        camera.capture(img)
        camera.stop_preview()
        twitter.tweet("hello", img)

if __name__ == '__main__':
    main()
