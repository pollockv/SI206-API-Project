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

cur, conn = setUpDatabase('database.db')

def get_recommendations_from_tastedive(artist, key="349890-SI206Fin-N4RHDBVP"):
    baseurl="https://tastedive.com/api/similar"
    params_d = {}
    params_d["q"]= artist
    params_d["k"]= key
    params_d["type"]= "music"
    params_d["limit"] = "3"
    resp = requests.get(baseurl, params=params_d)
    print(resp.url)
    respDic = resp.json()
    return respDic 


def table_insert(artist):
    count = 0
    artist_recom = {}
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
            sql_query = 'INSERT INTO RecommForAll(all_artists, list_of_rec) VALUES (?,?)'
            vals = (cleaned_str, str(artist_recom[key]))
            cur.execute(sql_query, vals)
            count +=1
            conn.commit()
        if count == 20:
            break

def main():
    createtables()
    cur.execute('SELECT artist FROM Artists')
    artists = cur.fetchall()
    for artist in artists:
        table_insert(artist)

if __name__ == "__main__":
    main()