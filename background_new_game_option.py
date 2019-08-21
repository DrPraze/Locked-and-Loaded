# "New_Game" By: Trung

# ----------------------------------------------------------------------------------------------------------------------
#                            Import Modules, Create Initial Canvas, and Begin Initial Code
# ----------------------------------------------------------------------------------------------------------------------

from Tkinter import *
# import os
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

# Main code
master = Tk()
master.title("New Player")


# ----------------------------------------------------------------------------------------------------------------------
#                                           Create commands
# ----------------------------------------------------------------------------------------------------------------------

# Set current player name
# position: 0:Time,1:Maze,2:Bulb,3:Bomb,4:Picture,5:Riddle,6:FinalDoor
def player_name():
    global player
    player = str(name_widget.get())
    if player == "":
        return
    player_data = pickle.load(open("data/player_database.p", "rb"))
    player_data.update({player: [0, "N", "N", "N", "N", "N", "N"]})
    pickle.dump(player_data, open("data/player_database.p", "wb"))
    db = anydbm.open("data/current_player.db", "c")
    db["name"] = player
    db.close()
    exit()


# List existed names
def load_message():
    mess = "\n(Please choose a different name than appears" \
           " on this list or that player's data will be overwritten with your own.)\n \nExisting players: "
    player_data = pickle.load(open("data/player_database.p", "rb"))
    for player in player_data:
        mess = mess + "\n-" + player
    mess_widget.config(text=mess)

# ----------------------------------------------------------------------------------------------------------------------
#                                           Add widgets to GUI
# ----------------------------------------------------------------------------------------------------------------------


Label(master, text="New player:", font="Arial 15").grid(row=0, column=0)
mess_widget = Label(master, text="Mess", justify=LEFT, font="Arial 15")
mess_widget.grid(row=1, column=0, columnspan=3)

name_widget = Entry(master, justify=CENTER)
name_widget.grid(row=0, column=1)

enter_button = Button(master, text="Ok", font="Arial 15", command=player_name)
enter_button.grid(row=2, column=0)

Button(master, text="Cancel", font="Arial 15", command=exit).grid(row=2, column=1)

load_message()

master.mainloop()
