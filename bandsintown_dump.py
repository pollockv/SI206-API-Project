import unittest
import requests
import sqlite3
import json
import os
import sys
import re
import urllib

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
    else:
        return []


def main():
    artistlist = ["Drake", "Hippo Campus", "STRFKR", "Mac Demarco"]
    finallist = []

    for artist in artistlist:
        eventlist = get_bandsintown_events(artist)
        if eventlist != []:
            artist_name = eventlist[0]['artist']['name']
            for event in eventlist:
                #list index at beginning to specify which event
                venue = event[0]['venue']['name']
                city = event[0]['venue']['city']
                country = event['venue']['country']
                latitude = event['venue']['latitude']
                longitude = event['venue']['longitude']
                finallist.append([artist_name, venue, city, country, latitude, longitude])
                #print(artist_name, venue, city, country, latitude, longitude)
                
                print(finallist)

if __name__ == "__main__":
    main()
