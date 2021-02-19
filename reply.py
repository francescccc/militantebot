#!-*- conding: utf8 -*-
import tweepy
import random
import time

auth = tweepy.OAuthHandler('FPWi4wYbTAHLwux8ll1r9vxtZ',
                           'bBIcQ4FFVoUi0xnbp7TAtrorwtRD6Pt50lvcSQiObdVSQ05wiX')
auth.set_access_token('1353790874463956999-4D5xxVhyleqXzmXzt0Cy2q1zQyBTvk',
                      'uWmxPKYDPaOCXvuGwruCffLaqNbwrthDLcZCMNWcGkd6l')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = '#militantebot'
numero = 100
copypasta = (' Amigo, isso não tem graça, vc ta tento uma atitude extremamente machista, não que eu esperasse diferente de um macho branco elitista',
' Você nao deveria fazer esse tipo de piada, isso é extremamento ofensivo a algumas pessoas',
' Vocês realmente acham graça nesse tipo de conteudo? que machista',
' quando vocês machos brancos heteros vão perceber que vocês estão passando vergonha????',

)
copypastas = (random.choice(copypasta))
search = '#militantebot'
numero = 1
for tweet in tweepy.Cursor(api.search, search).items(numero):
    try:    
            print("nome do usuario: @" + tweet.user.screen_name)
            api.update_status("@" + tweet.user.screen_name + f'{copypastas}', tweet.id)
            time.sleep(30)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

    