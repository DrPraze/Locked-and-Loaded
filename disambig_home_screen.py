# "Home_Screen" By: Trung

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
import anydbm
import background_premade_code


class ANSI:
    RED = '\033[91m'
    END = '\033[0m'

master_homescreen = Tk()
master_homescreen.title("Home Screen")
canvas_homescreen = Canvas(master_homescreen, width=1080, height=720)

background_image_homescreen = PhotoImage(file="images/background_image\lalss_1080x7203.gif")


# ----------------------------------------------------------------------------------------------------------------------
#                                           Create commands
# ----------------------------------------------------------------------------------------------------------------------

def click(event):
    x = event.x
    y = event.y
    mess = "Nothing"

    # Setting the box of buttons
    if 252 < x < 476 and 421 < y < 455:
        os.system("background_new_game_option.py")
    elif 254 < x < 469 and 465 < y < 494:
        os.system('background_load_game_option.py')
        db = anydbm.open("data/current_player.db", "c")
        if db["choice"] == "Y":
            master_homescreen.destroy()
            os.system("disambig_main_room.py")
            exit()
    elif 250 < x < 478 and 506 < y < 538:
        instruction()
    elif 240 < x < 487 and 551 < y < 580:
        os.system("disambig_leaderboard.py")
    elif 324 < x < 400 and 597 < y < 625:
        print ANSI.RED + "Thanks for playing!" + ANSI.END
        exit()


def instruction():
    master_homescreen2 = Tk()
    master_homescreen2.title('How to play "Locked and Loaded"')
    mess = "\n" \
           "You are locked in a room.\n" \
           "There is only one way to escape which is through a combination locked door.\n" \
           "Search around the room with your cursor to find minigames to play.\n" \
           "Some of the minigames can be deadly so try your best to win every one.\n" \
           "For each minigame you win you will receive a hint for one of the numbers to the combination.\n" \
           "Be careful though, the hints provided can be tricky to decipher as well.\n" \
           "Follow the instructions CAREFULLY to get out of the room in under 30 minutes.\n" \
           "The sooner you get out, the higher your final score will be." \
           "\n"

    Label(master_homescreen2, text=mess, font="Arial 15").grid()


def change_mouse_cursor():
    # Absolute coordinate of the pointer on monitor screen
    coord_absolute = master_homescreen.winfo_pointerxy()

    # Coordinate of the GUI origin (point 0,0 of the canvas) on monitor screen
    x_coord_gui = master_homescreen.winfo_rootx()
    y_coord_gui = master_homescreen.winfo_rooty()

    # Coordinate of pointer on GUI
    x = coord_absolute[0] - x_coord_gui
    y = coord_absolute[1] - y_coord_gui

    # Setting the cursor
    if (252 < x < 476 and 421 < y < 455) or (254 < x < 469 and 465 < y < 494) or (250 < x < 478 and 506 < y < 538) or (
                        240 < x < 487 and 551 < y < 580) or (324 < x < 400 and 597 < y < 625):
        master_homescreen.config(cursor="hand2")
    else:
        master_homescreen.config(cursor="left_ptr")

    # Loop
    master_homescreen.after(5, change_mouse_cursor)

# ----------------------------------------------------------------------------------------------------------------------
#                                           Add widgets to GUI
# ----------------------------------------------------------------------------------------------------------------------


master_homescreen.bind("<Button-1>", click)
canvas_homescreen.grid(column=0, row=0)
canvas_homescreen.create_image(0, 0, image=background_image_homescreen, anchor=NW)

# debug_lable = Label(master_homescreen, text="Last Player:" + Premade_code.name(), font="Arial 15")
# debug_lable.grid(column=0, row=1)

change_mouse_cursor()

master_homescreen.mainloop()
