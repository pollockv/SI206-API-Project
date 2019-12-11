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
    bandsdict = {}
    base_url = "https://rest.bandsintown.com/artists/" + bandName + "?app_id=" + id
    artistinfo = requests.get(base_url)
    print(artistinfo.url)
    return bandsdict


def main():
    artists = ["Drake", "Hippo Campus", "STRFKR", "Mac Demarco"]

    for artist in artists:
        print(get_bandsintown_artistinfo(artist))

if __name__ == "__main__":
    main()
