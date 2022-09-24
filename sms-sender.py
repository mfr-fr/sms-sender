import requests
import time
import os
os.system('Title  Sms-sender ║ BY MFR')
banner = " ___ _ __ ___  ___  \n/ __| '_ ` _ \/ __| \n\__ \ | | | | \__ \ \n|___/_| |_| |_|___/ _\n ___  ___ _ __   __| | ___ _ __ \n/ __|/ _ \ '_ \ / _` |/ _ \ '__|\n\__ \  __/ | | | (_| |  __/ |   \n|___/\___|_| |_|\__,_|\___|_|    \n╔═════════════════════════════════╗\n║ Copyright by mfr                ║\n║ https://github.com/mfr-fr       ║\n╚═════════════════════════════════╝"

#by mfr
os.system('cls' if os.name == 'nt' else 'clear')
print("╔═════════════════════════════════╗\n║ Copyright by mfr                ║\n║ https://github.com/mfr-fr       ║\n╚═════════════════════════════════╝")

#sleep
time.sleep(2)

#clear
os.system('cls' if os.name == 'nt' else 'clear')

#sms sender
print(banner)
choix = int(input("\n1) Send a message\n2) Check the status of an sms\n3) How to use ?\n99) Leave\n\nChoice : "))

if choix == 1:
    os.system('cls' if os.name == 'nt' else 'clear')

if choix == 2:
  os.system('cls' if os.name == 'nt' else 'clear')
  print(banner)
  id = input("Enter message id : ")
  url = ("https://textbelt.com/status/"+id+"")
  resp = requests.get(url,)
  print(resp.json())
  print("")
  close =(input("Press enter to close"))
  os.system('cls' if os.name == 'nt' else 'clear')
  print(quit())

if choix == 3:
  os.system('cls' if os.name == 'nt' else 'clear')
  print(banner)
  print("You can only send one message per day\nIf you want to send more than 1 message per day you must have a textbelt token\nGo to\nhttps://textbelt.com/purchase/\nto get your token\n\nImagine the phone number is\n+33 07 57 13 73 89\nYou need ton enter in the script\n+33757137389\n")
  close =(input("Press enter to close"))
  os.system('cls' if os.name == 'nt' else 'clear')
  print(quit())

if choix == 99:
 os.system('cls' if os.name == 'nt' else 'clear')
 print(quit())

print(banner)
response = int(input("Do you wave textbelt token ?\n( Without token you can only send one message per day )\n1) Yes\n2) No\nChoice : "))
#######################################################################
if response == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    #def du numero
    phone = input("Example : +33757137389 \nPhone number : ")
    texte = input("Message : ")
    token =input("Textbelt token : ")
    
    #clear
    os.system('cls' if os.name == 'nt' else 'clear')

    #sms sender
    print(banner)
    #resumé
    print("You whant to send : ")
    print(texte)
    print("----------")
    print("To")
    print(phone)
    print("----------")
    print("Your textbelt token is : ")
    print(token)
    ok = input("press enter for send ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    #envoi de la requette
    resp = requests.post('https://textbelt.com/text', {
      'phone': phone,
      'message': texte,
      'key': token,
    })
    print(resp.json())
    print("")
    close =(input("Press enter to close"))
     
##############################################################################
if response == 2:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    #def du numero
    phone = input("Example : +33757137389 \nPhone number : ")
    texte = input("Message : ")
    
    #clear
    os.system('cls' if os.name == 'nt' else 'clear')

    #sms sender
    print(banner)
    #resumé
    print("You whant to send : ")
    print(texte)
    print("----------")
    print("To")
    print(phone)
    print("")
    ok = input("press enter for send ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    #envoi de la requette
    resp = requests.post('https://textbelt.com/text', {
      'phone': phone,
      'message': texte,
      'key': 'textbelt',
    })
    print(resp.json())
    print("")
    close =(input("Press enter to close"))
