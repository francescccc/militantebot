import tweepy
from tweepy import OAuthHandler
import json
import urllib.request
from PIL import Image, ImageOps
import pyrebase
import math

config = {
    "apiKey": "AIzaSyD1s2TKUXZcUVTpOtqfqTQm8AAbV2R7HdE",
    "authDomain": "tweet-bb608.firebaseapp.com",
    "projectId": "tweet-bb608",
    "storageBucket": "tweet-bb608.appspot.com",
    "messagingSenderId": "271208042340",
    "appId": "1:271208042340:web:f89694e1c054976c5bf471",
    "measurementId": "G-PF3FJ5R1NE",
    "databaseURL": "https://tweet-bb608-default-rtdb.firebaseio.com",
    "serviceAccount": "serviceAccountCredentials.json",
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()


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


users = db.child("id1").get()
users1 = users.val()
print(users1)


def reply():
    users3 = db.child("id1").get()
    print(users3.val())
    global users1
    tweets = api.mentions_timeline(users1, tweet_mode='extended')
    print(users1, "uweo")
    for tweet in reversed(tweets):
        print(tweet.id, tweet.full_text)
        tweettext = tweet.full_text
        str = "https://t.co" in tweettext
        tweettext = tweet.full_text
        if str == True:
            for status in tweets:
                media_files = set()
                media = status.entities.get('media', [])
                tweettext = tweet.full_text
                str = "https://t.co" in tweettext
                if(len(media) > 0):
                    twitterbot = "invertbot_" in tweet.user.screen_name
                    twitterbot2 = "distortbott" in tweet.user.screen_name
                    if twitterbot == False:
                        if twitterbot2 == False:
                            if str == True:
                                print(tweet.full_text)
                                media_files.add(media[0]['media_url'])
                                for media_file in media_files:
                                    urllib.request.urlretrieve(media_file, 'original.png')
                                    original = Image.open('original.png')
                                    inverted = ImageOps.mirror(original)
                                    print(original.width)
                                    cropwidth = original.width // 2
                                    print(cropwidth)
                                    img = inverted
                                    x1 = img.width // 2
                                    y1 = 0
                                    x2 = img.width
                                    y2 = img.height
                                    cropped = img.crop((x1, y1, x2, y2))
                                    cropped.save('crop.png', quality=95)
                                    
                                    im1 = Image.open('original.png')
                                    im2 = Image.open('crop.png')

                                    im1.paste(cropped, (original.width // 2, 0))
                                    im1.save('result.png', quality=95)

                                    data = { "id1": tweet.id }
                                    users = db.update(data)
                                    users = db.child("id1").get()
                                    users1 = users.val()
                                    api.update_with_media('result.png', " @" + tweet.user.screen_name + " Pronto", in_reply_to_status_id = tweet.id)


                        else:
                            data = { "id1": tweet.id }
                            users = db.update(data)
                            users = db.child("id1").get()
                            users1 = users.val()

                    else:
                        data = { "id1": tweet.id }
                        users = db.update(data)
                        users = db.child("id1").get()
                        users1 = users.val()



                                    

                else:     
                    users3 = db.child("id").get()
                    print(users3.val())      
                    tweets = api.mentions_timeline(users1, tweet_mode='extended')
                    print(users1, "uweo")
                    print(tweet.id)
                    str1 = tweet.in_reply_to_status_id
                    if str1 is None:
                        api.update_status(" @" + tweet.user.screen_name + " Por favor, especifique a imagem que você quer que eu edite", in_reply_to_status_id = tweet.id)
                        print(" Por favor, especifique a imagem que você quer que eu edite")
                        data = { "id1": tweet.id }
                        users = db.update(data)
                        users = db.child("id1").get()
                        users1 = users.val()
                
                    else:
                        status = api.get_status(tweet.in_reply_to_status_id, tweet_mode='extended')
                        print(tweet.in_reply_to_status_id)
                        print(status.full_text)
                        media_files = set()
                        media_files = set()
                        media = status.entities.get('media', [])
                        if(len(media) > 0):
                            twitterbot = "invertbot_" in status.user.screen_name
                            twitterbot2 = "distortbott" in status.user.screen_name
                            if twitterbot == False:
                                if twitterbot2 == False:
                                    print(status.full_text)
                                    media_files.add(media[0]['media_url'])
                                    for media_file in media_files:
                                        urllib.request.urlretrieve(media_file, 'original.png')
                                        original = Image.open('original.png')
                                        inverted = ImageOps.mirror(original)
                                        inverted.save('inverted.png', quality=95)
                                        print(original.width)
                                        cropwidth = original.width // 2
                                        print(cropwidth)
                                        img = Image.open('inverted.png')
                                        x1 = img.width // 2
                                        y1 = 0
                                        x2 = img.width
                                        y2 = img.height
                                        cropped = img.crop((x1, y1, x2, y2))
                                        cropped.save('crop.png', quality=95)
                                        
                                        im1 = Image.open('original.png')
                                        im2 = Image.open('crop.png')

                                        im1.paste(im2, (original.width // 2, 0))
                                        im1.save('result.png', quality=95)

                                        data = { "id1": tweet.id }
                                        users = db.update(data)
                                        users = db.child("id1").get()
                                        users1 = users.val()
                                        api.update_with_media('result.png', " @" + tweet.user.screen_name + " Pronto", in_reply_to_status_id = tweet.id)

                                else:
                                    data = { "id1": tweet.id }
                                    users = db.update(data)
                                    users = db.child("id1").get()
                                    users1 = users.val()

                            else:
                                data = { "id1": tweet.id }
                                users = db.update(data)
                                users = db.child("id1").get()
                                users1 = users.val()

                        else:
                            data = { "id1": tweet.id }
                            users = db.update(data)
                            users = db.child("id1").get()
                            users = users.val()



while True:
            reply()
            import time
            time.sleep(15)
