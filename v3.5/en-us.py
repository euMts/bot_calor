from selenium import webdriver
from pathlib import Path
from time import sleep
import os
import re
import datetime
import tweepy
import ctypes
import sys

# Matheus Eduardo
# github.com/eumts

# - Setting variables -

driver = webdriver.Firefox()
driver.get(" ") # Your dontpad link
sleep(3)

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
            if (e.reason == ("[{'code': 185, 'message': 'User is over daily status update limit.'}]")):
                #quit() Pode sair se quiser.
                os.system("cls")
                print("Timeout, we'll be back in 6 hours.")
                sleep(21600) # 6 horas
                
            if (e.reason == ("Twitter error response: status code = 429")):
                #quit() Pode sair se quiser.
                os.system("cls")
                print("Timeout, we'll be back in 6 hours.")
                sleep(21600) # 6 horas

# Mentions only funcion

def fav_tweet_men????o():
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
                    print(str(mention.user.screen_name) + ' - ' + mention.full_text, flush=True) # @Mtss_e - Caramba, esse @bot_calor t?? bombando mesmo n??!!!
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
            if (e.reason == ("[{'code': 185, 'message': 'User is over daily status update limit.'}]")):
                #quit() Pode sair se quiser.
                print(e.reason)
            if (e.reason == ("Twitter error response: status code = 429")):
                #quit() Pode sair se quiser.
                print(e.reason)

# Checking dontpad function

def check():
    os.system('cls')
    driver.refresh()
    textarea = driver.find_element_by_xpath('//*[@id="text"]')
    text = textarea.text
    now = datetime.datetime.now()
    data = (now.strftime("[%d-%m-%Y  %H:%M:%S]"))
    if ("ON" in text):
        print()
        print("=--=-=-=-=-=-=-=-=-=")
        print("Calor_bot on")
        print("=--=-=-=-=-=-=-=-=-=")
        print()
        print(data)
        textarea.clear()
        textarea.send_keys('''ON
the bot is running, as your computer.
to change it and shut your pc down type the password:''')
        fav_tweet_calor()
        fav_tweet_men????o()
        sleep(30)

    if ("OFF" in text):
        os.system('cls')
        print()
        print("=--=-=-=-=-=-=-=-=-=")
        print("Calor_bot off")
        print("=--=-=-=-=-=-=-=-=-=")
        print()
        print(data)
        textarea.clear()
        textarea.send_keys('''OFF
the bot isnt running, but your pc does.
to change it and shut your pc down type the password:''')

    if (" " in text): # Your password (could not have the words ON and OFF, I recommend using a numer sequence.)
        os.system('cls')
        print()
        print("=--=-=-=-=-=-=-=-=-=")
        print("Shutting your computer down...")
        print("=--=-=-=-=-=-=-=-=-=")
        print()
        print(data)
        textarea.clear()
        textarea.send_keys('''OFF
the bot isnt running, and your pc isnt running too.''')
        os.startfile(r".\shutdown.bat")

# Quit function.
def quit():
    for i in range(10, -1, -1):
        print()
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Daily limit, try again soon.")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()
        print("Closing in " + str(i) + " seconds.")
        sleep(1)
        os.system("cls")
        if(i == 0):
            driver.close()
            sys.exit()

# Loop

while True:
    check()
    sleep(20) 
