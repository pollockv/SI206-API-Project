import unittest
import sqlite3
import json
import os
import requests
import ast


def createtables():
    cur.execute('CREATE TABLE IF NOT EXISTS RecommForAll(all_artists TEXT, list_of_rec LIST)')
    cur.execute('CREATE TABLE IF NOT EXISTS RecommForStudy(random_artist TEXT, list_of_rec LIST)')
    cur.execute('CREATE TABLE IF NOT EXISTS RecommForCar(random_artist TEXT, list_of_rec LIST)')

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

cur, conn = setUpDatabase('final-database.db')

def get_recommendations_from_tastedive(artist, key="349890-SI206Fin-N4RHDBVP"):
    baseurl="https://tastedive.com/api/similar"
    params_d = {}
    params_d["q"]= artist
    params_d["k"]= key
    params_d["type"]= "music"
    params_d["limit"] = "3"
    resp = requests.get(baseurl, params=params_d)
    respDic = resp.json()
    return respDic 


def table_insert(artists):
    count = 0
    artist_recom = {}
    for artist in artists:
        results = get_recommendations_from_tastedive(artist)['Similar']['Results']
        for recom in results:
            if artist in artist_recom:
                artist_recom[artist].append(recom['Name'])
            else:
                artist_recom[artist] = [recom['Name']]
        for key in artist_recom:
            artist_str = str(key).strip("()")
            cleaned_str = artist_str.replace("'',","")
            cur.execute('SELECT all_artists FROM RecommForAll WHERE all_artists = ?', (cleaned_str, ))
            result = cur.fetchone()
            if result:
                continue
            else:
                query1 = 'INSERT INTO RecommForAll(all_artists, list_of_rec) VALUES (?,?)'
                vals = (cleaned_str, str(artist_recom[key]))
                cur.execute(query1, vals)
                count +=1
                conn.commit()
        if count == 20:
            break

def carplaylist_table_insert(car_artists):
    count = 0
    artist_recom = {}
    for artist_id in car_artists:
        cur.execute('SELECT artist FROM Artists WHERE artist_id = ?', (artist_id[0], ))
        artist = cur.fetchone()
        results = get_recommendations_from_tastedive(artist)['Similar']['Results']
        for recom in results:
            if artist in artist_recom:
                artist_recom[artist].append(recom['Name'])
            else:
                artist_recom[artist] = [recom['Name']]
        for key in artist_recom:
            artist_str = str(key).strip("()")
            stripped_str = artist_str.replace("'',", "")
            cleaned_str = stripped_str.strip("','")
            cur.execute('SELECT random_artist FROM RecommForCar WHERE random_artist = ?', (cleaned_str, ))
            result = cur.fetchone()
            if result:
                continue
            else:
                query1 = 'INSERT INTO RecommForCar(random_artist, list_of_rec) VALUES (?,?)'
                vals = (cleaned_str, str(artist_recom[key]))
                cur.execute(query1, vals)
                count +=1
                conn.commit()
        if count == 20:
            break


def studyplaylist_table_insert(study_artists):
    count = 0
    artist_recom = {}
    for artist_id in study_artists:
        cur.execute('SELECT artist FROM Artists WHERE artist_id = ?', (artist_id[0], ))
        artist = cur.fetchone()
        results = get_recommendations_from_tastedive(artist)['Similar']['Results']
        for recom in results:
            if artist in artist_recom:
                artist_recom[artist].append(recom['Name'])
            else:
                artist_recom[artist] = [recom['Name']]
        for key in artist_recom:
            artist_str = str(key).strip("()")
            stripped_str = artist_str.replace("'',", "")
            cleaned_str = stripped_str.strip("','")
            cur.execute('SELECT random_artist FROM RecommForStudy WHERE random_artist = ?', (cleaned_str, ))
            result = cur.fetchone()
            if result:
                continue
            else:
                query1 = 'INSERT INTO RecommForStudy(random_artist, list_of_rec) VALUES (?,?)'
                vals = (cleaned_str, str(artist_recom[key]))
                cur.execute(query1, vals)
                count +=1
                conn.commit()
        if count == 20:
            break

def main():

    createtables()
    cur.execute('SELECT artist FROM Artists')
    artists = cur.fetchall()
    table_insert(artists)
    
    cur.execute('SELECT artist_id FROM CarPlaylist')
    car_artists = cur.fetchall()
    carplaylist_table_insert(car_artists)

    cur.execute('SELECT artist_id FROM StudyPlaylist')
    study_artists = cur.fetchall()
    studyplaylist_table_insert(study_artists)


if __name__ == "__main__":
    main()