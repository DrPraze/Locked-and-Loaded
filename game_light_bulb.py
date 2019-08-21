# "Light_Bulb_Game" By: Trung

# ----------------------------------------------------------------------------------------------------------------------
#                            Import Modules, Create Initial Canvas, and Begin Initial Code
# ----------------------------------------------------------------------------------------------------------------------

from Tkinter import *
# import os
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

master_bulb_game = Tk()
master_bulb_game.title("Light Bulb Minigame")
canvas_lightbulb = Canvas(master_bulb_game, width=1080, height=700)

# Image of bulbs
image_light_on = PhotoImage(file="images/light_bulb_images/Lightbulb_On.gif")
image_light_off = PhotoImage(file="images/light_bulb_images/Lightbulb_Off.gif")
image_button_off = PhotoImage(file="images/light_bulb_images/Button Off.gif")
image_button_on = PhotoImage(file="images/light_bulb_images/Button On.gif")
return_image = PhotoImage(file="images/light_bulb_images/return_arrow.gif")
background_image_bulb_game = PhotoImage(file="images/light_bulb_images/isg_offstate.gif")

# Condition of bulbs
bulb_state = {1: "OFF", 2: "OFF", 3: "OFF", 4: "OFF", 5: "OFF", 6: "OFF"}

# Relation between bulbs and buttons
bulb_button_assignment = {1: (1, 3), 2: (3, 4), 3: (1, 4, 5), 4: (5, 6), 5: (2, 4, 6)}

button_state = {1: "OFF", 2: "OFF", 3: "OFF", 4: "OFF"}

global button_x
global button_y
button_y = 500
button_x = 180
global button_resolution_width
global button_resolution_height
button_resolution_width = 100
button_resolution_height = 80

winning_condition = 0


# ----------------------------------------------------------------------------------------------------------------------
#                                           Create commands
# ----------------------------------------------------------------------------------------------------------------------

def reset_bulbgame():
    # Turn off all bulbs
    for bulb in range(1, 7):
        canvas_lightbulb.create_image(85 + 130 * bulb, 315, image=image_light_off, anchor=CENTER)
        bulb_state[bulb] = "OFF"
    # Turn off all buttons
    for button in range(1, 6):
        canvas_lightbulb.create_image(button_x * button, button_y, image=image_button_on, anchor=CENTER)
        canvas_lightbulb.create_image(button_x * button, button_y, image=image_button_off, anchor=CENTER)
        button_state[button] = "OFF"
    canvas_lightbulb.create_image(100, 650, image=return_image, anchor=CENTER)


def click(event):
    # Calculate the position for button image
    assign_x_left = button_x - button_resolution_width / 2
    assign_x_right = assign_x_left + button_resolution_width
    assign_y_up = button_y - button_resolution_height / 2
    assign_y_down = assign_y_up + button_resolution_height

    x = event.x
    y = event.y
    index = 0
    if winning_condition == 0:
        if assign_x_left < x < assign_x_right and assign_y_up < y < assign_y_down:
            index = 1
        elif (assign_x_left + button_x) < x < (assign_x_right + button_x) and assign_y_up < y < assign_y_down:
            index = 2
        elif (assign_x_left + button_x * 2) < x < (assign_x_right + button_x * 2) and assign_y_up < y < assign_y_down:
            index = 3
        elif (assign_x_left + button_x * 3) < x < (assign_x_right + button_x * 3) and assign_y_up < y < assign_y_down:
            index = 4
        elif (assign_x_left + button_x * 4) < x < (assign_x_right + button_x * 4) and assign_y_up < y < assign_y_down:
            index = 5
    if 12 < x < 188 and 614 < y < 686:
        exit()
    if index != 0:
        change_buttons(index)
        change_bulbs(index)

    # Debugging
    # message_widget_bulb_game.config(text="Mouse location: x=%d, y=%d, message= %s" % (x, y, str(index)))
    bulb_checking_bulbgame()


# Change bulb image
def change_bulbs(button_name):
    for bulb in bulb_button_assignment[button_name]:
        # Change the state of bulbs
        if bulb_state[bulb] == "OFF":
            canvas_lightbulb.create_image(85 + 130 * bulb, 315, image=image_light_on, anchor=CENTER)
            bulb_state[bulb] = "ON"
        else:
            canvas_lightbulb.create_image(85 + 130 * bulb, 315, image=image_light_off, anchor=CENTER)
            bulb_state[bulb] = "OFF"


# Change Button image
def change_buttons(index):
    if button_state[index] == "OFF":
        canvas_lightbulb.create_image(button_x * index, button_y, image=image_button_on, anchor=CENTER)
        button_state[index] = "ON"
    else:
        canvas_lightbulb.create_image(button_x * index, button_y, image=image_button_off, anchor=CENTER)
        button_state[index] = "OFF"


# Check if all bulbs are on or not
def bulb_checking_bulbgame():
    count_on_bulb = 0
    for bulb in range(1, 7):
        if bulb_state[bulb] == "ON":
            count_on_bulb += 1
    if count_on_bulb == 6:
        you_win_bulbgame()


# Winning condition
def you_win_bulbgame():
    global winning_condition
    winning_condition = 1
    message_widget_bulb_game.config(text="WIN")

    # Change stat
    background_premade_code.write_value_to_pos("W", 2)


# Change mouse Cursor
def change_mouse_cursor():
    # Absolute coordinate of the pointer with reference to the monitor screen (returns a tuple of x and y)
    coord_absolute = master_bulb_game.winfo_pointerxy()

    # Coordinate of the GUI origin (point 0,0 of the canvas) with reference to the monitor screen
    x_coord_gui = master_bulb_game.winfo_rootx()
    y_coord_gui = master_bulb_game.winfo_rooty()

    # Coordinate of pointer with reference to GUI origin
    x = coord_absolute[0] - x_coord_gui
    y = coord_absolute[1] - y_coord_gui

    # Find the bound of the button horizontally
    assign_x_left = button_x - button_resolution_width / 2
    assign_x_right = assign_x_left + button_resolution_width

    # Find the bound of the button vertically
    assign_y_up = button_y - button_resolution_height / 2 + 35
    assign_y_down = assign_y_up + button_resolution_height

    # Setting the cursor
    if (assign_x_left < x < assign_x_right or (assign_x_left + button_x) < x < (assign_x_right + button_x) or (
                assign_x_left + button_x * 2) < x < (assign_x_right + button_x * 2) or (
                assign_x_left + button_x * 3) < x < (assign_x_right + button_x * 3) or (
                assign_x_left + button_x * 4) < x < (
                assign_x_right + button_x * 4)) and (assign_y_up < y < assign_y_down) or (
                        12 < x < 188 and 614 < y - 35 < 686):
        master_bulb_game.config(cursor="hand2")
    else:
        master_bulb_game.config(cursor="left_ptr")

    # Loop
    master_bulb_game.after(5, change_mouse_cursor)

# ----------------------------------------------------------------------------------------------------------------------
#                                           Add widgets to GUI
# ----------------------------------------------------------------------------------------------------------------------

# Bind mouse
master_bulb_game.bind("<Button-1>", click)

message_widget_bulb_game = Label(master_bulb_game, text="TURN ON ALL THE BULBS", font="Arial 20")
message_widget_bulb_game.grid(row=0, column=0, columnspan=5)

# Canvas
canvas_lightbulb.grid(row=1, column=0, columnspan=5)
canvas_lightbulb.create_image(0, 0, image=background_image_bulb_game, anchor=NW)

# Buttons
# reset_button = Button(master_bulb_game, text="Reset", command=reset_bulbgame)
# reset_button.grid(row=4, column=0)

reset_bulbgame()

change_mouse_cursor()

master_bulb_game.mainloop()
