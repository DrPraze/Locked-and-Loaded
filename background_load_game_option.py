# "Load_Game" By: Trung

# ----------------------------------------------------------------------------------------------------------------------
#                                   Import Modules, and Begin Initial Code
# ----------------------------------------------------------------------------------------------------------------------

from Tkinter import *
import os
# import time
# import webbrowser
# import math
# import random
import pickle
import anydbm
import background_premade_code


class ANSI:
    RED = '\033[91m'
    END = '\033[0m'

# Initial that the player has not clicked OK
player_data = pickle.load(open("data/player_database.p", "rb"))
db = anydbm.open("data/current_player.db", "c")
db["choice"] = "N"


# ----------------------------------------------------------------------------------------------------------------------
#                                               Create commands
# ----------------------------------------------------------------------------------------------------------------------

# Set current player name
def select_player():
    global db
    player = var.get()
    # Save current player name
    db["name"] = player
    # Check if player clicked OK
    db["choice"] = "Y"
    exit()


# Load players'name
def load_option():
    global i
    i = 1
    for player in player_data:
        button = Radiobutton(master, text=player, font="Arial 15", variable=var, value=player)
        button.grid(sticky=W,columnspan=4)
        button.select()
        i += 1


# Open the New player gui
def new_player():
    os.system("background_new_game_option.py")
    master.destroy()
    os.system("background_load_game_option.py")


# Delete a player
def delete_player():
    player = var.get()
    player_data.pop(player, 0)
    pickle.dump(player_data, open("data/player_database.p", "wb"))

    # Restart the window
    master.destroy()
    os.system("background_load_game_option.py")
    exit()


# Set_up GUI
def set_up():
    master.title("Load Game")
    Label(master, text="Choose a profile, from the provided list below, to load: \n"
                       " (If you don't see your name on the list that means you haven't created a 'new player' yet \n"
                       " and must do so before starting the game.)", font="Arial 15").grid(columnspan=10)
    load_option()
    Button(master, text="Load Player Profile", font="Arial 15", command=select_player).grid(row=i, column=0)
    Button(master, text="New Player", font="Arial 15", command=new_player).grid(row=i, column=1)
    Button(master, text="Delete Player", font="Arial 15", command=delete_player).grid(row=i, column=2)
    Button(master, text="Cancel", font="Arial 15", command=exit).grid(row=i, column=6)

master = Tk()

var = StringVar()

set_up()

master.mainloop()
