import unittest
import sqlite3
import json
import os
import requests
import ast
import matplotlib.pyplot as plt

def visualizationBandsInTownPie():
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

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
    datadict = {}
    info = "This is a file containing percentage data for each country from our UpcomingEvents table."
    saveTextFile(info, 'calcBandsInTown.txt')
    cur.execute("SELECT count(country) FROM UpcomingEvents WHERE country = 'United States';")
    us_number = cur.fetchall()[0][0]
    cur.execute("SELECT count(country) FROM UpcomingEvents;")
    total_number = cur.fetchall()[0][0]
    print(us_number)
    print(total_number)
    percent_us = us_number / total_number * 100
    for item in datadict:
        saveTextFile(item, 'calcBandsInTown.txt')
        

def main():
    #joinLatLong(cur, conn)
    calcBandsInTown(cur, conn)

if __name__ == "__main__":
    main()