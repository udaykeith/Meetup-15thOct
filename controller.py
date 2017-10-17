#!/usr/bin/env python3.6

"""The controller should include code for user interaction
and should be the porthole into running the rest of your code.
To do this we need to call the model and wrapper code"""

import wrapper 
import model
from time import sleep
from random import uniform

			
def begin_scraping():
	start = input("""Select the desired option: \n
	1. Start Scraping \n""")
	start = int(start)
	# other_start = if you want to scrape and explore other options, press 2:
	if start == 1:
		model.get_data()
		#model.get_goog_data()

		

begin_scraping()