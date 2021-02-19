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
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '@militantebot_' in tweet.full_text.lower():
            copypasta = (' Amigo, isso não tem graça, vc ta tendo uma atitude extremamente machista, não que eu esperasse diferente de um macho branco elitista',
            ' Você nao deveria fazer esse tipo de piada, isso é extremamento ofensivo a algumas pessoas',
            ' Vocês realmente acham graça nesse tipo de conteudo? que machista',
            ' quando vocês machos brancos heteros vão perceber que vocês estão passando vergonha????',
            ' nossa quanta radiação, ta parecendo chernobyl',
            ' kkkkkkkkkkk passou vergonha',
            ' nossa, que ridiculo, não ter vergonha de ser tão machista?',
            ' essa vergonha eu não passo',
            ' como você tem coragem de falar uma coisa dessas????? a vergonha meu pai',
            ' amigo, algumas pessoas podem ficar muito desconfortaveis lendo isso, por favor apaga',
            ' generalizando os outros assim, a vergonha meu pai',
            ' por que vc n pensa antes de falar as coisas??? tem gente que se ofende',
            ' esse tipo de piada nem devia existir, machista',
            ' típico de macho hetéro, essa vergonha eu não passo kkkkkkkkkkkkkkkkk',
            ' chocada que em pleno 2021 ainda tem gente que pensa assim',
            ' Vcs realmente tem coragem de fazer esse tipo de gente nem merece atenção',
            ' kkkkkkkkk os cis héteros brancos tudo se doendo'

            )

            number = ('1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',                        
            '12',
            '13',
            '14',

            )


            copypastas = (random.choice(copypasta))
            print(copypastas)
            numberident = (random.choice(number))
            print(numberident)
            imagepath = (numberident + ("gret.jpg"))
            print(imagepath)
            print(str(tweet.id) + ' - ' + tweet.full_text)
            store_last_seen(FILE_NAME, tweet.id)
            api.update_with_media(imagepath, " @" + tweet.user.screen_name + f'{copypastas}', in_reply_to_status_id = tweet.id)

while True:
            reply()
            import time
            time.sleep(15)
