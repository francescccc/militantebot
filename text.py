import tweepy
import random
consumer_key = 'A8RIFnOvzltv3Ct9dX0kyaGee'
consumer_secret = '8D7n1tKUI3kZbyC7V33t2F9kgtHzvODY5tpVTVyFc2NmtiyNFl'
key = '1445596367502512136-c0K1T1SdaBDpY1AYWbJs4BQklYiqyx'
secret = '7pBDsThNOe6u7BPq2X7RddB1DSAo1Sgtca7R2DXjfljkO'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
def tweetsend2():
    with open("names1.txt", "r") as file:
        first_line = file.readline()
        for last_line in file:
            pass   

    print(first_line)
    first_line1 = api.get_user(first_line)
    ID = first_line1.id_str
    recipient_id = ID
    text = "Oii, desculpa o incomodo, eu só queria pedir, pra que se caso você pudesse me ajudar, eu to passando por umas situações financeiras em casa muito difíceis mesmo, e eu não me sinto confortavel pedindo doação, pq eu sei que tem gente que precisa bem mais que eu, ent o unico jeito que eu achei foi o kwai, se você puder usar meu código ou pedir pra alguém usar, ia me ajudar muito, de vdd, só se não for um incômodo pra você. Meu código é Kwai646639844 , é bem facil de fazer, é só criar uma conta, clicar na moedinha e colocar o código. Obrigada!!"
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
        
    with open("names1.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != first_line:
                f.write(i)
        f.truncate()
while True:
            tweetsend2()
            import time
            time.sleep(70)