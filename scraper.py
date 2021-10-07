import tweepy
import random
consumer_key = '5W3oMtUYziTOjBCXgld62POxW'
consumer_secret = 'm7FhKAwdF8qPez9VTIEvohmEJqbRau2F5Bl3eVtSsoaJRTYifb'
key = '1445235320329490441-Y4wHQevZFQruaweJnMF4hHH8zZg3To'
secret = '3tMYN5e2SPKVbe30mvPTuqqeZHOiFjv7SyGyM2a2JgDvs'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
def tweetsend2():
    with open("names.txt", "r") as file:
        first_line = file.readline()
        for last_line in file:
            pass   

    print(first_line)
    first_line1 = api.get_user(first_line)
    ID = first_line1.id_str
    recipient_id = ID
    text = "Oi, td bem? eu queria perguntar se voce quer participar de um projeto pra ganhar diamantes no freefire. Eu consegui um meio de comprar diamantes mais baratos, convertendo meu dinheiro para euro e comprando na playstore europeia, entao eu consigo comprar o pacote de 310 por 5 reais. Entao, o kwai esta pagando 6 reais por pessoa que colocar o codigo, então eu saio no lucro, e so você me mandar um print comprovando que você usou meu codigo que é Kwai646639844 , e mandar seu Id do freefire e eu vou enviar 510 diamantes."
    try:
        import random
        numvers = ["3",
        "4", 
        "5",
        "1122",
        "22",
        "223",
        "232",
        "2323",
        "23232",
        "34",
        "23",
        "11",
        "222",
        "11221",
        "221",
        "2231",
        "2321",
        "1",
        "a232321",
        "a341",
        "a2221" ,
        "a2311",
        "a111",
        "a5",
        "a1122",
        "a22",
        "a223",
        "a232",
        "a2323",
        "a23232",
        "a34",
        "a23",
        "a11",
        "a222",
        "a11221",
        "a221",
        "a2231",
        "a2321",
        "a1",
        "a232321",
        "a341",
        "a2221" ,
        


        ]
        nn = random.choice(numvers)
        print(nn)
        if nn == "4":
            api.create_friendship(recipient_id)


        api.send_direct_message(recipient_id, text)
        print("fo   dwoqdROVNEWRVIUEWOCVWEBCUILWABKCKEJHBWACi")
    except:
        print("nao foi")
        pass
        
    with open("names.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != first_line:
                f.write(i)
        f.truncate()
while True:
            tweetsend2()
            import time
            time.sleep(15)