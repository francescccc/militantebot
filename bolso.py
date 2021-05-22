import tweepy
from tweepy import OAuthHandler
import json
import urllib.request
from PIL import Image, ImageOps
import pyrebase
import math
import random

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


consumer_key = '2jXREqqrVS3wUyXqXJ3WLi0oo'
consumer_secret = 'c9z41ADMyAixWVgb2wWzryBnr9x8tjkW5AbKG1LQuRmpbTw8C3'
access_token = '1354759515363811328-v31fRhBAUTIGJYbOWCRyfVWF5xYAeh'
access_secret = 'J3IOMXZLXAWda5RkKoOTuAA2Yv0ya5qgua66dAhnH6Qep'

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


users = db.child("id2").get()
users1 = users.val()
print(users1)


def reply():
    users3 = db.child("id2").get()
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
                    if str == True:
                        print(tweet.full_text)
                        media_files.add(media[0]['media_url'])
                        for media_file in media_files:
                            urllib.request.urlretrieve(media_file, 'original.png')
                            urllib.request.urlretrieve(media_file, 'original2.png')
                            im1 = Image.open('bolsonaro1.png')
                            im2 = Image.open('original.png')
                            im3 = new_image = im2.resize((515, 296))
                            im1.paste(im3 , (502, 71, 1017, 367))
                            im1.save('1result.png', quality=95)


                            im1 = Image.open('bolsonaro.png')
                            im2 = Image.open('original2.png')
                            im3 = new_image = im2.resize((815, 442))
                            im1.paste(im3 , (320, 35, 1135, 477))
                            im1.save('2result.png', quality=95)


                            number = ('1',
                            '2',
                            

                            )
                            numberident = (random.choice(number))
                            print(numberident)
                            data = { "id2": tweet.id }
                            users = db.update(data)
                            users = db.child("id2").get()
                            users1 = users.val()
                            imagepath = (numberident + ("result.png"))
                            api.update_with_media(imagepath, " @" + tweet.user.screen_name + " Pronto", in_reply_to_status_id = tweet.id)


                



                            

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
                data = { "id2": tweet.id }
                users = db.update(data)
                users = db.child("id2").get()
                users1 = users.val()
        
            else:
                status = api.get_status(tweet.in_reply_to_status_id, tweet_mode='extended')
                print(tweet.in_reply_to_status_id)
                print(status.full_text)
                media_files = set()
                media_files = set()
                media = status.entities.get('media', [])
                print(status.user.screen_name)
                twitterbot = "Bolsobot_" in status.user.screen_name
                twitterbot2 = "distortbott" in status.user.screen_name
                print(twitterbot, twitterbot2)
                if twitterbot == True:
                    print(tweet.user.screen_name, "oi1")
                    data = { "id2": tweet.id }
                    users = db.update(data)
                    users = db.child("id2").get()
                    users1 = users.val()



                else:    
                    if twitterbot2 == True:
                        print(tweet.user.screen_name, "oi1")
                        data = { "id2": tweet.id }
                        users = db.update(data)
                        users = db.child("id2").get()
                        users1 = users.val()

                    else:    
                        if(len(media) > 0):
                            print(status.full_text)
                            media_files.add(media[0]['media_url'])
                            for media_file in media_files:
                                urllib.request.urlretrieve(media_file, 'original.png')
                                urllib.request.urlretrieve(media_file, 'original2.png')
                                im1 = Image.open('bolsonaro1.png')
                                im2 = Image.open('original.png')
                                im3 = new_image = im2.resize((515, 296))
                                im1.paste(im3 , (502, 71, 1017, 367))
                                im1.save('1result.png', quality=95)


                                im1 = Image.open('bolsonaro.png')
                                im2 = Image.open('original2.png')
                                im3 = new_image = im2.resize((815, 442))
                                im1.paste(im3 , (320, 35, 1135, 477))
                                im1.save('2result.png', quality=95)
                                number = ('1',
                                '2',
                                

                                )
                                numberident = (random.choice(number))
                                print(numberident)

                                data = { "id2": tweet.id }
                                users = db.update(data)
                                users = db.child("id2").get()
                                users1 = users.val()
                                imagepath = (numberident + ("result.png"))
                                api.update_with_media(imagepath, " @" + tweet.user.screen_name + " Pronto", in_reply_to_status_id = tweet.id)

                        else:
                            print(tweet.user.screen_name, "oi1")
                            data = { "id2": tweet.id }
                            users = db.update(data)
                            users = db.child("id2").get()
                            users1 = users.val()

                    



while True:
            reply()
            import time
            time.sleep(15)