import tweepy
import time
import ctypes
import sys

# Matheus Eduardo
# github.com/eumts

# - Definindo variáveis -

CONSUMER_KEY = " "
CONSUMER_SECRET = " "
ACCESS_KEY = " "
ACCESS_SECRET = " "

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.me()
print("Logado como " + user.name)
print()

# Função para tweets apenas com a palavra

def fav_tweet_calor():
    print()
    print("=-=-=-=-=-=-=-=-=-=-=")
    print("Procurando tweets...")
    print("=-=-=-=-=-=-=-=-=-=-=")
    print()
    resultados = api.search(q="calor", tweet_mode = "extended") # lang="pt-br" geocode = "xx.xxxxxx,xx.xxxxxx,xkm"      q="" é a query, palavra que vai buscar no tweet
    for resultado in reversed(resultados):
        arquivo_calor = open('curtidas_calor.txt','r')
        conteudo_calor = arquivo_calor.read()
        try:
            if (str(resultado.id) in conteudo_calor):
                print("Já retweetamos o tweet de @" + resultado.user.screen_name)
            else:
                if (resultado.user.screen_name == "bot_calor"):
                    print("euzinho") # Tentando interagir com um tweet meu
                else:
                    arquivo_calor.close()
                    print()
                    print(str(resultado.user.screen_name) + ' - ' + resultado.full_text, flush=True) # @Mtss_e - Nossa que calor!!!
                    print()
                    print()
                    print("Encontrado", flush=True)
                    print("Curtindo e retweetando...", flush=True)
                    print()
                    arquivo_calor = open('curtidas_calor.txt','a')
                    arquivo_calor.write(str(resultado.id) + "\n")
                    api.create_favorite(resultado.id)
                    api.retweet(resultado.id)
                    arquivo_calor.close()
        except tweepy.TweepError as e:
            print(e.reason)

# Função para menções

def fav_tweet_menção():
    print()
    print("=-=-=-=-=-=-=-=-=-=-=")
    print("Procurando menções...")
    print("=-=-=-=-=-=-=-=-=-=-=")
    print()
    mentions = api.mentions_timeline(tweet_mode = 'extended', lang="pt-br")
    for mention in reversed(mentions):
        arquivo_mencao = open('curtidas_mencao.txt','r')
        conteudo_mencao = arquivo_mencao.read()
        try:
            if (str(mention.id) in conteudo_mencao):
                print("Já retweetamos o tweet de @" + mention.user.screen_name)
            else:
                if (mention.user.screen_name == "bot_calor"):
                        print("euzinho")
                else:
                    arquivo_mencao.close()
                    print()
                    print(str(mention.user.screen_name) + ' - ' + mention.full_text, flush=True) # @Mtss_e - Caramba, esse @bot_calor tá bombando mesmo né!!!
                    print()
                    print()
                    print("Encontrado", flush=True)
                    print("Curtindo e retweetando...", flush=True)
                    print()
                    arquivo_mencao = open('curtidas_mencao.txt','a')
                    arquivo_mencao.write(str(mention.id) + "\n")
                    api.create_favorite(mention.id)
                    api.retweet(mention.id)
                    arquivo_mencao.close()
        except tweepy.TweepError as e:
            print(e.reason)

# Loop

while True:
    fav_tweet_calor()
    fav_tweet_menção()
    time.sleep(30)
