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

#three tables for Spotify API

def setUpArtists(results1, results2, cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS Artists(artist_id INTEGER PRIMARY KEY, artist TEXT UNIQUE)')
    limit1 = list(results1)[0:21]
    limit2 = list(results1)[20:41]
    limit3 = list(results1)[41:]
    l1= list(results2)[0:21]
    l2= list(results2)[20:41]
    l3= list(results2)[41:]
    for artist in limit1:
        cur.execute('INSERT OR IGNORE INTO Artists(artist_id, artist) VALUES (NULL ,?)', ( artist, ))
    for artist in limit2:
        cur.execute('INSERT OR IGNORE INTO Artists(artist_id, artist) VALUES (NULL ,?)', (artist, ))
    for artist in limit3:
        cur.execute('INSERT OR IGNORE INTO Artists(artist_id, artist) VALUES (NULL ,?)', (artist, ))
    for artist in l1:
        cur.execute('INSERT OR IGNORE INTO Artists(artist_id, artist) VALUES (NULL ,?)', (artist, ))
    for artist in l2:
        cur.execute('INSERT OR IGNORE INTO Artists(artist_id, artist) VALUES (NULL ,?)', (artist, ))
    for artist in l3:
        cur.execute('INSERT OR IGNORE INTO Artists(artist_id, artist) VALUES (NULL ,?)', (artist, ))
    conn.commit()

def setUpStudyPlaylist(data, cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS StudyPlaylist(artist_id INTEGER, songname TEXT)')
    limit1 = list(data.items())[0:21]
    limit2 = list(data.items())[20:41]
    limit3 = list(data.items())[41:]
    for item in limit1:
        if len(item[1])==1:
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO StudyPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][0])
            cur.execute(sql_query, vals)
        else:
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO StudyPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][0])
            cur.execute(sql_query, vals)
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO StudyPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][1])
            cur.execute(sql_query, vals)
    for item in limit2:
        if len(item[1])==1:
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0]
            sql_query = 'INSERT INTO StudyPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][0])
            cur.execute(sql_query, vals)
        else:
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO StudyPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][0])
            cur.execute(sql_query, vals)
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO StudyPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][1])
            cur.execute(sql_query, vals)
    for item in limit3:
        if len(item[1])==1:
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0]
            sql_query = 'INSERT INTO StudyPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][0])
            cur.execute(sql_query, vals)
        else:
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO StudyPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][0])
            cur.execute(sql_query, vals)
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO StudyPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][1])
            cur.execute(sql_query, vals)
    conn.commit()

def setUpCarPlaylist(data, cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS CarPlaylist(artist_id INTEGER, songname TEXT)')
    limit1 = list(data.items())[0:21]
    limit2 = list(data.items())[20:41]
    limit3 = list(data.items())[41:]
    #have no damn idea how to do the limit thing but i think that's okay
    for item in limit1:
        if len(item[1])==1:
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO CarPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][0])
            cur.execute(sql_query, vals)
        else:
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO CarPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][0])
            cur.execute(sql_query, vals)
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO CarPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][1])
            cur.execute(sql_query, vals)
    for item in limit2:
        if len(item[1])==1:
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0]
            sql_query = 'INSERT INTO CarPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][0])
            cur.execute(sql_query, vals)
        else:
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO CarPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][0])
            cur.execute(sql_query, vals)
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO CarPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][1])
            cur.execute(sql_query, vals)
    for item in limit3:
        if len(item[1])==1:
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0]
            sql_query = 'INSERT INTO CarPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][0])
            cur.execute(sql_query, vals)
        else:
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO CarPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][0])
            cur.execute(sql_query, vals)
            cur.execute("SELECT artist_id From Artists WHERE artist = ?", (item[0], ))
            artist_id = cur.fetchall()[0][0] #returns list of tuples
            sql_query = 'INSERT INTO CarPlaylist(artist_id, songname) VALUES (?,?)'
            vals = (artist_id, item[1][1])
            cur.execute(sql_query, vals)
    conn.commit()


#three tables for TasteDive API

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
    cur.execute('CREATE TABLE IF NOT EXISTS RecommForAll(all_artists TEXT, list_of_rec LIST)')
    cur.execute('SELECT artist FROM Artists')
    artists = cur.fetchall()
    artist_recom = {}
    for art in artists:
        artist = art[0]
        result_lst = get_recommendations_from_tastedive(artist, key="349890-SI206Fin-N4RHDBVP")['Similar']['Results']
        for recom in result_lst:
            if artist in artist_recom:
                artist_recom[artist].append(recom['Name'])
            else:
                artist_recom[artist] = [recom['Name']]
    for key in artist_recom:
        sql_query = 'INSERT INTO RecommForAll(all_artists, list_of_rec) VALUES (?,?)'
        vals = (key, str(artist_recom[key]))
        cur.execute(sql_query, vals)
    conn.commit()

def setUpRandomRecommForStudy(list_data, cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS RecommForStudy(random_artist TEXT, list_of_rec LIST)')
    artist_recom = {}
    for artist in list_data:
        result_lst = get_recommendations_from_tastedive(artist, key="349890-SI206Fin-N4RHDBVP")['Similar']['Results']
        for recom in result_lst:
            if artist in artist_recom:
                artist_recom[artist].append(recom['Name'])
            else:
                artist_recom[artist] = [recom['Name']]
    for key in artist_recom:
        sql_query = 'INSERT INTO RecommForStudy(random_artist, list_of_rec) VALUES (?,?)'
        vals = (key, str(artist_recom[key]))
        cur.execute(sql_query, vals)
    conn.commit()

def setUpRandomRecommForCar(list_data, cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS RecommForCar(random_artist TEXT, list_of_rec LIST)')
    artist_recom = {}
    for artist in list_data:
        result_lst = get_recommendations_from_tastedive(artist, key="349890-SI206Fin-N4RHDBVP")['Similar']['Results']
        for recom in result_lst:
            if artist in artist_recom:
                artist_recom[artist].append(recom['Name'])
            else:
                artist_recom[artist] = [recom['Name']]
    for key in artist_recom:
        sql_query = 'INSERT INTO RecommForCar(random_artist, list_of_rec) VALUES (?,?)'
        vals = (key, str(artist_recom[key]))
        cur.execute(sql_query, vals)
    conn.commit()

#tables for BandsinTown API

def get_bandsintown_events(bandName, id="75771b0391833569dedd2b5ceff8d2af", date="upcoming"):
    eventdict = {}
    base_url = "https://rest.bandsintown.com/artists/" + bandName + "/events?app_id=" + id + "&date=" + date
    resp = requests.get(base_url)
    if resp != []:
        eventdict = resp.json()
        return eventdict
    else:
        return []


def setUpUpcomingEvents(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS UpcomingEvents(event_id INTEGER PRIMARY KEY, artist_name TEXT, venue TEXT, city TEXT, country TEXT)')
    cur.execute('SELECT list_of_rec FROM RecommForAll')
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
            for event in eventlist:
                venue = event['venue']['name']
                city = event['venue']['city']
                country = event['venue']['country']
                finallist.append([artist_name, venue, city, country])
    for event in finallist:
        sql_query = 'INSERT INTO UpcomingEvents(event_id, artist_name, venue, city, country) VALUES (NULL, ?,?,?,?)'
        vals = (event[0], event[1], event[2], event[3])
        cur.execute(sql_query, vals)
    conn.commit()

def setUpLatitude(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS LatitudeForEvents(event_id INTEGER, latitude TEXT)')
    edit_list = []
    revise_lst = []
    finallist = []
    no_repeats = []
    cur.execute('SELECT list_of_rec FROM RecommForAll')
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
            for event in eventlist:
                venue = event['venue']['name']
                city = event['venue']['city']
                if 'latitude' not in event['venue']:
                    lat = ''
                    finallist.append([artist_name, venue, city, lat])
                else:
                    lat = event['venue']['latitude']
                    finallist.append([artist_name, venue, city, lat])
    for event in finallist:
        if event not in no_repeats:
            no_repeats.append(event)
    for event in no_repeats:
        cur.execute("SELECT event_id From UpcomingEvents WHERE artist_name = ? AND venue = ? AND city = ?", (event[0], event[1], event[2]))
        event_id = cur.fetchall()[0][0]
        sql_query = 'INSERT INTO LatitudeForEvents(event_id, latitude) VALUES (?,?)'
        vals = (event_id, event[1][3])
        cur.execute(sql_query, vals)
    conn.commit()
        




        

results_for_study = {'Maroon 5': ['Memories'], 'Selena Gomez': ['Lose You To Love Me'], 'Coldplay': ['Orphans'], 'Shawn Mendes': ["If I Can't Have You"], 'Khalid': ['Saturday Nights'], 'Travis Scott': ['HIGHEST IN THE ROOM'], 'Eminem': ['The Ringer'], 'Drake': ['Dreams Money Can Buy', '5 Am in Toronto'], 'Arctic Monkeys': ['Do I Wanna Know?'], 'Linkin Park': ['In the End', 'Numb', "What I've Done"], 'Panic! At The Disco': ['High Hopes', 'Death of a Bachelor'], 'Lil Nas X': ['Panini'], 'Dan + Shay': ['Speechless'], 'Luke Bryan': ["Knockin' Boots"], 'The 1975': ['Frail State Of Mind'], 'Usher': ['U Remind Me'], 'Paramore': ['Emergency'], 'One Direction': ['History'], 'Nicki Minaj': ['Run & Hide', 'Want Some More'], 'Cardi B': ['Press'], 'Madonna': ['Material Girl'], 'Taylor Swift': ['I Forgot That You Existed'], 'Kelly Clarkson': ['Broken & Beautiful (from the movie UGLYDOLLS)'], 'Dua Lipa': ["Don't Start Now"], 'Meghan Trainor': ['Hurt Me - From "Songland"'], 'Alessia Cara': ['Scars To Your Beautiful', 'Ready'], 'Carly Rae Jepsen': ['Party For One'], 'Miley Cyrus': ['Party In The U.S.A.'], 'Lorde': ['Supercut'], 'Florida Georgia Line': ['H.O.L.Y.'], 'Aerosmith': ['I Don\'t Want to Miss a Thing - From the Touchstone film, "Armageddon"'], 'Céline Dion': ['Lovers Never Die'], 'Bastille': ['Joy'], '5 Seconds of Summer': ['Lie To Me'], 'Charlie Puth': ['Patient'], 'Jay Sean': ['Emergency'], 'A R I Z O N A': ['Freaking Out'], 'Jason Mraz': ["Let's See What The Night Can Do", "I'm Yours"], 'Mike Posner': ['Stuck In The Middle'], 'The Vamps': ['Missing You'], 'Ellie Goulding': ['Flux'], 'A$AP Rocky': ['Distorted Records', 'Kids Turned Out Fine'], 'King Princess': ['Tough On Myself'], 'Bryson Tiller': ["Don't"], 'OneRepublic': ['Rescue Me'], 'Kito': ['Wild Girl'], 'Ralph': ['Gravity'], 'Shura': ['Touch'], 'Rina Sawayama': ['Cherry'], 'LIZ': ['When I Rule the World'], 'Lizzo': ['Good as Hell (feat. Ariana Grande) - Remix'], 'Natasha Bedingfield': ['Unwritten'], 'Corinne Bailey Rae': ['Put Your Records On'], 'Kina Grannis': ['For Now'], 'Villagers': ['Nothing Arrived - Live from Spotify London'], 'SOPHIE': ['Immaterial'], 'Sam Smith': ['How Do You Sleep?'], 'Jonas Brothers': ['Greenlight - From "Songland"'], 'Local Natives': ['Dark Days'], 'Clairo': ['Flaming Hot Cheetos'], 'Tame Impala': ['The Less I Know The Better'], 'Tennis': ["Ladies Don't Play Guitar"], 'Alvvays': ['In Undertow'], 'Real Estate': ['Darling']}
results_for_car = {'Maroon 5': ['Memories'], 'Khalid': ['Up All Night'], 'Sam Smith': ['How Do You Sleep?', "I'm Not The Only One"], 'Jonas Brothers': ['Sucker'], 'Eminem': ['Greatest'], 'Drake': ['The Motion'], 'Arctic Monkeys': ['R U Mine?', 'One For The Road'], 'Panic! At The Disco': ['Hey Look Ma, I Made It', 'Lying Is the Most Fun a Girl Can Have Without Taking Her Clothes Off'], 'Dan + Shay': ['Tequila'], 'Luke Bryan': ['Play It Again', 'Country Girl (Shake It For Me)'], 'Frank Ocean': ['In My Room'], 'Lana Del Rey': ['Cinnamon Girl'], 'Beyoncé': ['Me, Myself and I'], 'All Time Low': ['Dear Maria, Count Me In'], 'Paramore': ['Misery Business', 'Ignorance'], 'Lizzo': ['Juice'], 'Ariana Grande': ['One Last Time'], 'Justin Bieber': ['Love Yourself'], 'Little Mix': ['Black Magic'], 'Bruno Mars': ["That's What I Like"], 'Lady Gaga': ['Million Reasons'], 'Rihanna': ['Take A Bow'], 'OneRepublic': ['Apologize'], 'Nicki Minaj': ['Win Again'], 'Fleetwood Mac': ['In the Back of My Mind', 'Affairs of the Heart', 'All over Again'], 'Hailee Steinfeld': ['Most Girls'], 'Demi Lovato': ['Sorry Not Sorry'], 'Troye Sivan': ['My My My!'], 'Ed Sheeran': ['Supermarket Flowers'], 'John Mayer': ['Carry Me Away'], 'The Script': ['Something Unreal'], 'Hozier': ['Almost (Sweet Music)'], 'Adele': ['When We Were Young'], 'P!nk': ['Walk Me Home'], 'A$AP Rocky': ['Buck Shots'], 'Michael Bublé': ["It's Beginning to Look a Lot like Christmas"], 'Paul McCartney': ['Wonderful Christmastime (Edited Version) [Remastered]'], 'Sia': ["Santa's Coming For Us"], 'Christina Aguilera': ['This Christmas'], 'John Legend': ['Bring Me Love'], 'The Weeknd': ['Die For You'], 'Childish Gambino': ['Sober'], 'G-Eazy': ['Scary Nights'], 'The Aces': ['Stuck'], 'Tei Shi': ['Keep Running'], 'ABRA': ['Fruit'], 'FKA twigs': ['home with you'], 'Harry Styles': ['Watermelon Sugar'], 'Meghan Trainor': ["I'll Be Home"], 'Phil Collins': ["You'll Be In My Heart"], 'JoJo': ['Leave (Get Out) - 2018'], 'The Milk Carton Kids': ['A Sea of Roses'], 'Yumi Zouma': ['In Camera'], 'COIN': ['Cemetery'], 'King Princess': ['You Destroyed My Heart'], 'Yellow Days': ['The Way Things Change'], 'Robyn': ['Baby Forgive Me'], 'Toro y Moi': ['Girl Like You']}
list_study = ['Clairo', 'One Direction', 'Jonas Brothers', 'Aerosmith', 'Tame Impala', 'Dan + Shay', 'Taylor Swift', 'Nicki Minaj', 'OneRepublic', 'Jason Mraz']
list_car = ['Hozier', 'The Milk Carton Kids', 'Troye Sivan', 'Yumi Zouma', 'Rihanna', 'Childish Gambino', 'Meghan Trainor', 'A$AP Rocky', 'ABRA', 'Christina Aguilera']
#example: {'Similar': {'Info': [{'Name': 'Maroon 5', 'Type': 'music'}], 'Results': [{'Name': 'Adam Levine', 'Type': 'music'}, {'Name': 'Onerepublic', 'Type': 'music'}, {'Name': 'Train', 'Type': 'music'}, {'Name': 'Bruno Mars', 'Type': 'music'}, {'Name': 'The Script', 'Type': 'music'}, {'Name': 'The Wanted', 'Type': 'music'}, {'Name': 'James Blunt', 'Type': 'music'}, {'Name': 'Justin Timberlake', 'Type': 'music'}, {'Name': 'Jason Mraz', 'Type': 'music'}, {'Name': 'Flo Rida', 'Type': 'music'}]}}
#setUpArtists(results_for_study, results_for_car, cur, conn)
#setUpStudyPlaylist(results_for_study, cur, conn)
#setUpCarPlaylist(results_for_car, cur, conn)
setUpRandomRecommForStudy(list_study, cur, conn)
setUpRandomRecommForCar(list_car, cur, conn)
setUpRecommForAll(cur, conn)
setUpUpcomingEvents(cur, conn)
setUpLatitude(cur, conn)
#setUpLongitude