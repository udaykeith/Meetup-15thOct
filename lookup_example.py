#!/usr/bin/env python3.6

#Code to try and use the API independently of the database

import requests
import json

lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

def get_lookup(stock):
	try:
		api_lookup = requests.get(lookup_url+stock)
		data = api_lookup.content	
		quote = json.loads(data)
		return quote
	except:
			pass
#def get_quote(symbol)
print((get_lookup("MSFT")))