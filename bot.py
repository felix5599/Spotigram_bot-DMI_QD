#!/usr/bin/python

#Import dei vari packages
from re import L
from unittest import result
import telebot
#from telegram import MessageId
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#SPOTIPY SETTINGS -  Queste variabili vengono prese da Spotify for Developer
cid = "aggiungere CID"
cid_secret = "aggiungere cid_secret"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= cid, client_secret= cid_secret))

#TOKEN Bot telegram
API_TOKEN = 'aggiungere api token'
bot = telebot.TeleBot(API_TOKEN)

# ========== TOP 5 TRACCIE ARTISTA ==========
@bot.message_handler(commands=['top'])
def top_artisti(message):
    bot.send_message(message.chat.id, "Inviami il nome di un artista e ti dirò quali sono le sue 5 canzoni più famose!")
    bot.register_next_step_handler(message, nome_artista)

def nome_artista(message):
    try:
        chat_id = message.chat.id
        input_text = message.text
        results = sp.artist_top_tracks(search_artist_id(str (input_text)))
    except Exception as e: 
        bot.send_message(chat_id, "C'è stato un errore! Prova a inserire in modo corretto il nome dell'artista :/")

    buffer = '' #Buffer da utilizzare per poi inviare il messaggio
    for idx,track in enumerate(results['tracks'][:5]):
        buffer += str(idx + 1)+ " " + track['name'] + "\n"

    bot.send_message(chat_id, buffer)

# ========== INFORMAZIONI ARTISTA ==========
@bot.message_handler(commands=['info'])
def info_artisti(message):
    bot.send_message(message.chat.id, "Inviami il nome di un artista e ti dirò le informazioni di questo artista!")
    bot.register_next_step_handler(message, info_artista)

def info_artista(message):
    try:
        chat_id = message.chat.id
        input_text = message.text
        results = sp.search(input_text, limit= 1, type="artist")
    except Exception as e: 
        bot.send_message(chat_id, "C'è stato un errore! Prova a inserire in modo corretto il nome dell'artista :/")
    
    items = results['artists']['items']
    artist = items[0]
    
    image_url = artist['images'][0]['url']

    caption = '' #Buffer da utilizzare per poi inviare il messaggio
    caption += "Nome: " + artist['name'] + "\n"
    caption += "Follower: " + str(artist['followers']['total']) + "\n"
    caption += "Popolarità: " + str(artist["popularity"]) + "/100\n"
    caption += "Generi: \n"
    for genere in artist['genres']:
        caption += "- " + genere + "\n"
    
    bot.send_photo(chat_id, image_url, caption)

# ========== FUNZIONE CHE DA COME RITORNO L'ID DELL'ARTISTA ==========
def search_artist_id(nome_artista) -> str:
    results = sp.search(nome_artista, limit= 1, type="artist")
    items = results['artists']['items']
    risultato_finale = items[0]
    
    return(str(risultato_finale['uri']))

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
