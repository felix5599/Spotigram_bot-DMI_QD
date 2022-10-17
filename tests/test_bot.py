import pytest
import src.bot

def test_search_artist_id():
    assert src.bot.search_artist_id("Pink Floyd").replace("spotify:artist:","") == "0k17h0D3J5VfsdmQ1iZtE9"
    assert src.bot.search_artist_id("Led Zeppelin").replace("spotify:artist:","") == "36QJpDe2go2KgaRleHCDTp"
    assert src.bot.search_artist_id("Rihanna").replace("spotify:artist:","") == "5pKCCKE2ajJHZ9KAiaK11H"

def test_search_album_id():
    assert src.bot.search_album_id("The Dark Side Of The Moon").replace("spotify:album:","") == "4LH4d3cOWNNsVw41Gqt2kv"
