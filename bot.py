#!/usr/bin/python
#Import dei vari packages
from logging import exception
from unittest import result
import telebot
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Access Token for Telegram Bot and Spotify for developer
cid = "45727c4bbd944c94ad186a28bd89ab64"
cid_secret = "682e567ecf20491a8c18a63b8dfeb94d"
API_TOKEN = '5107605922:AAGnSznHtUHLW9nlSrLq90NqYUfgni37qGs'

# Spotipy Setting
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= cid, client_secret= cid_secret))

# Bot Telegram
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start','help','aiuto','ciao'])
def send_welcome (message):
    bot.reply_to(message,"Ciao! sono SpotyBot, il mio compito è quello di aiutarti nel mondo della musica!")
    bot.send_message(message.chat.id, "Scrivi 'artista' per sapere le canzoni più famose del tuo artista preferito! \nScrivi 'album' per sapere le canzoni dell'album che cerchi!")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    command_message = str(message.text).lower() #Prende il comando inviato tramite messagio, e lo rende tutto minuscolo
    if command_message == 'artista' :
        bot.send_message(message.chat.id, "Scrivimi il nome di un artista e ti dirò quali sono le sue 5 canzoni più famose!")
        bot.register_next_step_handler(message, nome_artista)
    elif command_message == 'album' :
        bot.send_message(message.chat.id, "Scrivimi l'album che cerchi e ti darò tutte le info! :) ")
        bot.register_next_step_handler(message, nome_album)
    elif command_message == "info":
        bot.send_message(message.chat.id, "Inviami il nome di un artista e ti dirò le informazioni di questo artista!")
        bot.register_next_step_handler(message, info_artista)


# ========== TOP 5 TRACCE ARTISTA ==========
def nome_artista(message):
    try:
        chat_id = message.chat.id
        input_text = message.text
        artist_id = search_artist_id(str (input_text))
        results = sp.artist_top_tracks(artist_id)
    except Exception as e: 
        bot.send_message(chat_id, "C'è stato un errore! Prova a inserire in modo corretto il nome dell'artista :/")

    buffer = '' #Buffer da utilizzare per poi inviare il messaggio
    for idx,track in enumerate(results['tracks'][:5]):
        buffer += str(idx + 1)+ " " + track['name'] + "\n"

    bot.send_message(chat_id, buffer)

# Funzione che ritorna l'ID dell'artista
def search_artist_id(nome_artista) -> str:
    results = sp.search(nome_artista, limit= 1, type="artist")
    items = results['artists']['items']
    risultato_finale = items[0]
    
    return(str(risultato_finale['uri']))
# ============ FINE ARTISTA==================

# ========== TRACCE ALBUM ==========
def nome_album(message):
    try:
       chat_id = message.chat.id
       input_text = message.text
       album_id = search_album_id(str (input_text)) # Cerca l'ID dell'album corrispondente
       results = sp.album_tracks(album_id)
    except Exception as e:
       bot.send_message(chat_id, "C'è stato un errore! Prova a inserire in modo corretto il nome dell'album :/")

    number_tracks = int (results['total']) #Prende il numero totale di tracce presenti nell'album
    buffer = ''
    
    for idx,track in enumerate(results['items'][:number_tracks]):
        buffer += str(idx + 1)+ " " + track['name'] + "\n"

    bot.send_message(chat_id, buffer)    

#Funzione che ritorna l'id album
def search_album_id(nome_album) -> str:
    results = sp.search(nome_album, limit= 1, type="album")
    items = results['albums']['items']
    risultato_finale = items[0]
    
    return(str(risultato_finale['uri']))
# ========== FINE TRACCE ALBUM ==========

# ========== INFORMAZIONI ARTISTA ==========
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
# ========== FINE INFORMAZIONI ARTISTA ==========

# -----====== IL CODICE DEVE ESSERE SCRITTO PRIMA DI QUESTA FUNZIONE =====-----
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
