#! python2
# "Maze_Game" By: Trung

# ----------------------------------------------------------------------------------------------------------------------
#                            Import Modules, Create Initial Canvas, and Begin Initial Code
# ----------------------------------------------------------------------------------------------------------------------

from Tkinter import *
# import os
# import time
# import webbrowser
# import math
import random
# import pickle
# import anydbm
import background_premade_code


class ANSI:
    RED = '\033[91m'
    END = '\033[0m'

master = Tk()
master.title("Maze game")
canvas_maze = Canvas(master, width=1080, height=720)

# Image of pixel
black_square = u'\u25fc'
white_square = u'\u25fb'
triangle = u'\u25b2'

# Maze dimension
maze_w = 80  # 100
maze_h = 35  # 40
maze_list = list()

# 15 is the coefficient for height
# 10 is the coefficient for width
one_third_height = maze_h * 15 / 3
two_third_height = one_third_height * 2
one_third_width = maze_w * 10 / 3
two_third_width = one_third_width * 2

# First position
current_position = maze_w * (maze_h - 1) + maze_w / 2 + maze_h - 1

# Position to make pathway
current_pix = maze_w * (maze_h - 1) + maze_w / 2 + maze_h - 1

# debugging time
debug_time = 1
global amount_of_pathways
amount_of_pathways = 8  # out of 20

# Reach destination
global reach_destination
reach_destination = 0

# Last direction
last_dir = ""

# Reach Last line
reach_last_line = 0


# ----------------------------------------------------------------------------------------------------------------------
#                                           Create commands
# ----------------------------------------------------------------------------------------------------------------------

def make_randome_maze():  # make random maze
    for y in range(0, maze_h):
        # print "\n"
        for x in range(0, maze_w):
            # Maze matrix
            # print "%03d" % (y * (maze_w + 1) + x),
            random_wall = random.randint(0, 20)
            # Start and End game position
            if (y <= 1 or y >= maze_h - 2) and x == maze_w / 2:
                maze_list.append(white_square)
            # First and Last line and 2 sides
            elif (y == 0) or (y == maze_h - 1) or x == 0 or x == maze_w - 1:
                maze_list.append(black_square)
            # Random
            elif random_wall < amount_of_pathways:
                maze_list.append(white_square)
            else:
                maze_list.append(black_square)
        maze_list.append("\n")

def loop_random_path():
    global reach_last_line
    global reach_destination
    if reach_last_line != 1:
        make_random_path()
    elif reach_destination != 1:
        make_final_path()
    else:
        maze_ready()
        return

    print_maze()
    master.after(debug_time, loop_random_path)

def make_final_path(): # Make path at the final row (top row)
    global current_pix
    global reach_destination

    # Finish pixel = maze_w - maze_w/2 + row(0)
    # Finish pixel at last line = 2* maze_w - maze/2 + row(1)
    destination = maze_w * 3 / 2 + 1

    # Compare Pixel with destination
    if current_pix < destination:
        next_pix = current_pix + 1
    elif current_pix > destination:
        next_pix = current_pix - 1
    else:
        next_pix = current_pix - maze_w - 1
        reach_destination = 1

    # Change Pixel appearance
    current_pix = next_pix
    maze_list[current_pix] = white_square


def make_random_path():  # Make random path to the final line
    global current_pix
    global reach_last_line
    global last_dir

    # Make random direction
    direction = random.randint(1, 5)
    if direction == 3:  # UP
        current_dir = "U"
        next_pix = current_pix - maze_w - 1
    elif direction < 3:  # LEFT
        current_dir = "L"
        next_pix = current_pix - 1
    elif direction > 3:  # RIGHT
        current_dir = "R"
        next_pix = current_pix + 1

    # If it has the opposite direction as before => return
    if (current_dir == "L" and last_dir == "R") or (current_dir == "R" and last_dir == "L"):
        return
    last_dir = current_dir

    # If hit boundaries => return
    for i in range(0, maze_h):
        if (next_pix == (maze_w + 1) * i) or (next_pix == (maze_w + 1) * (i + 1) - 2) or (0 <= next_pix < maze_w) or (
                            (maze_w + 1) * (maze_h - 1) <= next_pix < (maze_w + 1) * maze_h - 1):
            return

    # Final Line
    if (maze_w + 1) <= current_pix < (maze_w + 1) * 2 - 1:
        reach_last_line = 1

    # Change Pixel appearance
    current_pix = next_pix
    maze_list[current_pix] = white_square

    # Position of current and next Pixel
    # print current_direction, next_pix, current_pix


def print_maze():  # Print maze to the screen
    maze_button.config(state=DISABLED)
    maze_string = ""
    for i in maze_list:
        maze_string = maze_string + i
    wall_widget = Label(master, text=maze_string, bg="black", fg="white")
    wall_widget.grid(row=0)


def click(event):
    x = event.x
    y = event.y

    global one_third_height
    global two_third_height
    global one_third_width
    global two_third_width
    direction = "NONE"
    # Click box
    if one_third_width < x < two_third_width and y < one_third_height:
        direction = "UP"
    elif one_third_width < x < two_third_width and two_third_height < y < maze_h * 15:
        direction = "DOWN"
    elif one_third_height < y < two_third_height and x < one_third_width:
        direction = "LEFT"
    elif one_third_height < y < two_third_height and x > two_third_width:
        direction = "RIGHT"
    move(direction)
    # Message
    # instruction_label.config(text="Mouse location: x=%d, y=%d. Mess:%s" % (x, y, direction))


def move(direction):
    global current_position
    if direction == "UP":
        next_position = current_position - maze_w - 1
    elif direction == "DOWN":
        next_position = current_position + maze_w + 1
    elif direction == "LEFT":
        next_position = current_position - 1
    elif direction == "RIGHT":
        next_position = current_position + 1

    # Change last position to normal (not triangle)
    maze_list[current_position] = white_square

    # Out of range error
    try:
        if maze_list[next_position] == white_square:
            current_position = next_position
    except UnboundLocalError:
        current_position = current_position

    # Display current position
    display_current_postition(current_position)
    print_maze()

    # Check if player reach destination or not
    if current_position == maze_w / 2:
        you_win()


def display_current_postition(n):  # Display current position with triangle
    if maze_list[n] == triangle:
        maze_list[n] = white_square
    else:
        maze_list[n] = triangle


def maze_ready():  # Maze ready to show to the player
    master.bind("<Button-1>", click)
    display_current_postition(current_position)
    maze_button.config(text="Maze generated. Click to see", state=NORMAL)


def you_win():  # Winning condition
    instruction_label.config(text="YOU WIN", font="Arial 32")
    master.unbind("<Button-1>")

    # Change stat
    background_premade_code.write_value_to_pos("W", 1)

    # Exit button
    Button(master, text="Go back", font="Arial 15", command=exit).grid()


def mouse_cursor():  # Change mouse cursor
    # Absolute coordinate of the pointer on monitor screen
    coord_absolute = master.winfo_pointerxy()

    # Coordinate of the GUI origin (point 0,0 of the canvas) on monitor screen
    x_coord_gui = master.winfo_rootx()
    y_coord_gui = master.winfo_rooty()

    # Coordinate of pointer on GUI
    x = coord_absolute[0] - x_coord_gui
    y = coord_absolute[1] - y_coord_gui

    # Initialize value
    global one_third_height
    global two_third_height
    global one_third_width
    global two_third_width

    # Set cursor
    if one_third_width < x < two_third_width and y < one_third_height:  # UP
        master.config(cursor="sb_up_arrow")
    elif one_third_width < x < two_third_width and two_third_height < y < maze_h * 15:  # DOWN
        master.config(cursor="sb_down_arrow")
    elif one_third_height < y < two_third_height and x < one_third_width:  # LEFT
        master.config(cursor="sb_left_arrow")
    elif one_third_height < y < two_third_height and x > two_third_width:  # RIGHT
        master.config(cursor="sb_right_arrow")
    else:
        master.config(cursor="left_ptr")

    # Loop
    master.after(5, mouse_cursor)

# ----------------------------------------------------------------------------------------------------------------------
#                                           Add widgets to GUI
# ----------------------------------------------------------------------------------------------------------------------


how_to_play_text = "How to play:\n" \
                   "You are in a maze. Your position is displayed by a TRIANGLE\n" \
                   "that appears at the bottom center of the screen.\n" \
                   "When you hover over a certain section of the screen\n" \
                   "your cursor will indicate that you can click there.\n" \
                   "The left side of the screen moves your triangle to the left,\n" \
                   "right side to the right, top moves the triangle upward, and the bottom downward.\n" \
                   "The goal is to get your triangle to the gap in the top center of the maze.\n"
instruction_label = Label(master, text=how_to_play_text, font="Arial 12 bold")
instruction_label.grid(row=1)

maze_button = Button(master, text="Generating Maze", font="Arial 12", command=print_maze, state=DISABLED)
maze_button.grid(column=0, row=2)

make_randome_maze()

loop_random_path()

mouse_cursor()

master.mainloop()
