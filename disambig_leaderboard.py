# "Leaderboard" By: Trung

# ----------------------------------------------------------------------------------------------------------------------
#                            Import Modules, Create Initial Canvas, and Begin Initial Code
# ----------------------------------------------------------------------------------------------------------------------

from Tkinter import *
# import os
# import time
# import webbrowser
# import math
import random
import pickle
import anydbm
import background_premade_code


class ANSI:
    RED = '\033[91m'
    END = '\033[0m'

master = Tk()
master.title("Leaderboard")

# Get the name of the current player
db = anydbm.open("data/current_player.db", "c")
current_player_name = db["name"]
db.close()

# Database
leaderboard_score = pickle.load(open("data/leaderboard.p", 'rb'))
player_data = pickle.load(open("data/player_database.p", "rb"))


# ----------------------------------------------------------------------------------------------------------------------
#                                           Create commands
# ----------------------------------------------------------------------------------------------------------------------

def print_leaderboard():
    score_list = list()
    for player in leaderboard_score:
        score_list = score_list + [(leaderboard_score[player], player)]
    score_list.sort(reverse=True)

    # Format GUI
    Label(master, text="Pos:", font="Arial 15 bold").grid(row=1, column=0)
    Label(master, text="Name:", font="Arial 15 bold").grid(row=1, column=1)
    Label(master, text="Score:", font="Arial 15 bold").grid(row=1, column=2)

    # Print score to GUI
    row = 1
    for score in score_list:
        row += 1
        if score[1] == current_player_name:
            color = "Red"
        else:
            color = "Black"
        Label(master, text=str(row - 1), font="Arial 15", fg=color).grid(row=row, column=0)
        Label(master, text=score[1], font="Arial 15", fg=color).grid(row=row, column=1)
        Label(master, text=str(score[0]), font="Arial 15", fg=color).grid(row=row, column=2)
        if row > 10:
            break

# ----------------------------------------------------------------------------------------------------------------------
#                                           Add widgets to GUI
# ----------------------------------------------------------------------------------------------------------------------


Label(master, text="Leaderboard:", font="Arial 15 bold").grid(columnspan=3)

# make_score()
print_leaderboard()
Button(master, text="Exit", font="Arial 15", command=exit).grid(columnspan=3)

master.mainloop()
