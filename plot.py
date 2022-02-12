import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

def game_stats(gameKey):
    conn = sqlite3.connect('dice.db')
    c = conn.cursor()
    c.execute("SELECT gameID, value FROM rollHistory")
    rolls = []
    for row in c.fetchall():
        if row[0] == gameKey:
            rolls.append(row[1]) # append each roll value to list
    
    font1 = {'size': 12}

    n = 12
    bins = np.arange(2, n+2, 1)

    fig, ax = plt.subplots()

    arr = ax.hist(rolls, ec='white', bins = bins, align='left')
    
    plt.xticks(bins[:-1]) #set x-axis ticks
    ax.grid(False) #remove grid lines

    labels = [arr[0][i] for i in range(len(arr[0]))] #calculate labels in plot point variable "arr"
    points = ax.patches #don't know what this is
    for bar, count in zip(points, labels): #this is to calculate where to place the labels
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.01,
            int(count),
            )

    plt.title("Frequency of Dice Rolls", fontdict = font1)
    plt.xlabel("Roll Values", fontdict = font1)
    plt.ylabel("Frequency", fontdict = font1)
    
    plt.show()

    c.close()
    conn.close()