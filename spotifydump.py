import sqlite3
import json
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data

client_id = "9db9eeacd0004463b836ed7e1c7869e8"
client_secret = "2eb76cf70264493abde544ba5a65a1ae"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

playlist1 = "Car Playlist" #chosen playlist
playlist1 = "Study Playlist"
results = sp.search(playlist1, type='artist') #search query
print(results)

# conn = sqlite3.connect('geodata.sqlite')
# cur = conn.cursor()

# cur.execute('''
# CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# for item in results['tracks']['items']:
#     print(item)

# SQL for putting values into db tables
# INSERT INTO table_name (column1, column2, column3, ...)
# VALUES (value1, value2, value3, ...);