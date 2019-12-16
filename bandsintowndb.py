import unittest
import sqlite3
import json
import os
import requests
import ast


def createtables():
    cur.execute('CREATE TABLE IF NOT EXISTS UpcomingEvents(event_id INTEGER PRIMARY KEY, artist_name TEXT, venue TEXT, city TEXT, country TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS LatitudeForEvents(event_id INTEGER, latitude TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS LongitudeForEvents(event_id INTEGER, longitude TEXT)')

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

cur, conn = setUpDatabase('test-database.db')


def get_bandsintown_events(bandName, id="75771b0391833569dedd2b5ceff8d2af", date="upcoming"):
    eventdict = {}
    base_url = "https://rest.bandsintown.com/artists/" + bandName + "/events?app_id=" + id + "&date=" + date
    resp = requests.get(base_url)
    if resp != []:
        eventdict = resp.json()
        return eventdict
    else:
        return []

def table_insert(finallist):
    count = 0
    for event in finallist:
        cur.execute('SELECT artist_name FROM UpcomingEvents WHERE artist_name = ?', (event[0], ))
        result = cur.fetchone()
        if result:
            continue
        else:
            sql_query = 'INSERT INTO UpcomingEvents(event_id, artist_name, venue, city, country) VALUES (NULL, ?,?,?,?)'
            vals = (event[0], event[1], event[2], event[3])
            cur.execute(sql_query, vals)
            count +=1
            conn.commit()
            print("Getting row...")
        if count == 20:
            break

def latlong_insert(finallist):
    count = 0
    for event in finallist:
        cur.execute('SELECT latitude from LatitudeForEvents WHERE latitude = ?', (event[4], ))
        result = cur.fetchone()
        if result:
            continue
        else:
            cur.execute('SELECT event_id FROM UpcomingEvents WHERE artist_name = ?', (event[0], ))
            event_id = cur.fetchone()[0]
            cur.execute('INSERT INTO LatitudeForEvents(event_id, latitude) VALUES(?,?)', (event_id, event[4]))
            cur.execute('INSERT INTO LongitudeForEvents(event_id, longitude) VALUES(?,?)', (event_id, event[5]))
            count +=1
            conn.commit()
        if count == 20:
            break


def main():

    # Create tables if not already there
    createtables()
    cur.execute('SELECT list_of_rec FROM RecommForAll')

    # Creating list of items for the db
    edit_list = []
    revise_lst = []
    finallist = []
    artists = cur.fetchall()
    for tup in artists:
        res = ast.literal_eval(tup[0])
        edit_list.append(res)
    for lst in edit_list:
        for artist in lst:
            if artist not in revise_lst:
                revise_lst.append(artist)
    for artist in revise_lst:
        eventlist = get_bandsintown_events(artist)
        if eventlist == {'errorMessage': '[NotFound] The artist was not found'}:
            continue
        if eventlist != []:
            artist_name = eventlist[0]['artist']['name']
            venue = eventlist[0]['venue']['name']
            city = eventlist[0]['venue']['city']
            country = eventlist[0]['venue']['country']
            if 'latitude' not in eventlist[0]['venue']:
                lat = ''
                longitude = ''
                finallist.append([artist_name, venue, city, country, lat, longitude])
            else:
                lat = eventlist[0]['venue']['latitude']
                longitude = eventlist[0]['venue']['longitude']
                finallist.append([artist_name, venue, city, country, lat, longitude])

    # Pass list into db
    table_insert(finallist)
    #latlong_insert(finallist)

if __name__ == "__main__":
    main()