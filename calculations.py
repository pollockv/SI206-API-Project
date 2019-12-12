import unittest
import sqlite3
import json
import os
import requests
import ast


def saveTextFile(data,filename):
    outfile = open(filename, 'w')
    outfile.write(data)
    outfile.close()

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

cur, conn = setUpDatabase('spotify_database.db')

def joinLatLong(cur, conn):
    cur.execute("SELECT latitude, longitude FROM LongitudeForEvents JOIN LatitudeForEvents;")

def calcBandsInTown(cur, conn):
    cur.execute("SELECT count(country) FROM UpcomingEvents WHERE country = 'United States';")
    us_number = cur.fetchall()[0][0]
    cur.execute("SELECT count(country) FROM UpcomingEvents;")
    total_number = cur.fetchall()[0][0]
    print(us_number)
    print(total_number)
    percent = us_number / total_number * 100
    print("{}%".format(percent))
        

def main():
    #joinLatLong(cur, conn)
    calcBandsInTown(cur, conn)

if __name__ == "__main__":
    main()