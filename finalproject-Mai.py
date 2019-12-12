import requests

# https://tastedive.com/api/similar?q=red+hot+chili+peppers%2C+pulp+fiction

def get_recommendations_from_tastedive(bandName, key="349890-SI206Fin-N4RHDBVP"):
    baseurl="https://tastedive.com/api/similar"
    params_d = {}
    params_d["q"]= bandName
    params_d["k"]= key
    params_d["type"]= "music"
    params_d["limit"] = "20"
    resp = requests.get(baseurl, params=params_d)
    print(resp.url)
    respDic = resp.json()
    return respDic



# def extract_movie_titles(bandName):
#     result=[]
#     for listRes in bandName['Similar']['Results']:
#         result.append(listRes['Name'])
#     return result

# def get_related_titles(listMovieName):
#     if listMovieName != []:
#         auxList=[]
#         relatedList=[]
#         for bandName in listMovieName:
#             auxList = extract_movie_titles(get_recommendations_from_tastedive(bandName))
#             for movieNameAux in auxList:
#                 if movieNameAux not in relatedList:
#                     relatedList.append(movieNameAux)
        
#         return relatedList
#     return listMovieName















# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
# client_id = "9db9eeacd0004463b836ed7e1c7869e8"
# client_secret = "2eb76cf70264493abde544ba5a65a1ae"
# client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

# name = "Playlist 1" #chosen artist
# result = sp.search(name) #search query
# print(result['tracks']['items'][0]['artists'])

# # SQL for putting values into db tables
# # INSERT INTO table_name (column1, column2, column3, ...)
# # VALUES (value1, value2, value3, ...);