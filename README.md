# Meetup-15thOct

*The repository include code which was used during the "Python for Fintech" at Byte Academy of October 15th. There are 6.py files and one bash file. Below are brief descriptions for the code in each file - detailed descriptions are given in comments in each file. The broad scope of the meetup was to understand how to use the Markit API and stream live stock data into a SQL database.*

**Description of files**:
1) run.sh - bash file for running the entire program. Run using "./run.sh" on terminal/command prompt
2) controller.py - Code for taking user input
3) wrapper.py - Code for interacting with Markit API
4) Model.py - Code for parsing JSON and passing to ORM file 
5) ORM.py Code for injecting data fields into .db file
6) create_db.py - Code for using SQLite3 in python to create a database with specific schema
7) lookup_example - includes function to make simple API calls to Markit API

Markit Api v2 documentation: http://dev.markitondemand.com/MODApis/Api/v2/doc
