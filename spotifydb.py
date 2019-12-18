import unittest
import requests
import sqlite3
import json
import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
import random

client_id = "9db9eeacd0004463b836ed7e1c7869e8"
client_secret = "2eb76cf70264493abde544ba5a65a1ae"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

cur, conn = setUpDatabase('final-database.db')

def create_tables():
    cur.execute('CREATE TABLE IF NOT EXISTS Artists(artist_id INTEGER PRIMARY KEY, artist TEXT UNIQUE)')
    cur.execute('CREATE TABLE IF NOT EXISTS StudyPlaylist(artist_id INTEGER, songname TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS CarPlaylist(artist_id INTEGER, songname TEXT)')

def table_insert(username, playlist_id):
    count = 0
    results = sp.user_playlist(username, playlist_id, fields="tracks,next")
    tracks = results['tracks']
    for item in enumerate(tracks['items']):
        track = item[1]['track']
        artist = track['artists'][0]['name']
        song = track['name']
        cur.execute('SELECT artist_id FROM Artists WHERE artist = ?', (artist, ))
        result = cur.fetchone()
        if result:
            continue
        else:
            cur.execute('INSERT INTO Artists(artist_id, artist) VALUES(NULL, ?)', (artist, ))
            count +=1
            conn.commit()
        if count == 20:
            break

def carplaylist_insert(username, playlist_id):
    count = 0
    results = sp.user_playlist(username, playlist_id, fields="tracks,next")
    tracks = results['tracks']
    for item in enumerate(tracks['items']):
        track = item[1]['track']
        artist = track['artists'][0]['name']
        song = track['name']
        cur.execute('SELECT artist_id FROM CarPlaylist WHERE songname = ?', (song, ))
        result = cur.fetchone()
        if result:
            continue
        else:
            cur.execute('SELECT artist_id FROM Artists WHERE artist = ?', (artist,))
            artist_id = cur.fetchone()[0]
            cur.execute('INSERT INTO CarPlaylist (artist_id, songname) VALUES(?, ?)', (artist_id, song))
            count +=1
            conn.commit()
        if count == 20:
            break


def studyplaylist_insert(username, playlist_id):
    count = 0
    results = sp.user_playlist(username, playlist_id, fields="tracks,next")
    tracks = results['tracks']
    for item in enumerate(tracks['items']):
        track = item[1]['track']
        artist = track['artists'][0]['name']
        song = track['name']
        cur.execute('SELECT artist_id FROM StudyPlaylist WHERE songname = ?', (song, ))
        result = cur.fetchone()
        if result:
            continue
        else:
            cur.execute('SELECT artist_id FROM Artists WHERE artist = ?', (artist,))
            artist_id = cur.fetchone()[0]
            cur.execute('INSERT INTO StudyPlaylist (artist_id, songname) VALUES(?, ?)', (artist_id, song))
            count +=1
            conn.commit()
        if count == 20:
            break

def main():
    studyplaylist = "2DJapkOfWVgb01aWi3ZNrm" #chosen playlist
    carplaylist = "1I2JfNqzWCNvGUI6EDbqVC"
    username = "p85ag2eg0vz37ioz6t2iw1t2s"
    print("Please input the playlist ID:")
    playlist_id = input()
    create_tables()
    table_insert(username, playlist_id)
    carplaylist_insert(username, carplaylist)
    studyplaylist_insert(username, studyplaylist)

if __name__ == "__main__":
    main()
