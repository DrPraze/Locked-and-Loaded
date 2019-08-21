# "Main_Room" By: D.T. Kelly

# ----------------------------------------------------------------------------------------------------------------------
#                            Import Modules, Create Initial Canvas, and Begin Initial Code
# ----------------------------------------------------------------------------------------------------------------------

from Tkinter import *
import os
import time
# import webbrowser
# import math
# import random
# import pickle
# import anydbm
import background_premade_code


class ANSI:
    RED = '\033[91m'
    END = '\033[0m'

canvas_width = 1080
canvas_height = 720
main_canvas = Tk()
main_canvas.title("Locked and Loaded")
main_room = Canvas(main_canvas, width=canvas_width, height=canvas_height, bg="darkseagreen")

background_image = PhotoImage(file="images/main_room_images/mrns_1080x720.gif")
clock_image = PhotoImage(file="images/main_room_images/clock.gif")
return_image = PhotoImage(file="images/light_bulb_images/return_arrow.gif")

main_room.create_image(0, 0, image=background_image, anchor=NW)
main_room.create_image(665, 70, image=clock_image, anchor=CENTER)
main_room.create_image(530, 680, image=return_image)

# Initial Time
t0 = time.clock()

# Get the name of the current player
current_player_name = background_premade_code.name()
print current_player_name, "is playing"

# position: 0:Time, 1:Maze, 2:Bulb, 3:Bomb, 4:Picture, 5:Riddle, 6:FinalDoor


# ----------------------------------------------------------------------------------------------------------------------
#                                           Create commands
# ----------------------------------------------------------------------------------------------------------------------

def select_game(event):
    check_time()
    position, game_name = 0, "Nothing"

    x1, x2, x3, y1, y2, y3 = event.x, event.x, event.x, event.y, event.y, event.y
    # Get mouse click coordinates. (0,0) is the top left corner of the map. ^
    if (79 <= x1 <= 212) and (40 <= y1 <= 618):
        position, game_name = 1, "Maze Game"
        os.system("game_maze.py")

    elif (309 <= x1 <= 492) and (95 <= y1 <= 483):
        position, game_name = 6, "Final Door"
        os.system("game_final_door.py")

    elif (609 <= x1 <= 718) and (144 <= y1 <= 273):
        position, game_name = 4, "Spot the Difference Game"
        os.system("game_spot_the_difference.py")

    elif (715 <= x1 <= 805) and (316 <= y1 <= 365):
        position, game_name = 2, "Bulbs Game"
        os.system("game_light_bulb.py")

    elif (520 <= x1 <= 600 and 376 <= y1 <= 496) or (736 <= x1 <= 817 and 376 <= y1 <= 496):
        position, game_name = 5, "Riddle Game"
        os.system("game_riddle.py")

    elif (861 <= x1 <= 1003) and (86 <= y1 <= 636):
        position, game_name = 3, "Bomb Game"  # The Closet
        os.system("disambig_the_closet.py")

    elif (620 <= x1 <= 710) and (18 <= y1 <= 108):
        time_left()
    elif (440 <= x1 <= 620) and (640 <= y1 <= 712):
        save_and_get_back()

    time.sleep(.1)
    if background_premade_code.value_at(6) == "W":
        you_win()
    elif (background_premade_code.value_at(6) or background_premade_code.value_at(3)) == "L":
        you_lose()

    if background_premade_code.value_at(position) == "W":
        print current_player_name, str(background_premade_code.value_at(position)) + "on the", game_name

    # Update debugging screen
    if game_name == "Nothing":
        return
    message = "You just played the %s." % game_name
    info_label.configure(text=message)


def change_mouse_cursor():
    # Absolute coordinate of the pointer on monitor screen
    coord_absolute = main_canvas.winfo_pointerxy()

    # Coordinate of the GUI (point 0,0 of the canvas) on monitor screen
    x_coord_gui = main_canvas.winfo_rootx()
    y_coord_gui = main_canvas.winfo_rooty()

    # Coordinate of pointer on GUI
    x1 = coord_absolute[0] - x_coord_gui
    y1 = coord_absolute[1] - y_coord_gui - 35
    # Setting the cursor
    if (79 <= x1 <= 212 and 40 <= y1 <= 618) or \
            (309 <= x1 <= 492 and 95 <= y1 <= 483) or \
            (609 <= x1 <= 718 and 144 <= y1 <= 273) or \
            (715 <= x1 <= 805) and (316 <= y1 <= 365) or \
            (520 <= x1 <= 600) and (376 <= y1 <= 496) or \
            (736 <= x1 <= 817) and (376 <= y1 <= 496) or \
            (620 <= x1 <= 710) and (18 <= y1 <= 108) or \
            (861 <= x1 <= 1003) and (86 <= y1 <= 636) or \
            (440 <= x1 <= 620) and (640 <= y1 <= 712):
        main_canvas.config(cursor="hand2")

    else:
        main_canvas.config(cursor="left_ptr")

    # Loop
    main_canvas.after(5, change_mouse_cursor)


def time_left():
    master_time_left = Tk()
    master_time_left.title("Time left")
    Label(
        master_time_left, text="You have %.2d:%.2d left" % background_premade_code.time_left(),
        font="Arial 30", fg="Red").grid()
    Button(master_time_left, text="OK", font="Arial 15", command=master_time_left.destroy).grid()


def check_time():  # if time > 1800s then you_lose
    global t0
    # Save time to database
    background_premade_code.add_time_to_database(time.clock() - t0)
    # Reset counter
    t0 = time.clock()
    if background_premade_code.value_at(0) < 1800:
        return
    else:
        you_lose()


def you_win():
    main_canvas.destroy()
    background_premade_code.add_time_to_database(time.clock() - t0)
    os.system("background_win_game.py")
    exit()


def you_lose():
    main_canvas.destroy()
    os.system("background_lose_game.py")
    exit()


def save_and_get_back():
        # Save time
        background_premade_code.add_time_to_database(time.clock() - t0)
        print "Player %s" % current_player_name, "has %.2d:%.2d left" % background_premade_code.time_left()
        main_canvas.destroy()
        os.system("disambig_home_screen.py")
        exit()

# ----------------------------------------------------------------------------------------------------------------------
#                                           Add widgets to GUI
# ----------------------------------------------------------------------------------------------------------------------


main_room.bind("<Button-1>", select_game)
main_room.grid(row=1, column=0, rowspan=72, columnspan=108)

info_label = Label(
    main_canvas, text="The resolution of this window is 1080w x 720, "
                      "thus this game is best played in windowed mode.", font="Arial 15")

info_label.grid(row=0, column=0, columnspan=108, sticky="EW")

# Debugging auto win button
# win_button = Button(main_canvas, text="Auto Win", command=you_win)
# win_button.grid(row=72, column=105)

change_mouse_cursor()

main_canvas.mainloop()
