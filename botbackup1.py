# -*- coding: utf-8 -*-
import tweepy
import random

consumer_key = 'FPWi4wYbTAHLwux8ll1r9vxtZ'
consumer_secret = 'bBIcQ4FFVoUi0xnbp7TAtrorwtRD6Pt50lvcSQiObdVSQ05wiX'

key = '1353790874463956999-4D5xxVhyleqXzmXzt0Cy2q1zQyBTvk'
secret = 'uWmxPKYDPaOCXvuGwruCffLaqNbwrthDLcZCMNWcGkd6l'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

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
    sn = s.user.screen_name
    copypasta = (' @%s Amigo, isso não tem graça, vc ta tendo uma atitude extremamente machista, não que eu esperasse diferente de um macho branco elitist a%s' 
    ' @%s Você nao deveria fazer esse tipo de piada, isso é extremamento ofensivo a algumas pessoas %s' 
    ' @%s Vocês realmente acham graça nesse tipo de conteudo? que machista %s' 
    ' @%s quando vocês machos brancos heteros vão perceber que vocês estão passando vergonha???? %s'
    % (username_to_reply_to, your_status), 

    )

    copypastas = (random.choice(copypasta))
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '@militantebot_' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status(imagepath, status=f'{copypastas}', in_reply_to_status=tweet_to_reply_to.id)
            store_last_seen(FILE_NAME, tweet.id)
while True:
            reply()
            import time
            time.sleep(15)
            sender['screen_name'],
            in_reply_to_status_id=data['id_str']
