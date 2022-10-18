import pytest
from telegram import Message, Chat
import src.bot

#Making a fake user
fake_user = src.bot.User(id = 123, first_name= "Giovanni", is_bot= False, last_name= "Dell'acqua", username= "fakeuser123")

fake_chat = Chat(id = 123, username= fake_user.username,)

def test_search_artist_id():
    assert src.bot.search_artist_id("Pink Floyd").replace("spotify:artist:","") == "0k17h0D3J5VfsdmQ1iZtE9"
    assert src.bot.search_artist_id("Led Zeppelin").replace("spotify:artist:","") == "36QJpDe2go2KgaRleHCDTp"
    assert src.bot.search_artist_id("Rihanna").replace("spotify:artist:","") == "5pKCCKE2ajJHZ9KAiaK11H"

def test_search_album_id():
    assert src.bot.search_album_id("The Dark Side Of The Moon").replace("spotify:album:","") == "4LH4d3cOWNNsVw41Gqt2kv"
    assert src.bot.search_album_id("Celebration Day").replace("spotify:album:","") == "0kTe1sQd9yhDsdG2Zth7X6"

def test_send_welcome():
    src.bot.send_welcome(fake_chat.id)