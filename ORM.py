#!/usr/bin/env python3.6

"""ORM stands for Object Relational Mapping. Here,
our objects (fields like "last price") are mapped 
onto appropriate columns"""

import sqlite3


connection = sqlite3.connect('stockdata.db')
cursor = connection.cursor()

#INSERT INTO MSFT
def update_msft(name,last_price,timestamp):
	cursor.execute('INSERT INTO msft (name,last_price,timestamp_) VALUES(?,?,?)',(name, last_price, timestamp))
	connection.commit()
	
#INSERT INTO GOOG
def update_goog(name,last_price,timestamp):
	cursor.execute('INSERT INTO goog (name,last_price,timestamp_) VALUES(?,?,?)',(name, last_price, timestamp))
	connection.commit()

#def get_df_msft(name):
#	df = pd.read_sql_query('SELECT * FROM msft WHERE name = "{}"'.format("Microsoft Corp"), connection)
#	return(df)
#def get_df_goog(name):
#	df1 = pd.read_sql_query('SELECT * FROM goog WHERE name = "{}"'.format("Alphabet Inc"), connection)
#	return(df1)	
#
#