# -*- coding: utf-8 -*-
import tweepy
import random


consumer_key = 'zc5f5LIwKCwcit5jn7G61HUca'
consumer_secret = 'GsMJ7pgPuhESAp2XC1pRvsXn2MtqNdOFVbBr9tOI7MNUiTeQud'

key = '1365410449664208904-O52PkPj6mHfNPmUgZZFwNlKJxCYKMJ'
secret = 'sqVEqF6kvwDxjQifIrB6CBH4bDfBNreb5xjehGMqBeWz0'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)








def tweetsend2():
    print("oi")
    public_tweets = api.search(q='bts -filter:retweets', count=1, geocode="-11.800399,-48.339055,1800km", since="2018-06-09", tweet_mode="extended")
    for tweet in public_tweets:
        print(tweet.full_text)
        print(tweet.user.id)
        recipient_id = tweet.user.id
        text = "Oiii, você poderia por favor dar um olhada no meu fixado? Eu to passando por umas situações meio dificeis, e em 30 segundos você poderia me ajudar sem gastar nada, por favor, eu realmente preciso"
        try:
            number = ('1',
            '2',
            '3',

            )
            numberident = (random.choice(number))
            print(numberident)
            api.send_direct_message(recipient_id, text)
            numberchance = "2" in numberident
            if numberchance == True:
                try:
                    api.create_friendship(tweet.user.id)
                except:
                    print("deu erro")
        except:
            pass



while True:
            tweetsend2()
            import time
            time.sleep(180)
