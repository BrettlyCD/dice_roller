import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

def game_stats(gameKey):
    conn = sqlite3.connect('dice.db')
    c = conn. cursor()
    c.execute("SELECT gameID, value FROM rollHistory")
    rolls = []
    for row in c.fetchall():
        if row[0] == gameKey:
            rolls.append(row[1]) # append each roll value to list
    
    font1 = {'size': 12}

    plt.hist(rolls)

    plt.title("Frequency of Dice Rolls", fontdict = font1)
    plt.xlabel("Roll Values", fontdict = font1)
    plt.ylabel("Frequency", fontdict = font1)

    plt.show()