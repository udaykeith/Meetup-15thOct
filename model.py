#!/usr/bin/env python3.6 

"""The model should include the "bussiness logic". Here the "logic"
is to select only a certain parameters and add them to
specific columns."""

from wrapper import Markit
import ORM
from time import sleep



def get_data():
		markit = Markit()
		try:
			name = (markit.get_quote_msft())["Name"]
		except:
			pass
		try:
			last_price = (markit.get_quote_msft())["LastPrice"]
		except:
			pass
		try:
			timestamp = (markit.get_quote_msft())["Timestamp"]
		except:
			pass
		try:
			name1 = (markit.get_quote_goog())["Name"]
		except:
			pass
		try:
			last_price1 = (markit.get_quote_goog())["LastPrice"]
		except:
			pass
		try:
			timestamp1 = (markit.get_quote_goog())["Timestamp"]
		except:
			pass
		try:
			ORM.update_goog(name1,last_price1,timestamp1)
		except:
			pass
		try:
			ORM.update_msft(name,last_price,timestamp)
		except:
			pass
		sleep(5)
		get_data()
		
		


#def review_correlation_simul():
	#ORM.get_df_goog(name)
	#ORM.get_df_msft(name1)
	#return df1.corrwith(df)
	# execute every minute


