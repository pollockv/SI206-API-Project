import unittest
import requests
import sqlite3
import json
import os
import sys
import re
import urllib
import bandsintown

# https://app.swaggerhub.com/apis/Bandsintown/PublicAPI/3.0.0#/VenueData

def get_bandsintown_artistinfo(artist, id="75771b0391833569dedd2b5ceff8d2af"):
    base_url = "https://rest.bandsintown.com/artists/" + artist + "?app_id=" + id
    resp = requests.get(base_url)
    artistdict = resp.json()
    return artistdict

def get_bandsintown_events(bandName, id="75771b0391833569dedd2b5ceff8d2af", date="upcoming"):
    eventdict = {}
    base_url = "https://rest.bandsintown.com/artists/" + bandName + "/events?app_id=" + id + "&date=" + date
    resp = requests.get(base_url)
    if resp != []:
        eventdict = resp.json()
        return eventdict

def main():
    artistlist = ["Drake", "Hippo Campus", "STRFKR", "Mac Demarco"]

    for artists in artistlist:
        eventlist = get_bandsintown_events(artists)
        artistinfo = get_bandsintown_artistinfo(artists)
        if eventlist != []:
            for item in eventlist:
                # list index at beginning to specify which event
                artist_name = item['artist']['name']
                venue = item['venue']['name']
                city = item['venue']['city']
                latitude = item['venue']['latitude']
                longitude = item['venue']['longitude']
                print(artist_name, venue, city, latitude, longitude)

if __name__ == "__main__":
    main()
