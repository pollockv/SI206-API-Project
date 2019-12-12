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

cur, conn = setUpDatabase('edit_database.db')

def setUpRecommForAll(cur, conn):



def main():
    #setUpRecommForStudy(list_study, cur, conn)
    #setUpRecommForCar(list_car, cur, conn)
    #setUpForAll(cur, conn)

if __name__ == "__main__":
    main()