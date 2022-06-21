# "Spot_the_Difference_Game" By: Matt

# ----------------------------------------------------------------------------------------------------------------------
#                            Import Modules, Create Initial Canvas, and Begin Initial Code
# ----------------------------------------------------------------------------------------------------------------------

from tkinter import *
# import os
# import time
# import webbrowser
import math
import random
# import pickle
# import anydbm
import background_premade_code


class ANSI:
    RED = '\033[91m'
    END = '\033[0m'

canvas_width = 417
canvas_height = 700
main_canvas = Tk()
main_canvas.title("Spot The Difference")
spot_the_difference = Canvas(main_canvas, width=canvas_width, height=canvas_height)

image = PhotoImage(file='images/spot_difference_images/spot_the_difference_image1.gif')
return_image = PhotoImage(file="images/light_bulb_images/return_arrow.gif")

spot_the_difference.create_image(0, 0, image=image, anchor=NW)
imageID = spot_the_difference.create_image(0, 0, image=image, anchor=NW)
spot_the_difference.create_image(100, 650, image=return_image)

image_IDs = []
global differences_found
set_of_differences_found = set()
# print 'The number of differences found so far is:', len(set_of_differences_found)
repeat_clicks = []

radius = 5


# ----------------------------------------------------------------------------------------------------------------------
#                                           Create commands
# ----------------------------------------------------------------------------------------------------------------------

def check_for_difference(event):
    x1, y1 = event.x, event.y
    # print 'Location:', x1,y1
    if 10 < x1 < 190 and 615 < y1 < 685:
        exit()
    if 305 <= y1:
        message = "You can only click on the differences in the top picture!!"
        change_color(info_label, 4)

    elif (220 <= x1 <= 230) and (266 <= y1 <= 280):
        message = "You found the pumpkin's extra nose!"  # 1
        if "extra_nose" in set_of_differences_found:
            repeat_clicks.append("extra_nose")
        set_of_differences_found.add("extra_nose")
        spot_the_difference.create_oval(x1 - radius, y1 - radius, x1 + radius,
                                        y1 + radius, fill='orange', outline='black')
        change_color(info_label, 2)

    elif (235 <= x1 <= 250) and (145 <= y1 <= 165):
        message = "You found the witch's extra leg!"  # 1
        if "extra_leg" in set_of_differences_found:
            repeat_clicks.append("extra_leg")
        set_of_differences_found.add("extra_leg")
        spot_the_difference.create_oval(x1 - radius, y1 - radius, x1 + radius,
                                        y1 + radius, fill='orange', outline='black')
        change_color(info_label, 2)

    elif (345 <= x1 <= 365) and (240 <= y1 <= 260):
        message = "You found an extra bat!"  # 1
        if "extra_bat_bot_right" in set_of_differences_found:
            repeat_clicks.append("extra_bat_bot_right")
        set_of_differences_found.add("extra_bat_bot_right")
        spot_the_difference.create_oval(x1 - radius, y1 - radius, x1 + radius,
                                        y1 + radius, fill='orange', outline='black')
        change_color(info_label, 2)

    elif (105 <= x1 <= 125) and (118 <= y1 <= 140):
        message = "You found an extra bat!"  # 1
        if "extra_bat_top_left" in set_of_differences_found:
            repeat_clicks.append("extra_bat_top_left")
        set_of_differences_found.add("extra_bat_top_left")
        spot_the_difference.create_oval(x1 - radius, y1 - radius, x1 + radius,
                                        y1 + radius, fill='orange', outline='black')
        change_color(info_label, 2)

    elif (70 <= x1 <= 90) and (260 <= y1 <= 290):
        message = "You found an extra grave stone!"  # 1
        if "extra_grave_stone" in set_of_differences_found:
            repeat_clicks.append("extra_grave_stone")
        set_of_differences_found.add("extra_grave_stone")
        spot_the_difference.create_oval(x1 - radius, y1 - radius, x1 + radius,
                                        y1 + radius, fill='orange', outline='black')
        change_color(info_label, 2)

    elif (296 <= x1 <= 310) and (205 <= y1 <= 218):
        message = "You found an extra branch!"  # 1
        if "extra_branch" in set_of_differences_found:
            repeat_clicks.append("extra_branch")
        set_of_differences_found.add("extra_branch")
        spot_the_difference.create_oval(x1 - radius, y1 - radius, x1 + radius,
                                        y1 + radius, fill='orange', outline='black')
        change_color(info_label, 2)

    elif (265 <= x1 <= 280) and (125 <= y1 <= 135):
        message = "You found the difference in the broom stick!"  # 1
        if "broom_stick" in set_of_differences_found:
            repeat_clicks.append("broom_stick")
        set_of_differences_found.add("broom_stick")
        spot_the_difference.create_oval(x1 - radius, y1 - radius, x1 + radius,
                                        y1 + radius, fill='orange', outline='black')
        change_color(info_label, 2)
    else:
        message = "No difference here.  Try again!"
        change_color(info_label, 4)
    # print set_of_differences_found
    # print len(set_of_differences_found)
    display_differences_found_count.delete(0, END)
    display_differences_found_count.insert(0, len(set_of_differences_found))
    info_label.configure(text=message)
    if len(set_of_differences_found) == 7:
        you_win()
    diameter = 20


def you_win():
    message = "Congratulations, you won!"
    display_differences_found_count.delete(0, END)
    display_differences_found_count.insert(0, "YOU WIN!!")
    change_color(display_differences_found_count, 12)
    change_color(info_label, 12)
    change_color(differences_label, 12)
    info_label.configure(text=message)
    differences_label.configure(text="YOU WIN!!")

    # Change stat
    background_premade_code.write_value_to_pos("W", 4)


def change_color(my_widget, n):
    if n == 0:
        return  # Done flashing
    else:
        current_color = my_widget.cget("background")
        next_color = "red" if current_color == "yellow" else "yellow"
        my_widget.config(background=next_color)
        main_canvas.after(250, change_color, my_widget, n - 1)


def change_mouse_cursor():
    # Absolute coordinate of the pointer on monitor screen
    coord_absolute = main_canvas.winfo_pointerxy()

    # Coordinate of the GUI origin (point 0,0 of the canvas) on monitor screen
    x_coord_gui = main_canvas.winfo_rootx()
    y_coord_gui = main_canvas.winfo_rooty()

    # Coordinate of pointer on GUI
    x1 = coord_absolute[0] - x_coord_gui
    y1 = coord_absolute[1] - y_coord_gui - 90

    # Setting the cursor
    if 10 < x1 < 190 and 615 < y1 < 685:
        main_canvas.config(cursor="hand2")
    else:
        main_canvas.config(cursor="left_ptr")

    # Loop
    main_canvas.after(5, change_mouse_cursor)

# ----------------------------------------------------------------------------------------------------------------------
#                                           Add widgets to GUI
# ----------------------------------------------------------------------------------------------------------------------


spot_the_difference.bind("<Button-1>", check_for_difference)
spot_the_difference.grid(row=3, column=0, columnspan=2)

info_label = Label(main_canvas, text="Start looking for differences!", bg="red")
info_label.grid(row=1, column=0, columnspan=2)

differences_label = Label(main_canvas, text="Number of Differences Found", background="orange")
differences_label.grid(row=2, column=0)
display_differences_found_count = Entry(main_canvas, justify=CENTER, width=20, background="orange")
display_differences_found_count.grid(row=2, column=1)
display_differences_found_count.insert(0, len(set_of_differences_found))

instructions = """Welcome to Spot the scary difference!
        Spot these seven spooky differences!
 Click on the differences you find in the TOP picture!"""

Label(main_canvas, text=instructions).grid(row=0, column=0, columnspan=2)

change_mouse_cursor()

main_canvas.mainloop()
