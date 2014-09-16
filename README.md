# twittertron3000

A little Python app to display Tweets on the [Display-O-Tron 3000](http://shop.pimoroni.com/products/displayotron-3000) - a [Raspberry Pi](http://www.raspberrypi.org/) add-on board by [Pimoroni](http://shop.pimoroni.com/). A work in progress.

## Requirements

### Hardware

- Raspberry Pi ([Model B+](http://www.raspberrypi.org/products/model-b-plus/), [Model B](http://www.raspberrypi.org/products/model-b/) or [Model A](http://www.raspberrypi.org/products/model-a/))
- [Display-O-Tron 3000](http://shop.pimoroni.com/products/displayotron-3000) from Pimoroni

### Software

- Python 2.7
- tweepy
- dot3k

Installation:

```bash
sudo apt-get install pip
sudo pip install tweepy dot3k
```

Also see dot3k's requirements at [pimoroni/dot3k](https://github.com/pimoroni/dot3k/tree/master/python)

#### Python 3

Unfortunately the dependencies don't support Python 3. Blame `smbus` and `tweepy`. I'm sorry.

## Twitter Application Setup

Set up a Twitter application at [dev.twitter.com](https://dev.twitter.com/) - see instructions at [raspi.tv](http://raspi.tv/2013/how-to-create-a-twitter-app-on-the-raspberry-pi-with-python-tweepy-part-1)

Then copy the relevant API keys in to the [auth.py](twittertron/auth.py)

## Licence

Unless otherwise specified, everything in this repository is covered by the following licence:

[![Creative Commons Attribution 4.0 International Licence](http://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

***twittertron3000*** by [Ben Nuttall](https://github.com/bennuttall) of the [Raspberry Pi Foundation](http://www.raspberrypi.org) is licensed under a [Creative Commons Attribution 4.0 International Licence](http://creativecommons.org/licenses/by-sa/4.0/).

Based on a work at https://github.com/bennuttall/twittertron3000
