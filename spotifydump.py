import unittest
import requests
import sqlite3
import json
import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data


client_id = "9db9eeacd0004463b836ed7e1c7869e8"
client_secret = "2eb76cf70264493abde544ba5a65a1ae"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API


def saveTextFile(data,filename):
    outfile = open(filename, 'w')
    outfile.write(data)
    outfile.close()


def readDataFromFile(filename):
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)
    return json_data

def show_tracks(tracks):
    trackdict = {}
    for item in enumerate(tracks['items']):
        track = item['track']
        artist = track['artists'][0]['name']
        track_name = track['name']


def main():
    studyplaylist = "2DJapkOfWVgb01aWi3ZNrm" #chosen playlist
    carplaylist = "1I2JfNqzWCNvGUI6EDbqVC"
    username = "p85ag2eg0vz37ioz6t2iw1t2s"
    #print(sp.user_playlist_tracks(username, studyplaylist, limit=20, offset=0, market=None))

    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            print(playlist['name'])
            print('  total tracks', playlist['tracks']['total'])
            results = sp.user_playlist(username, playlist['id'],
                fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)

if __name__ == "__main__":
    main()