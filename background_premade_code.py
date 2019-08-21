# "Premade_Code" By: Trung

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


class ANSI:
    RED = '\033[91m'
    END = '\033[0m'

db = anydbm.open("data/current_player.db", "c")
current_player_name = db["name"]
db.close()


# ----------------------------------------------------------------------------------------------------------------------
#                                               Create commands
# ----------------------------------------------------------------------------------------------------------------------

# Get current player name
def name():
    return current_player_name


# Get value at position
def value_at(pos):
    player_database = pickle.load(open("data/player_database.p", "rb"))
    return player_database[current_player_name][pos]


# Write value to position
def write_value_to_pos(value, pos):
    player_data = pickle.load(open("data/player_database.p", "rb"))
    player_data[current_player_name][pos] = value
    pickle.dump(player_data, open("data/player_database.p", "wb"))


# Add time to database
def add_time_to_database(value):
    player_data = pickle.load(open("data/player_database.p", "rb"))
    player_data[current_player_name][0] += value
    pickle.dump(player_data, open("data/player_database.p", "wb"))


# Calculate time left
def time_left():
    time = 1800 - value_at(0)
    minute, second = divmod(time, 60)
    return int(minute), int(second)


# Overwrite score in database
def update_score_to_database(value):
    leaderboard_score = pickle.load(open("data/leaderboard.p", 'rb'))
    leaderboard_score.update({current_player_name: value})
    pickle.dump(leaderboard_score, open("data/leaderboard.p", "wb"))


# Delete player profile out of database (used when win or lose)
def delete_player_profile():
    player_data = pickle.load(open("data/player_database.p", "rb"))
    player_data.pop(current_player_name, 0)
    pickle.dump(player_data, open("data/player_database.p", "wb"))


# Open leader board
def open_leaderboard():
    os.system("disambig_leaderboard.py")
