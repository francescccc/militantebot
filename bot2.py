import tweepy
from tweepy import OAuthHandler
import json
import urllib.request
from PIL import Image, ImageOps
from cv2 import cv2
import numpy as np


consumer_key = 'mecfcpzfGrnQAlFHfaCImOwtG'
consumer_secret = 'HwV0Ezxs3NpNw2WLVSdg1P1v1bmDJteeHZ6yPGKLJ5afBDx2JH'
access_token = '1355583006946242562-jmlVaMVwMCd5RTrzeLzbVJEbMktXiy'
access_secret = 'b6WBVM90uaohiLemabmxZwZIKlppInOxUHyKjllUVGqFB'

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return




def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        print(tweet.id, tweet.full_text)
        tweettext = tweet.full_text
        str = "https://t.co" in tweettext
        tweettext = tweet.full_text
        if str == True:
            for status in tweets:
                print(status)
                media_files = set()
                media = status.entities.get('media', [])
                tweettext = tweet.full_text
                str = "https://t.co" in tweettext
                if(len(media) > 0):
                    if str == True:
                        print(tweet.full_text)
                        media_files.add(media[0]['media_url'])
                        for media_file in media_files:
                            url = media_file
                            urllib.request.urlretrieve(url, 'invert.png')
                            im = Image.open('invert.png')
                            im_mirror = ImageOps.mirror(im)
                            im_mirror.save('invert1.png', quality=95)
                            width = im.width
                            print(width)
                            quotient = width / 2
                            inverted1 = cv2.imread('invert.png')
                            inverted2 = cv2.imread('invert1.png')
                            inverted1_inverted2 = np.hstack((inverted1[:, :int(quotient)], inverted2[:, int(quotient):]))
                            cv2.imwrite('invert3.png', inverted1_inverted2)
                            imagepath = 'invert3.png'
                            api.update_with_media(imagepath, " @" + tweet.user.screen_name + " Pronto", in_reply_to_status_id = tweet.id)
                            store_last_seen(FILE_NAME, tweet.id)

        else:           
            tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
            print(tweet.id)
            status = api.get_status(tweet.in_reply_to_status_id, tweet_mode='extended')
            print(tweet.in_reply_to_status_id)
            print(status.full_text)
            media_files = set()
            media_files = set()
            media = status.entities.get('media', [])
            if(len(media) > 0):
                print(status.full_text)
                media_files.add(media[0]['media_url'])
                for media_file in media_files:
                    url = media_file
                    urllib.request.urlretrieve(url, 'invert.png')
                    im = Image.open('invert.png')
                    im_mirror = ImageOps.mirror(im)
                    im_mirror.save('invert1.png', quality=95)
                    width = im.width
                    print(width)
                    quotient = width / 2
                    inverted1 = cv2.imread('invert.png')
                    inverted2 = cv2.imread('invert1.png')
                    inverted1_inverted2 = np.hstack((inverted1[:, :int(quotient)], inverted2[:, int(quotient):]))
                    cv2.imwrite('invert3.png', inverted1_inverted2)
                    imagepath = 'invert3.png'
                    api.update_with_media(imagepath, " @" + tweet.user.screen_name + " Pronto", in_reply_to_status_id = tweet.id)
                    store_last_seen(FILE_NAME, tweet.id)


            else:
                api.update_status(" @" + tweet.user.screen_name + " Por favor, especifique a imagem que você quer que eu edite", in_reply_to_status_id = tweet.id)
                print(" Por favor, especifique a imagem que você quer que eu edite")





while True:
            reply()
            import time
            time.sleep(15)
