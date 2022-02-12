import sqlite3
import time
import datetime
import matplotlib.pyplot as plt #importing matplotlib below to show distribution of dice rolls
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

def open_connection():
    conn = sqlite3.connect('dice.db')
    c = conn.cursor()

def create_table(): 
    c.execute('CREATE TABLE IF NOT EXISTS rollHistory(rollID INTEGER PRIMARY KEY, datestamp TEXT, gameTitle TEXT, gameID TEXT, diceCount INTEGER, value INTEGER)')

    c.close()
    conn.close()

def data_entry(game, gameID, dice, roll):
    timevalue = time.time()
    date = str(datetime.datetime.fromtimestamp(timevalue).strftime('%Y-%m-%d %H:%M:%S'))

    conn = sqlite3.connect('dice.db')
    c = conn.cursor()

    c.execute("INSERT INTO rollHistory (datestamp, gameTitle, gameID, diceCount, value) VALUES (?, ?, ?, ?, ?)", (date, game, gameID, dice, roll))

    conn.commit()

    c.close()
    conn.close()

def data_delete():
    c.execute("DELETE FROM rollHistory")
    conn.commit()

def close_connection():
    c.close()
    conn.close()




