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

# - Definindo variáveis -

driver = webdriver.Firefox()
driver.get(" ") # Seu link do dontpad
sleep(3)

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
    resultados = api.search(q = 'calor', tweet_mode = "extended", lang="pt-br") # lang="pt-br" geocode = "xx.xxxxxx,xx.xxxxxx,xkm"      q="" é a query, palavra que vai buscar no tweet
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
            if (e.reason == ("[{'code': 185, 'message': 'User is over daily status update limit.'}]")):
                #quit() Pode sair se quiser.
                os.system("cls")
                print("Tomamos timeout, voltamos em 6 horas.")
                sleep(21600) # 6 horas
                
            if (e.reason == ("Twitter error response: status code = 429")):
                #quit() Pode sair se quiser.
                os.system("cls")
                print("Tomamos timeout, voltamos em 6 horas.")
                sleep(21600) # 6 horas
            
# Função para verificar o dontpad

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
            if (e.reason == ("[{'code': 185, 'message': 'User is over daily status update limit.'}]")):
                #quit() Pode sair se quiser.
                print(e.reason)
            if (e.reason == ("Twitter error response: status code = 429")):
                #quit() Pode sair se quiser.
                print(e.reason)

# Função verificar o dontpad

def verificar():
    os.system('cls')
    driver.refresh()
    textarea = driver.find_element_by_xpath('//*[@id="text"]')
    texto = textarea.text
    now = datetime.datetime.now()
    data = (now.strftime("[%d-%m-%Y  %H:%M:%S]"))
    if ("ON" in texto):
        print()
        print("=--=-=-=-=-=-=-=-=-=")
        print("Calor_bot ligado")
        print("=--=-=-=-=-=-=-=-=-=")
        print()
        print(data)
        textarea.clear()
        textarea.send_keys('''ON
o bot do calor está ligado, assim como seu computador.
para desligar seu computador digite a senha:''')
        fav_tweet_calor()
        fav_tweet_menção()
        sleep(30)

    if ("OFF" in texto):
        os.system('cls')
        print()
        print("=--=-=-=-=-=-=-=-=-=")
        print("Calor_bot desligado")
        print("=--=-=-=-=-=-=-=-=-=")
        print()
        print(data)
        textarea.clear()
        textarea.send_keys('''OFF
o bot do calor está desligado, e seu computador ligado.
para desligar seu computador digite a senha:''')

    if (" " in texto): # Sua senha (não pode conter as palavras ON e OFF, eu recomendo usar uma sequencia de números.)
        os.system('cls')
        print()
        print("=--=-=-=-=-=-=-=-=-=")
        print("Desligando pc..")
        print("=--=-=-=-=-=-=-=-=-=")
        print()
        print(data)
        textarea.clear()
        textarea.send_keys('''OFF
o bot do calor está desligado, assim como seu computador.''')
        os.startfile(r".\shutdown.bat")

# Função sair.

def quit():
    for i in range(10, -1, -1):
        print()
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Limite de tweets alcançado, tente novamente mais tarde.")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()
        print("Fechando em " + str(i) + " segundos.")
        sleep(1)
        os.system("cls")
        if(i == 0):
            driver.close()
            sys.exit()

# Loop

while True:
    verificar()
    sleep(20)