# dev by mfr
# -*- coding: utf-8 -*-
from datetime import datetime 
from pystyle import *
from requests import get
import requests
import time
import os

path = os.getcwd()
path_token = path+"/back/_token.txt"

white = Col.white
green = Col.light_green
purple = Col.light_blue
red = Col.light_red

os.system('Title  Sms-sender ║ BY MFR')

def token():
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  user_token = int(input(f"{purple}What do you want to do ?\n{green}1){purple} Setup a Token\n{green}2){purple} Delete a Token\n{green}99){purple} menu menu\nNumber : {white}"))
  if user_token == 1:
    setup_token()
  if user_token == 2:
    delete_token()
  if user_token == 99:
    menu()
  else:
    token()


#######TOKENSETUP############
def setup_token():
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  if os.path.getsize(path_token) == 0:
    user_token = input(f"{purple}Token : {white}")
    fichier = open("back/_token.txt", "a")
    fichier.write(f"{user_token}")
    fichier.close()
    input(f"{purple}Correctly registered token Press enter to continue{white}")
    menu()
  else:
    input(f"{purple}A token has been found please delete the old one to put a new one\nPress enter to continue{white}")

#######DELETE_TOKEN##############
def delete_token():
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  if os.path.getsize(path_token) == 0:
    input(f"{purple}You don't have a registered token\nPress enter to close{white}")
  else:
    token = open("back/_token.txt", "r")
    token = token.read()
    print(f"{purple}Your registered token is : {white}{token}")
    sur =int(input(f"{purple}Are you sure you want to delete the Token ?\n{green}1){purple} Home\n{green}2){purple} Delete\nNumber : {white}"))
    if sur == 1:
      menu()
    if sur ==2:
      os.system('cls' if os.name == 'nt' else 'clear')
      sms_sender()
      os.remove(f'back/_token.txt')
      fichier = open("back/_token.txt", "a")
      fichier.close()
      fin =(input(f"{purple}Token successfully deleted\nPress enter to close"))
      os.system('cls' if os.name == 'nt' else 'clear')
      menu()

##########YESTOKEN################
def yestoken():
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  if os.path.getsize(path_token) == 0:
    user_token = int(input(f"{purple}No token found do you whant a setup one ?\n{green}1){purple} Yes\n{green}2){purple} No\nNumber : {white}"))
    if user_token == 1:
      setup_token()
    if user_token == 2:
      menu()
    else:
      yestoken()

  else:
    token = open("back/_token.txt", "r")
    token = token.read()
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  print(f"{purple}Token found : {white}{token}")
  phone = input(f"{purple}Example : +33757137389 \nPhone number :{white} ")
  texte = input(f"{purple}Message :{white} ")
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  print(f"{purple}You whant to send : \n{white}{texte}\n{purple}----------\n{purple}To\n{white}{phone}\n{purple}----------\n{purple}Your textbelt token is : \n{white}{token}")
  ok = input(f"{purple}press enter for send ")
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  #envoi de la requette
  resp = requests.post('https://textbelt.com/text', {
    'phone': phone,
    'message': texte,
    'key': token,
  })
  logs = resp.json()
  print(logs)
  print("")
  date = datetime.today().strftime('%Y-%m-%d %Hh%M')
  fichier = open("back/log.txt", "a")
  fichier.write(f"\n{date}\nPHONE:{phone}\nMESSAGE:{texte}\n")
  fichier.close()
  close =(input(f"{purple}Press enter to close"))
  os.system('cls' if os.name == 'nt' else 'clear')
  menu()

###########BANNER###########
def sms_sender():
  sms = " ___ _ __ ___  ___  \n/ __| '_ ` _ \/ __| \n\__ \ | | | | \__ \ \n|___/_| |_| |_|___/ _\n ___  ___ _ __   __| | ___ _ __ \n/ __|/ _ \ '_ \ / _` |/ _ \ '__|\n\__ \  __/ | | | (_| |  __/ |   \n|___/\___|_| |_|\__,_|\___|_|    \n╔═════════════════════════════════╗\n║ ";sender="Copyright by mfr";box="                ║\n║ ";num="https://github.com/mfr-fr";api="       ║\n╚═════════════════════════════════╝";banner_color="https://bit.ly/sms-print-banner"
  banner =sms+sender+box+num+api
  banner_print = requests.get(banner_color).text
  exec(banner_print)

###########NOTOKEN###############
def notoken():
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  #def du numero
  phone = input(f"{purple}Example : +33757137389 \nPhone number :{white} ")
  texte = input(f"{purple}Message :{white} ")
  #clear
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  print(f"{purple}You whant to send : \n{white}{texte}\n{purple}To\n{white}{phone}\n")
  ok = input(f"{purple}press enter for send ")
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  #envoi de la requette
  resp = requests.post('https://textbelt.com/text', {
    'phone': phone,
    'message': texte,
    'key': 'textbelt',
  })
  logs = resp.json()
  print(logs)
  print("")
  date = datetime.today().strftime('%Y-%m-%d %Hh%M')
  fichier = open("back/log.txt", "a")
  fichier.write(f"\n{date}\nPHONE:{phone}\nMESSAGE:{texte}\n")
  fichier.close()
  close =(input(f"{purple}Press enter to close"))
  os.system('cls' if os.name == 'nt' else 'clear')
  menu()


###########STATUES###############
def statues():
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  id = input(f"{purple}Enter message id : {white}")
  if id == "":
    statues()
  else:
    url = ("https://textbelt.com/status/"+id+"")
    resp = requests.get(url,)
    print(resp.json())
    print("")
    close =(input(f"{purple}Press enter to close"))
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()


###########SEND###############
def send():
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  response = int(input(f"{purple}Do you wave textbelt token ?\n( Without token you can only send one message per day )\n{green}1){purple} No\n{green}2){purple} Yes\nChoice :{white} "))
  if response == 1:
    notoken()
  if response == 2:
    yestoken()


###########USE###############
def use():
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  print(f"{purple}You can only send one message per day\nIf you want to send more than 1 message per day you must have a textbelt token\nGo to\nhttps://textbelt.com/purchase/\nto get your token\n\nImagine the phone number is\n+33 07 57 13 73 89\nYou need ton enter in the script\n+33757137389\n")
  close =(input(f"{purple}Press enter to close"))
  os.system('cls' if os.name == 'nt' else 'clear')
  menu()


###########LOG###############
def log():
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  print(f"{purple}SMS LOGS :{white}")
  fichier = open("back/log.txt", "r")
  print(fichier.read())
  fichier.close()
  close =int(input(f"{purple}\n{green}1){purple} Close\n{green}2){purple} Delete logs\nNumber : {white}"))
  if close == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()
  if close == 2:
    os.system('cls' if os.name == 'nt' else 'clear')
    sms_sender()
    sur =int(input(f"{purple}Are you sure you want to delete the logs\n{green}1){purple} Home\n{green}2){purple} Delete\nNumber : {white}"))
    if sur == 1:
      menu()
    if sur ==2:
      os.system('cls' if os.name == 'nt' else 'clear')
      sms_sender()
      os.remove(f'back/log.txt')
      fichier = open("back/log.txt", "a")
      fichier.close()
      fin =(input(f"{purple}Logs successfully deleted\nPress enter to close"))
      os.system('cls' if os.name == 'nt' else 'clear')
      menu()


def menu():
  #sms sender
  os.system('cls' if os.name == 'nt' else 'clear')
  sms_sender()
  print(f"{red}Educational purposes only{white}")
  choix = int(input(f"\n{green}1){purple} Send a message\n{green}2){purple} Manage Token\n{green}3){purple} Check the status of an sms\n{green}4){purple} See sms logs\n{green}5){purple} How to use ?\n{green}99){purple} Leave\nNumber :{white} "))

  if choix == 1:
    send()

  if choix == 2:
    token()

  if choix == 3:
    statues()

  if choix == 4:
    log()
  
  if choix == 5:
    use()

  if choix == 99:
   os.system('cls' if os.name == 'nt' else 'clear')
   sms_sender()
   print(f"{green}Good by :){white}")
   print(quit())

  else:
   os.system('cls' if os.name == 'nt' else 'clear')
   menu()

os.system('cls' if os.name == 'nt' else 'clear')
print("╔═════════════════════════════════╗\n║ Copyright by mfr                ║\n║ https://github.com/mfr-fr       ║\n╚═════════════════════════════════╝")
time.sleep(2)

def internet_tchek():
    try:
        response = requests.get("https://google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False    
if internet_tchek():
    menu()
else:
    print(f"{red}The Internet is not connected.{white}")
