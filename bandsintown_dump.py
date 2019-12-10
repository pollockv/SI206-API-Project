import unittest
import requests
import sqlite3
import json
import os
import sys

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