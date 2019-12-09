#insert into database
#need two tables for each API (6 tables in all!)
    #at least two tables must share a key
#have to limit how many items you store in a database each time code is run (only 20 items at a time)
#need atleast 100 items in database from each API (300 in total)

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

#2 tables required for Spotify API
#data is the dictionaries that we made ('results_for_study', 'results_for_car')

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
    #have no damn idea how to do the limit thing but i think that's okay
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
    cur.execute('CREATE TABLE IF NOT EXISTS CarPlaylist(artist TEXT, songname TEXT)')
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


cur, conn = setUpDatabase('spotify.db')
setUpStudyPlaylist(results_for_study, cur, conn)
setUpCarPlaylist(results_for_car, cur, conn)