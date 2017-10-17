#!/usr/bin/env bash
""" The run file should be written in bash and should be 
a one stop shop to launch your entire code"""

rm -rf __pycache__ # deletes previous pycache
rm -rf stockdata.db # deletes db created while last run

python3.6 create_db_pairs.py # create your .db file
python3.6 controller.py # Launch your code!!

