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


def get_recommendations_from_tastedive(bandName, key="349890-SI206Fin-N4RHDBVP"):
    baseurl="https://tastedive.com/api/similar"
    params_d = {}
    params_d["q"]= bandName
    params_d["k"]= key
    params_d["type"]= "music"
    params_d["limit"] = "3"
    resp = requests.get(baseurl, params=params_d)
    print(resp.url)
    respDic = resp.json()
    return respDic 

def setUpRecommForAll(cur, conn):
    count = 0
    cur.execute('SELECT artist FROM Artists')
    artists = cur.fetchall()


def main():
    #setUpRecommForStudy(list_study, cur, conn)
    #setUpRecommForCar(list_car, cur, conn)
    #setUpForAll(cur, conn)

if __name__ == "__main__":
    main()