import unittest
import sqlite3
import json
import os
import requests
import ast

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

cur, conn = setUpDatabase('spotify_database.db')


def joinLatLong(cur, conn):
    cur.execute("SELECT City, Country FROM Customers WHERE Country='Germany UNION ALL SELECT City, Country FROM Suppliers EXCEPT ORDER BY City;")
        
#joinLatLong(cur, conn)