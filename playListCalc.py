import matplotlib.pyplot as plt
import sqlite3
import unittest
import os
import json
import requests
import ast
from wordcloud import WordCloud, STOPWORDS 
import pandas as pd 
import numpy as np

def saveTextFile(data,filename):
    outfile = open(filename, 'w')
    outfile.write(data)
    outfile.close()

def get_artist_playList(db_filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, db_filename)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    info = "This will calculate how many times an artist appeared in play list/n"
    saveTextFile(info, 'calcDistance.txt')

    cur.execute("SELECT artist, COUNT(StudyPlaylist.artist_id) FROM StudyPlaylist JOIN Artists WHERE StudyPlaylist.artist_id = Artists.artist_id GROUP BY StudyPlaylist.artist_id")
    Study_results = cur.fetchall()
    print("Study PlayList")      
    print(Study_results)
    
    cur.execute("SELECT artist, COUNT(CarPlaylist.artist_id) FROM CarPlaylist JOIN Artists WHERE CarPlaylist.artist_id = Artists.artist_id GROUP BY CarPlaylist.artist_id")
    Car_results = cur.fetchall()     
    print("Car PlayList")  
    print(Car_results)

    conn.close()
    calc_Artistfreq_PlayList(Study_results, Car_results)

    draw_ScatterPlot(Study_results, Car_results)


def draw_ScatterPlot(playList1, playList2):
    x1=[]
    y1=[]
    x2=[]
    y2=[]

    for artist1 in playList1:
        x1.append(artist1[0])
        y1.append(artist1[1])

    for artist2 in playList2:
        x2.append(artist2[0])
        y2.append(artist2[1])

    plt.scatter(x1,y1, label='Study PlayList', color='blue', s=50, marker="o")
    plt.scatter(x2,y2, label='Car PlayList', color='red', s=50, marker="o")
    # plt.figure(figsize=(20,20))
    plt.gcf().set_size_inches((20, 20))    

    plt.xlabel('Artist Name')
    plt.ylabel('Frequency')
    plt.title('Car List and Study List Match')
    plt.xticks(rotation=90)
    plt.show()
    

def calc_Artistfreq_PlayList(list1, list2):

    freq_list = []
    for item1 in list1:
        for item2 in list2:
            if item1[0] == item2[0]:
                newValue = item1[1] + item2[1]
                freq_list.append((item1[0], newValue))
    
    print(freq_list)

    words = ""
    for item in freq_list:
        words = words+item[0]+" "
        saveTextFile(words, 'playList.txt')
    draw_wordcloud(words)
    # draw_barchart(freq_list)
    # draw_ScatterPlot(freq_list)
    


def draw_wordcloud(artits):
    wordcloud = WordCloud(max_font_size=40).generate(artits)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# def draw_barchart(playList):
#     plt.title('Car List and Study List Match')
#     x=[]
#     y=[]
#     # sorted_Dict = sorted(cat_dict.items())
#     for artist in playList:
#         x.append(artist[0])
#         y.append(artist[1])

#     plt.bar(x,y) 
#     plt.colorbar()
#     plt.xlabel("Artist Name")
#     plt.ylabel("Frequency")
#     plt.xticks(rotation=90)
#     plt.tight_layout()
#     plt.show()


# def draw_ScatterPlot(playList):
#     x=[]
#     y=[]
#     for artist in playList:
#         x.append(artist[0])
#         y.append(artist[1])
        

#     plt.scatter(x,y, label='Times appear in Play Lists', color='b,k', s=25, marker="o")

#     plt.xlabel('Artist Name')
#     plt.ylabel('Frequency')
#     plt.title('Car List and Study List Match')
#     plt.legend()
#     plt.xticks(rotation=90)
#     plt.show()



def main():
    get_artist_playList("spotify_database.db")
    
if __name__ == "__main__":
    main()


