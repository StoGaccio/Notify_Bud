import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
))

# Esempio: cerchiamo un artista
results = sp.search(q="Arctic Monkeys", type="artist")
print(results)

artist_id = "7Ln80lUS6He07XvHI8qqHH"  # Arctic Monkeys
albums = sp.artist_albums(artist_id, album_type="album,single", limit=5)

for album in albums["items"]:
    print(album["name"], "-", album["release_date"])

import yagmail

yag = yagmail.SMTP(os.getenv("GMAIL_USER"), os.getenv("GMAIL_PASS"))

def send_email(new_releases):
    body = "Ecco le nuove uscite:\n" + "\n".join(new_releases)
    yag.send(to="leonardogaccioli@gmail.com", subject="Nuove uscite Spotify", contents=body)
import time

while True:
    # codice per controllare nuove uscite
    print("Controllo completato...")
    time.sleep(86400)  # aspetta 24 ore
