# "The_Closet" By: D.T. Kelly

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
# import background_premade_code


class ANSI:
    RED = '\033[91m'
    END = '\033[0m'


canvas_width = 1080
canvas_height = 720

main_canvas = Tk()  # Creates root window for the GUI
main_canvas.title("Locked and Loaded")  # Puts a title on the root window
bomb_in_closet = Canvas(main_canvas, width=canvas_width, height=canvas_height, bg="darkseagreen")
# ^ Alters the size of the canvas (by pixels), and adds a background (bg) color to the canvas ^

main_canvas_image = PhotoImage(
    file="images/bomb_game_images/obg_1080x720.gif")  # Adds image to the canvas, includes file path
return_image = PhotoImage(file="images/light_bulb_images/return_arrow.gif")

bomb_in_closet.create_image(0, 0, image=main_canvas_image, anchor=NW)  # Defines where the image is anchored
bomb_in_closet.create_image(100, 650, image=return_image)


# ----------------------------------------------------------------------------------------------------------------------
#                                           Create commands
# ----------------------------------------------------------------------------------------------------------------------

def select_bomb_display(event):
    x1, y1 = event.x, event.y
    # ^ Gets mouse click coordinates. (0,0) is the top left corner of the map ^
    if (332 <= x1 <= 659) and (237 <= y1 <= 501):  # Defines what should happen when you click in a certain area
        message = "You have selected the bomb game."
        main_canvas.destroy()
        os.system("game_bomb.py")  # Opens the file in parenthesis, "os module" must be imported to use os.system
        exit()  # Closes the current window after the recently opened file is closed
    elif 12 < x1 < 188 and 614 < y1 < 686:
        exit()

    else:
        message = "Nothing interesting happened."  # Changes the message variable to clarify where you are clicking

    top_label.configure(text=message)  # Updates the text on the top label describing where you clicked


# Setting Mouse cursor for several buttons
def mouse_coordinate():
    # Absolute coordinate of the pointer on monitor screen
    coord_absolute = main_canvas.winfo_pointerxy()

    # Coordinate of the GUI (point 0,0 of the canvas) on monitor screen
    x_coord_gui = main_canvas.winfo_rootx()
    y_coord_gui = main_canvas.winfo_rooty()

    # Coordinate of pointer on GUI
    x1 = coord_absolute[0] - x_coord_gui
    y1 = coord_absolute[1] - y_coord_gui - 20
    # Setting the cursor
    if (332 <= x1 <= 659) and (237 <= y1 <= 501) or (12 < x1 < 188 and 614 < y1 < 686):
        main_canvas.config(cursor="hand2")

    else:
        main_canvas.config(cursor="left_ptr")

    # Loop
    main_canvas.after(5, mouse_coordinate)

# ----------------------------------------------------------------------------------------------------------------------
#                                               Add widgets to GUI
# ----------------------------------------------------------------------------------------------------------------------


top_label = Label(main_canvas, text="The resolution of this window is 1080w x 720h, "
                                    "thus this game is best played in windowed mode.", bg="orange4")
top_label.grid(row=0, column=0, columnspan=108, sticky="EW")
# ^ Creates a label and defines in what canvas it should appear, what text should be in it, what color it is, and ^
# ^^ where in the grid it should appear, the 'sticky="EW"' defines on what side of a grid cell a widget should appear ^^


bomb_in_closet.grid(row=1, column=0, rowspan=72, columnspan=108)
# ^ Defines where the image: bomb_in_closet is in the newly formed grid ^
bomb_in_closet.bind("<Button-1>", select_bomb_display)
# ^ Turns the entire bomb_in_closet image into a button ^
# ^^ then narrows the selection by activating the select_bomb_display command when you click in the right area ^^
mouse_coordinate()

mainloop()
