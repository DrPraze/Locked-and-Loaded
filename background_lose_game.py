# "Lose_Game" By: Trung

# ----------------------------------------------------------------------------------------------------------------------
#                            Import Modules, Create Initial Canvas, and Begin Initial Code
# ----------------------------------------------------------------------------------------------------------------------

from Tkinter import *
import os
# import time
# import webbrowser
# import math
# import random
# import pickle
# import anydbm
import background_premade_code


class ANSI:
    RED = '\033[91m'
    END = '\033[0m'

master = Tk()
master.title("You lost...")


# ----------------------------------------------------------------------------------------------------------------------
#                                           Create commands
# ----------------------------------------------------------------------------------------------------------------------

# Calculate_score
def print_player_score():
    mess = "Something went wrong and you\n" \
           "were trapped or suffered serious bodily harm.\nUnfortunately that means you lose!\n" \
           "Your score is "
    player_score = 0
    mess += "%s\n" % (player_score)
    message_label.config(text=mess)

    # Update score in database
    background_premade_code.update_score_to_database(player_score)
    # Delete player profile
    background_premade_code.delete_player_profile()


# Open homescreen
def open_homescreen():
    master.destroy()
    os.system("disambig_home_screen.py")
    exit()

# ----------------------------------------------------------------------------------------------------------------------
#                                           Add widgets to GUI
# ----------------------------------------------------------------------------------------------------------------------


message_label = Label(master, text="Your score is", font="Arial 15 bold", fg="Red")
message_label.grid(columnspan=2)

# Buttons
Button(master, text="Leaderboard", font="Arial 15", command=background_premade_code.open_leaderboard).grid(row=2, column=0)
Button(master, text="Back to homescreen", font="Arial 15", command=open_homescreen).grid(row=2, column=1)

print_player_score()
master.mainloop()
