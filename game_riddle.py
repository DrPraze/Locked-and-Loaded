# "Riddle_Game" By: Kevin

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


main_screen = Tk()
main_screen.title("The Riddler")
game_window = Canvas(main_screen, width=600, height=600, bg="black")
game_window.grid(row=0, columnspan=5)

introduction_screen = PhotoImage(file="images/riddle_game_images/introduction_screen.gif")
riddle_selection_screen = PhotoImage(file="images/riddle_game_images/riddle_selection_screen.gif")

tries_remaining = 3

set_hint = set()
num_hint = []

state_dictionary = {1: 1, 2: 1, 3: 1, 4: 1}

# GENERATES A RANDOM SELECTED RIDDLE
randa = random.randint(1, 4)


# ----------------------------------------------------------------------------------------------------------------------
#                                           Create commands
# ----------------------------------------------------------------------------------------------------------------------

def intro():
    # BUTTONS THAT ARE ENABLED
    start_button.config(state=NORMAL)
    hint_button.configure(state=DISABLED)
    submit_button.configure(state=DISABLED)

    # ENTRIES AND MESSAGES THAT ARE DISABLED
    answer.configure(state=DISABLED)
    message.configure(text=" ")
    tries_remaining_display.configure(state=DISABLED)

    # CREATES IMAGE WITH introduction_screen.gif
    game_window.create_image(300, 300, image=introduction_screen, anchor=CENTER)


def mouse_click():
    # BUTTONS STATES
    start_button.config(text="CONTINUE", state=DISABLED)
    hint_button.configure(state=NORMAL)

    # ENTRIES AND MESSAGES THAT ARE DISABLED
    answer.configure(state=NORMAL)
    tries_remaining_display.configure(state=NORMAL)

    game_window.create_image(300, 300, image=riddle_selection_screen, anchor=CENTER)
    game_window.bind("<Button-1>", go_to_riddle)


def go_to_riddle(event):
    global riddle
    global riddle_answer
    global chosen_riddle

    x1, y1 = event.x, event.y  # Get mouse click coordinates. (0,0) is the top left corner of the map.
    answer.configure(state=NORMAL)
    answer.delete(0, END)
    submit_button.configure(state=NORMAL)

    # FOR DEBUGGING PURPOSES, PRINTS OUT MOUSE CLICK LOCATION:
    # print "Location:", x1, y1

    # CONDITIONS FOR MOUSE CLICK:
    if (0 <= x1 <= 300) and (0 <= y1 <= 300):
        if state_dictionary[1] == 1:
            riddle = "I don't have eyes, but once I did see. " \
                     "Once I had thoughts, but now I'm white and empty. (one word)"
            riddle_answer = "Skull"
            chosen_riddle = 1
        elif (state_dictionary[1] == 0) and (randa != chosen_riddle):
            riddle = "You already answered this riddle. Choose another one."
        else:
            riddle = "You already won the game!"

    if (0 <= x1 <= 300) and (300 <= y1 <= 600):
        if state_dictionary[2] == 1:
            riddle = "The more of me you take, the more you leave behind. (one word)"
            riddle_answer = "Footsteps"
            chosen_riddle = 2
        elif (state_dictionary[2] == 0) and (randa != chosen_riddle):
            riddle = "You already answered this riddle. Choose another one."
        else:
            riddle = "You already won the game!"

    if (300 <= x1 <= 600) and (0 <= y1 <= 300):
        if state_dictionary[3] == 1:
            riddle = "What begins with T, ends with T and has T in it? (one word)"
            riddle_answer = "Teapot"
            chosen_riddle = 3
        elif (state_dictionary[3] == 0) and (randa != chosen_riddle):
            riddle = "You already answered this riddle. Choose another one."
        else:
            riddle = "You already won the game!"

    if (300 <= x1 <= 600) and (300 <= y1 <= 600):
        if state_dictionary[4] == 1:
            riddle = "What has a head, a tail, is brown and has no legs? (one word)"
            riddle_answer = "Penny"
            chosen_riddle = 4
        elif (state_dictionary[4] == 0) and (randa != chosen_riddle):
            riddle = "You already answered this riddle. Choose another one."
        else:
            riddle = "You already won the game!"

    # DISPLAYS THE RIDDLE THE PLAYER SELECTED:
    message.configure(text=riddle)


def check_then_submit():
    global tries_remaining
    global randa
    global chosen_riddle
    global riddle
    global riddle_answer

    answer1 = answer.get()
    num_words = len(answer1.split())
    # print num_words

    if num_words == 1:
        if (answer1 == riddle_answer) or (answer1.lower() == riddle_answer) or (answer1.capitalize() == riddle_answer):
            state_dictionary[chosen_riddle] = 0
            # print "You solved ", chosen_riddle
            if randa == chosen_riddle:
                win()
            else:
                riddle = "Good job. Now answer another riddle."

        elif answer1 == "":
            answer.configure(text="Say Something")

        elif answer != riddle_answer:
            tries_remaining -= 1
            # print tries_remaining
            riddle = "Wrong. -1 try"
            tries_remaining_display.delete(0, END)
            tries_remaining_display.insert(0, tries_remaining)

        if tries_remaining == 0:
            tries_remaining_display.delete(0, END)
            riddle = "You lose the game!"
            lose()

    else:
        riddle = "Please enter a one word response. Try another riddle."

    message.configure(text=riddle)


def hint():
    global riddle
    global tries_remaining

    set_hint.add("1")
    if "1" in set_hint:
        num_hint.append(1)

    if len(num_hint) == 1:
        riddle = "Tricked you! There are no hints here! -1 try."
        tries_remaining -= 1
        tries_remaining_display.delete(0, END)
        tries_remaining_display.insert(0, tries_remaining)

    if len(num_hint) == 2:
        riddle = "Didn't you learn the first time -1 try."
        tries_remaining -= 1
        tries_remaining_display.delete(0, END)
        tries_remaining_display.insert(0, tries_remaining)

    if (len(num_hint) == 3) or (tries_remaining == 0):
        riddle = "I Warned you! -1 try."
        tries_remaining -= 1
        tries_remaining_display.delete(0, END)
        tries_remaining_display.insert(0, tries_remaining)
        lose()

    message.configure(text=riddle)


def win():
    global go_to_riddle
    global riddle
    riddle = "Congratulations. You found the hint."
    message.configure(text=riddle)
    state_dictionary[1] = 0
    state_dictionary[2] = 0
    state_dictionary[3] = 0
    state_dictionary[4] = 0

    # UPDATE BUTTONS STATES
    start_button.destroy()
    hint_button.destroy()
    submit_button.destroy()

    # ENTRIES AND MESSAGES THAT ARE DISABLED
    answer.destroy()
    tries_remaining_display.destroy()
    a.destroy()
    b.destroy()

    # Change stat
    background_premade_code.write_value_to_pos("W", 5)


def lose():
    global riddle

    # BUTTONS STATES
    start_button.config(text="CONTINUE", state=DISABLED)
    hint_button.configure(state=DISABLED)
    submit_button.configure(state=DISABLED)

    game_window.unbind("<Button-1>")
    riddle = "You lose the game!"
    tries_remaining_display.delete(0, END)
    tries_remaining_display.insert(0, "YOU LOSE!!")

    message.configure(text=riddle)


def return_home():
    exit()

# ----------------------------------------------------------------------------------------------------------------------
#                                           Add widgets to GUI
# ----------------------------------------------------------------------------------------------------------------------


message = Label(main_screen, text="Click a box to choose a riddle.", bg="green")
message.grid(row=5, column=0, columnspan=5, sticky="EW")

answer = Entry(main_screen, justify=CENTER, width=20)
answer.grid(row=6, column=1)

a = Label(main_screen, text="What am I?")
a.grid(row=6, column=0)
b = Label(main_screen, text="Tries Remaining:")
b.grid(row=7, column=0)

submit_button = Button(main_screen, text="SUBMIT ANSWER", command=check_then_submit)
submit_button.grid(row=6, column=2)

tries_remaining_display = Entry(main_screen, justify=CENTER, width=20)
tries_remaining_display.grid(row=7, column=1)
tries_remaining_display.insert(0, '3')

hint_button = Button(main_screen, text="HINT", command=hint)
hint_button.grid(row=7, column=2)

main_screen_button = Button(main_screen, text="GO HOME", state=NORMAL, command=return_home)
main_screen_button.grid(row=9, column=2)

start_button = Button(main_screen, text="START", command=mouse_click)
start_button.grid(row=11, column=1)

intro()

main_screen.mainloop()
