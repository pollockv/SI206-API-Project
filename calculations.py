import unittest
import sqlite3
import json
import os
import requests
import ast
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 
import pandas as pd 
import numpy as np
from math import sin, cos, sqrt, atan2, radians
import geoplotlib
import pandas as pd
from geoplotlib.utils import read_csv

def saveTextFile(data,filename):
    outfile = open(filename, 'w')
    outfile.write(data)
    outfile.close()

def readDataFromFile(filename):
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)
    return json_data

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    # conn.close()
    return cur, conn

cur, conn = setUpDatabase('spotify_database.db')

#percentage data for USA events from our UpcomingEvents table
def calcBandsInTown(cur, conn):
    cur.execute("SELECT count(country) FROM UpcomingEvents WHERE country = 'United States';")
    us_number = cur.fetchall()[0][0]
    cur.execute("SELECT count(country) FROM UpcomingEvents;")
    total_number = cur.fetchall()[0][0]
    percent_us = us_number / total_number * 100

    info = "This is a file containing percentage data for USA events from our UpcomingEvents table.\n"
    us_str = "Number of events in USA: " +str(us_number) + "\n"
    total_str = "Total Number of events: " +str(total_number) + "\n"
    percent_str = "Percentage for events in USA: " +str(percent_us) + "\n"
    combined_str = info + us_str + total_str + percent_str
    saveTextFile(combined_str, 'calcBandsInTown.txt')

    visualizationBandsInTownPie(us_number,total_number)
        
def visualizationBandsInTownPie(us_number,total_number):
    labels = 'United State', 'Other countries'
    sizes = [us_number, (total_number)-(us_number)]
    explode = (0.1, 0) 

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal') 
    plt.show()

#************************************************************************************

#percentage data for each country from our UpcomingEvents table
def get_events_by_country(cur, conn):
    cur.execute("SELECT country, count(country) from UpcomingEvents GROUP BY country")
    events_by_country = cur.fetchall()
    print("Events by country:")      
    print(events_by_country)
    draw_barchart(events_by_country)

def draw_barchart(CountryList):
    plt.title('Events in each country')
    x=[]
    y=[]
    for country in CountryList:
        x.append(country[0])
        y.append(country[1])

    plt.bar(x,y) 
    plt.xlabel("Country Name")
    plt.ylabel("Frequency")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()    
#************************************************************************************

#get distance between a venue and University of Michigan
def get_Long_Lat(cur, conn):
    info = "This function will calculate the distance between the concert venue you input and the University of Michigan\n\n **********************************\n\n"

    venue = input("Enter venue : ")
    cur.execute("SELECT latitude, longitude FROM LongitudeForEvents JOIN LatitudeForEvents JOIN UpcomingEvents WHERE venue=(?) and LatitudeForEvents.event_id = UpcomingEvents.event_id and LongitudeForEvents.event_id = UpcomingEvents.event_id", (venue,))
    results = cur.fetchall()

    Distance = calDistance(float(results[0][0]), float(results[0][1]))
    yourinput = "Your input was: " + venue + "\n\n"
    result_txt = "The Distance between " + venue + " and University of Michigan is: " + str(Distance)
    combined_str = info + yourinput + result_txt
    saveTextFile(combined_str, 'calcDistance.txt')
    DistanceVisual(float(results[0][0]), float(results[0][1]),venue,Distance)

def calDistance(lat, lon):
#calculate distance between University of Michigan and event venu in km
    R = 6373.0

    lat1 = radians(lat)
    lon1 = radians(lon)
    coord1 = "The first set of coordinates is ({},{})\n".format(lat1,lon1)

    lat2 = radians(42.2780)
    lon2 = radians(-83.7382)
    coord1 = "The second set of coordinates is ({},{})\n".format(lat2,lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = round((R * c),2)
    
    return distance

def DistanceVisual(lat1, lon1,venue, distance): 
    locs = pd.DataFrame({'name': ['University of Michigan',venue+" "+ str(distance)+" km"],'lat': [42.2780, lat1], 'lon': [-83.7382, lon1]})
    geoplotlib.dot(locs, color='b', point_size= 20,f_tooltip=lambda r:r['name'])
    geoplotlib.show()

#************************************************************************************

#This will calculate how many times an artist appeared in each play list
def get_artist_playList(cur, conn):
    info = "This will calculate how many times an artist appeared in a playlist\n"

    cur.execute("SELECT artist, COUNT(StudyPlaylist.artist_id) FROM StudyPlaylist JOIN Artists WHERE StudyPlaylist.artist_id = Artists.artist_id GROUP BY StudyPlaylist.artist_id")
    Study_results = cur.fetchall()
    print("Study PlayList")      
    study_str = "\n**********************************\n\nStudy Playlist Frequency:\n\n" + str(Study_results)
    
    cur.execute("SELECT artist, COUNT(CarPlaylist.artist_id) FROM CarPlaylist JOIN Artists WHERE CarPlaylist.artist_id = Artists.artist_id GROUP BY CarPlaylist.artist_id")
    Car_results = cur.fetchall()     
    car_str = "\n**********************************\n\nCar Playlist Frequency:\n\n" + str(Car_results)
    print(Car_results)

    combined_str = info + study_str + car_str
    saveTextFile(combined_str, 'calcArtistFrequency.txt')
    calc_Artistfreq_PlayList(Study_results, Car_results)


def calc_Artistfreq_PlayList(list1, list2):
    freq_list = []
    for item1 in list1:
        for item2 in list2:
            if item1[0] == item2[0]:
                newValue = item1[1] + item2[1]
                freq_list.append((item1[0], newValue))

    words = ""
    for item in freq_list:
        words = words+item[0]+" "
    info = "The list of Artists that appear in both playlists:\n\n ******************************\n\n" + words
    saveTextFile(info, "calcPlaylistArtistFreq.txt")
    draw_wordcloud(words)

def draw_wordcloud(artits):
    wordcloud = WordCloud(max_font_size=40).generate(artits)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
#************************************************************************************




#************************************************************************************

def main():
    calcBandsInTown(cur, conn)
    get_events_by_country(cur, conn)
    get_artist_playList(cur, conn)
    get_Long_Lat(cur, conn)


if __name__ == "__main__":
    main()