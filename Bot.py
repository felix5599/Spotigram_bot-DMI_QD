#!/usr/bin/python
#Import dei vari packages
from ast import If
from unittest import result
import telebot
#from telegram import MessageId
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#SPOTIPY SETTINGS -  Queste variabili vengono prese da Spotify for Developer
cid = "45727c4bbd944c94ad186a28bd89ab64"
cid_secret = "682e567ecf20491a8c18a63b8dfeb94d"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= cid, client_secret= cid_secret))

#TOKEN Bot telegram
API_TOKEN = '5107605922:AAGnSznHtUHLW9nlSrLq90NqYUfgni37qGs'
bot = telebot.TeleBot(API_TOKEN)

# ========== TOP 5 TRACCIE ARTISTA ==========
@bot.message_handler(commands=['help','info','aiuto','ciao'])
def send_welcome (message):
    #bot.reply_to(message,"""/ciao sono SpotyBot, il mio compito è quello di aiutarti nel mondo della musica!""")
    bot.send_message(message.chat.id, "Inviami il nome di un artista e ti dirò quali sono le sue 5 canzoni più famose!")


#def top_artisti(message):
#    bot.send_message(message.chat.id, "Inviami il nome di un artista e ti dirò quali sono le sue 5 canzoni più famose!")
#    bot.register_next_step_handler(message, nome_artista)

#def nome_artista(message):
#    try:
#        chat_id = message.chat.id
#        input_text = message.text
#        results = sp.artist_top_tracks(search_artist_id(str (input_text)))
#    except Exception as e: 
#        bot.send_message(chat_id, "C'è stato un errore! Prova a inserire in modo corretto il nome dell'artista :/")

#    buffer = '' #Buffer da utilizzare per poi inviare il messaggio
#    for idx,track in enumerate(results['tracks'][:5]):
#        buffer += str(idx + 1)+ " " + track['name'] + "\n"

#    bot.send_message(chat_id, buffer)

#  ========== TOP TRACCIE ALBUM ==========
#@bot.message_handler(commands=['album'])
#def top_album(message):
#    bot.send_message(message.chat.id, "Inviami il nome di un album e ti dirò quali sono le sue canzoni!")
   # bot.register_next_step_handler(message, nome_artista)

# ========== FUNZIONE CHE DA COME RITORNO L'ID DELL'ARTISTA ==========
#def search_artist_id(nome_artista) -> str:
#    results = sp.search(nome_artista, limit= 1, type="artist")
#    items = results['artists']['items']
#   risultato_finale = items[0]
    
#    return(str(risultato_finale['uri']))

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