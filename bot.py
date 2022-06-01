#!/usr/bin/python

#Import dei vari packages
import telebot
from telegram import MessageId
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#SPOTIPY SETTINGS -  Queste variabili vengono prese da Spotify for Developer
cid = "AGGIUNGERE CID"
cid_secret = "AGGIUNGERE CID_SECRET"
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= cid, client_secret= cid_secret))

#TOKEN Bot telegram
API_TOKEN = 'AGGIUNGERE API TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Prende come parametri i comandi /help e /start 
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):   
    bot.reply_to(message, "Prova comando start o help")
   

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# Qualsiasi messaggio venga inviato farà una ricerca su spotify, inviando i primi 5 risultati
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    messaggioDaInviare = []
    results = sp.search(q= message.text, limit= 5) #Risultati della ricerca di spotify
    for idx, track in enumerate(results['tracks']['items']):
        buffer1 = idx
        buffer2 = track['name']
        buffer3 = str(buffer1) + ": " + buffer2
        messaggioDaInviare.append(buffer3)

    stringa_Messaggio = ''
    for x in messaggioDaInviare:
        stringa_Messaggio += x + "\n" 
    bot.reply_to(message, stringa_Messaggio)

bot.infinity_polling()

#QUA é STATA FATTA UNA BOZZA | LASCIARLA PER OGNI EVENIENZA
# messaggioDaInviare = []
# results = sp.search(q='pink floyd',  limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     buffer1 = idx
#     buffer2 = track['name']
#     buffer3 = str(buffer1) + ": " + buffer2
#     messaggioDaInviare.append(buffer3)
# stringa_Messaggio = ''
# for x in messaggioDaInviare:
#     stringa_Messaggio += x + "\n" 
#print(stringa_Messaggio)