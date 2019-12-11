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

def get_bandsintown_artistinfo(bandName, id="75771b0391833569dedd2b5ceff8d2af"):
    base_url = "https://rest.bandsintown.com/artists/" + bandName + "?app_id=" + id
    resp = requests.get(base_url)
    bandsdict = resp.json()
    return bandsdict

def get_bandsintown_events(bandName, id="75771b0391833569dedd2b5ceff8d2af", date="upcoming"):
    eventdict = {}
    base_url = "https://rest.bandsintown.com/artists/" + bandName + "/events?app_id=" + id + "&date=" + date
    resp = requests.get(base_url)
    if resp != []:
        eventdict = resp.json()
        return eventdict

def main():
    sqldict = {}
    artists = ["Drake", "Hippo Campus", "STRFKR", "Mac Demarco"]

    for artist in artists:
        eventdict = get_bandsintown_events(artist)
        print(eventdict['name'])

if __name__ == "__main__":
    main()
