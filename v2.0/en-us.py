import tweepy
import time
import ctypes
import sys

# Matheus Eduardo
# github.com/eumts

# - Setting variables -

CONSUMER_KEY = " "
CONSUMER_SECRET = " "
ACCESS_KEY = " "
ACCESS_SECRET = " "

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.me()
print("Logged as " + user.name)
print()

# Words only tweets

def fav_tweet_calor():
    print()
    print("=-=-=-=-=-=-=-=-=-=-=")
    print("Looking for tweets...")
    print("=-=-=-=-=-=-=-=-=-=-=")
    print()
    results = api.search(q="calor", tweet_mode = "extended") # lang="pt-br" geocode = "xx.xxxxxx,xx.xxxxxx,xkm"      q="" its the query, the word that the script will look for
    for result in reversed(results):
        arquivo_calor = open('curtidas_calor.txt','r')
        conteudo_calor = arquivo_calor.read()
        try:
            if (str(result.id) in conteudo_calor):
                print("We already retweeted the tweet of @" + result.user.screen_name)
            else:
                if (result.user.screen_name == "bot_calor"):
                    print("myself") # Trying to interact with my tweet
                else:
                    arquivo_calor.close()
                    print()
                    print(str(result.user.screen_name) + ' - ' + result.full_text, flush=True) # @Mtss_e - Nossa que calor!!!
                    print()
                    print()
                    print("Found", flush=True)
                    print("Liking and retweeting...", flush=True)
                    print()
                    arquivo_calor = open('curtidas_calor.txt','a')
                    arquivo_calor.write(str(result.id) + "\n")
                    api.create_favorite(result.id)
                    api.retweet(result.id)
                    arquivo_calor.close()
        except tweepy.TweepError as e:
            print(e.reason)

# Mentions only funcion

def fav_tweet_menção():
    print()
    print("=-=-=-=-=-=-=-=-=-=-=")
    print("Looking for mentions...")
    print("=-=-=-=-=-=-=-=-=-=-=")
    print()
    mentions = api.mentions_timeline(tweet_mode = 'extended', lang="pt-br")
    for mention in reversed(mentions):
        arquivo_mencao = open('curtidas_mencao.txt','r')
        conteudo_mencao = arquivo_mencao.read()
        try:
            if (str(mention.id) in conteudo_mencao):
                print("We already retweeted the tweet of @" + mention.user.screen_name)
            else:
                if (mention.user.screen_name == "bot_calor"):
                        print("myself")
                else:
                    arquivo_mencao.close()
                    print()
                    print(str(mention.user.screen_name) + ' - ' + mention.full_text, flush=True) # @Mtss_e - Caramba, esse @bot_calor tá bombando mesmo né!!!
                    print()
                    print()
                    print("Found", flush=True)
                    print("Liking and retweeting...", flush=True)
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
