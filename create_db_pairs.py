#!/usr/bin/env python3.6

import sqlite3

#table 1 = insert into msft
#table 2 = insert into goog

connection = sqlite3.connect('stockdata.db')
cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE msft (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(128),
        last_price FLOAT(128),
        timestamp_ TIMESTAMP(128)
    );'''
)

cursor.execute(
    '''CREATE TABLE goog (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(128),
        last_price FLOAT(128),
        timestamp_ TIMESTAMP(128)
    );'''
)

#cursor.execute(
#   '''CREATE TABLE correlation (
#      pk INTEGER PRIMARY KEY AUTOINCREMENT,
#	  timestamp_ TIMESTAMP(128),
#	  r_percent_change FLOAT(128)	



connection.commit()
cursor.close()
connection.close()
