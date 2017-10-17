#!/usr/bin/env python3.6

#The wrapper should include code for interacting with API


import requests
import pandas as pd
import json

# create a class of API URL's. Here the class Markit includes
# a class for the Google and Microsoft url's. 
class Markit:
	
	def __init__(self):
		self.msft_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol=MSFT"
		self.goog_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol=GOOG"

	def get_quote_msft(self):
		try:
			url_msft = requests.get(self.msft_url)
			content = url_msft.content	
			msft_quote = json.loads(content)
			return msft_quote
		except:
			pass
			

	def get_quote_goog(self):
		try:
			url_goog = requests.get(self.goog_url)
			content = url_goog.content
			goog_quote = json.loads(content)
			return goog_quote
		except:
			pass

		
