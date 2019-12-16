from math import sin, cos, sqrt, atan2, radians
import matplotlib.pyplot as plt
import sqlite3
import unittest
import os
import json
import requests
import ast
import geoplotlib
import pandas as pd

from geoplotlib.utils import read_csv
# import numpy as np
# from mpl_toolkits.basemap import Basemap

def saveTextFile(data,filename):
    outfile = open(filename, 'w')
    outfile.write(data)
    outfile.close()



def get_Long_Lat(db_filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, db_filename)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    info = "This function will calculate the distance between concert venue and University of Michigan/n"
    saveTextFile(info, 'calcDistance.txt')

    venue = input("Enter venu : ")
    # query = "SELECT latitude, longitude FROM LongitudeForEvents JOIN LatitudeForEvents JOIN UpcomingEvents WHERE venue=? and LatitudeForEvents.event_id = UpcomingEvents.event_id and LongitudeForEvents.event_id = UpcomingEvents.event_id", (venue)
    cur.execute("SELECT latitude, longitude FROM LongitudeForEvents JOIN LatitudeForEvents JOIN UpcomingEvents WHERE venue=(?) and LatitudeForEvents.event_id = UpcomingEvents.event_id and LongitudeForEvents.event_id = UpcomingEvents.event_id", (venue,))
    results = cur.fetchall()      
    print(results)

    conn.close()
    result_txt = "The Distance between " +venue+ "and University of Michigan is: "
    saveTextFile(result_txt, 'calcDistance.txt')

    Distance = calDistance(float(results[0][0]), float(results[0][1]))
    
    saveTextFile(str(Distance), 'calcDistance.txt')
    DistanceVisual(float(results[0][0]), float(results[0][1]),venue,Distance)
    

def calDistance(lat, lon):
# approximate radius of earth in km
#calculate distance between University of Michigan and event venu
    R = 6373.0

    lat1 = radians(lat)
    lon1 = radians(lon)

    lat2 = radians(42.2780)
    lon2 = radians(-83.7382)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = round((R * c),2)
    

    print("Result: ", distance)
    return distance

def DistanceVisual(lat1, lon1,venue, distance):
    # Dataframe containing the data to plot    
    locs = pd.DataFrame({'name': ['University of Michigan',venue+" "+ str(distance)+" km"],'lat': [42.2780, lat1], 'lon': [-83.7382, lon1]})
    #function to create a dot density map with annotated tooltip
    geoplotlib.dot(locs, color='b', point_size= 20,f_tooltip=lambda r:r['name'])
    # ui_manager.info("Distance = " +distance)
    geoplotlib.show()

    # data = 42.2780, -83.7382, lat, lon
    # geoplotlib.voronoi(data,linecolor=’b’)
    # geoplotlib.graph(data,
    #              src_lat= "from",
    #              src_lon="from",
    #              dest_lat="to",
    #              dest_lon="to",
    #              color='hot_r',
    #              alpha=16,
    #              linewidth=2)


def main():
    get_Long_Lat("spotify_database.db")
    

if __name__ == "__main__":
    main()
