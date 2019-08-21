# "Final_Door_Game" By: D.T. Kelly

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


canvas_width = 1080
canvas_height = 720

main_canvas = Tk()
main_canvas.title("Final Door")
padlock_on_door = Canvas(main_canvas, width=canvas_width, height=canvas_height, bg="gray66")
# ^ Alters the size of the canvas (by pixels), and adds a background (bg) color to the canvas ^

main_canvas_image = PhotoImage(file="images/final_door_images/fd_1080x720.gif")
# ^ Adds image to the canvas, includes file path ^
padlock_on_door.create_image(0, 0, image=main_canvas_image, anchor=NW)  # Defines where the image is anchored

win_screen = PhotoImage(file='images/bomb_game_images/win_screen.gif')
game_over = PhotoImage(file='images/bomb_game_images/game_over.gif')
return_image = PhotoImage(file="images/light_bulb_images/return_arrow.gif")
padlock_on_door.create_image(100, 650, image=return_image)

triesA = set()
triesB = []


if background_premade_code.value_at(1) == "W":
    hint1 = "So you think you're good at math? Complete the sequence:\n" \
            "1=3, 2=3, 3=5, 4=4, 5=4, 6=3, 7=5, 11=?"  # 1, once you subtract it, its no longer 120.
else:
    hint1 = "Try going back to the room and winning the Maze Game"
if background_premade_code.value_at(2) == "W":
    hint2 = "If two's a company, and three's a crowd, what is 4 and 5?"  # 9 because 4+5=9
else:
    hint2 = "Try going back to the room and winning the Bulb Game"
if background_premade_code.value_at(3) == "W":
    hint3 = "How many dots are in this sentence: The possibilities are endless."
    # ^ 9 there are nine after the colon including the period ^
else:
    hint3 = "Try going back to the room and winning the Bomb Game"
if background_premade_code.value_at(4) == "W":
    hint4 = "If there are 4 apples and you take away 3 how many do you have?"  # 3 because you took 3
else:
    hint4 = "Try going back to the room and winning the Spot the Difference Game"
if background_premade_code.value_at(5) == "W":
    hint5 = "You are a participant in a race. You pass the person in second place. What position are you in?"
    # ^ 2 because you passed the person in second ^
else:
    hint5 = "Try going back to the room and winning the Riddle Game"


# ----------------------------------------------------------------------------------------------------------------------
#                                           Create commands
# ----------------------------------------------------------------------------------------------------------------------

def select_game(event):
    x1, y1 = event.x, event.y
    # Get mouse click coordinates. (0,0) is the top left corner of the map. ^
    if (422 <= x1 <= 446) and (371 <= y1 <= 402):
        current_hint = hint1
    elif (471 <= x1 <= 492) and (371 <= y1 <= 404):
        current_hint = hint2
    elif (515 <= x1 <= 537) and (371 <= y1 <= 404):
        current_hint = hint3
    elif (561 <= x1 <= 584) and (371 <= y1 <= 408):
        current_hint = hint4
    elif (608 <= x1 <= 630) and (371 <= y1 <= 408):
        current_hint = hint5
    elif 10 < x1 < 190 and 610 < y1 < 685:
        exit()

    else:
        current_hint = "Click directly below each entry for the corresponding hint."

    hint_label.configure(text=current_hint)


# Setting Mouse cursor for several buttons
def change_mouse_cursor():
    # Absolute coordinate of the pointer on monitor screen
    coord_absolute = main_canvas.winfo_pointerxy()

    # Coordinate of the GUI (point 0,0 of the canvas) on monitor screen
    x_coord_gui = main_canvas.winfo_rootx()
    y_coord_gui = main_canvas.winfo_rooty()

    # Coordinate of pointer on GUI
    x1 = coord_absolute[0] - x_coord_gui
    y1 = coord_absolute[1] - y_coord_gui

    # Setting the cursor
    if (422 <= x1 <= 446) and (371 <= y1 <= 402) or (471 <= x1 <= 492) and (371 <= y1 <= 404) or (
                    515 <= x1 <= 537) and (371 <= y1 <= 404) or (561 <= x1 <= 584) and (371 <= y1 <= 408) or (
                    608 <= x1 <= 630) and (371 <= y1 <= 408) or (10 < x1 < 190 and 610 < y1 < 685):
        main_canvas.config(cursor="hand2")

    else:
        main_canvas.config(cursor="left_ptr")

    # Loop
    main_canvas.after(5, change_mouse_cursor)


def attempt():
    triesA.add("1")
    if "1" in triesA:
        triesB.append(1)

    if len(triesB) == 0:
        hint_label.configure(text="You guessed incorrectly and heard something rattle inside the lock...")

    if len(triesB) == 1:
        hint_label.configure(text="You guessed incorrectly and heard something rattle inside the lock...")

    if len(triesB) == 2:
        hint_label.configure(text="The button felt looser this time, better be careful going forward...")

    if len(triesB) == 3:
        hint_label.configure(text="This time you heard a definitive snap, the lock mechanism must be breaking...")

    if len(triesB) == 4:
        hint_label.configure(text="The combination disks were hard to turn as you input the new numbers,\n "
                                  "something is definitely wrong...")

    if len(triesB) == 5:
        hint_label.configure(text="You hear another snap, the lock will surely break\n "
                                  "if you keep guessing incorrectly... (I wouldn't try again if I were you)")

    if len(triesB) >= 6:
        you_lose()

    try:
        pe1a = int(padlock_entry_1.get())
        pe2b = int(padlock_entry_2.get())
        pe3c = int(padlock_entry_3.get())
        pe4d = int(padlock_entry_4.get())
        pe5e = int(padlock_entry_5.get())
    except ValueError:
        return

    if pe1a == 6 and pe2b == 9 and pe3c == 9 and pe4d == 3 and pe5e == 2 and len(triesB) < 6:
        you_win()


def you_win():
    main_canvas.unbind("<Button 1>")
    # Unbind the canvas. The game is over.
    padlock_on_door.unbind("<Button-1>")
    attempt_button.configure(state=DISABLED)
    padlock_entry_1.configure(text="", bg="green")
    padlock_entry_2.configure(text="", bg="green")
    padlock_entry_3.configure(text="", bg="green")
    padlock_entry_4.configure(text="", bg="green")
    padlock_entry_5.configure(text="", bg="green")

    # Change his/her stat
    background_premade_code.write_value_to_pos("W", 6)

    print ANSI.RED + "YOU WON!!!!!!!!!" + ANSI.END

    winners_screen = Toplevel()
    winners_screen.title("Winner's Screen")
    losers_or_winners_screen_canvas = Canvas(winners_screen, width=600, height=300, bg="black")
    losers_or_winners_screen_canvas.grid(row=0, columnspan=50)
    losers_or_winners_screen_canvas.create_image(0, 0, image=win_screen, anchor=NW)
    home2_button = Button(
        winners_screen, text="RETURN HOME", bg='blue', cursor='X_cursor', command=exit)
    home2_button.grid(row=1, column=40)
    home2_button.config(width=25)


def you_lose():
    main_canvas.unbind("<Button 1>")
    # Unbind the canvas. The game is over.
    padlock_on_door.unbind("<Button-1>")
    attempt_button.configure(state=DISABLED)
    padlock_entry_1.configure(text="", bg="red")
    padlock_entry_2.configure(text="", bg="red")
    padlock_entry_3.configure(text="", bg="red")
    padlock_entry_4.configure(text="", bg="red")
    padlock_entry_5.configure(text="", bg="red")

    # Change his/her stat
    background_premade_code.write_value_to_pos("L", 6)

    losers_screen = Toplevel()
    losers_screen.title("Loser's Screen")
    losers_or_winners_screen_canvas = Canvas(losers_screen, width=600, height=300, bg="black", cursor='pirate')
    losers_or_winners_screen_canvas.grid(row=0, columnspan=5)
    losers_or_winners_screen_canvas.create_image(20, 15, image=game_over, anchor=NW)
    home2_button = Button(
        losers_screen, text="RETURN HOME", bg='blue', cursor='X_cursor', command=exit)
    home2_button.grid(column=2)
    home2_button.config(width=50)


def return_to_the_main_room_winning():
    print ANSI.RED + "You escaped!" + ANSI.END
    exit()


def return_to_the_main_room_losing():
    print ANSI.RED + "You broke the lock and were trapped. You lose!" + ANSI.END
    exit()

# ----------------------------------------------------------------------------------------------------------------------
#                                           Add widgets to GUI
# ----------------------------------------------------------------------------------------------------------------------


padlock_on_door.grid(row=1, column=0, rowspan=72, columnspan=108)
# ^ Defines where the image: bomb_in_closet is in the newly formed grid ^
padlock_on_door.bind("<Button-1>", select_game)
# ^ Turns the entire bomb_in_closet image into a button ^
# ^^ then narrows the selection by activating the select_bomb_display command when you click in the right area ^^


padlock_entry_1 = Entry(main_canvas, justify=CENTER, width=2)
padlock_entry_1.grid(row=38, column=49)

padlock_entry_2 = Entry(main_canvas, justify=CENTER, width=2)
padlock_entry_2.grid(row=38, column=52)

padlock_entry_3 = Entry(main_canvas, justify=CENTER, width=2)
padlock_entry_3.grid(row=38, column=55)

padlock_entry_4 = Entry(main_canvas, justify=CENTER, width=2)
padlock_entry_4.grid(row=38, column=59)

padlock_entry_5 = Entry(main_canvas, justify=CENTER, width=2)
padlock_entry_5.grid(row=38, column=63)

attempt_button = Button(main_canvas, text="Unlock", command=attempt, bg="goldenrod3", font="Arial 12 bold")
# ^ Creates a button with the text "Return to the room" on it ^
# ^^ with a red background that runs the "return_to_the_main_room" command ^^
attempt_button.grid(row=38, column=65)  # Defines where the newly formed button will be in the grid

hint_label = Label(main_canvas, text="Click directly below each entry for the corresponding hint.",
                   font="Arial 15 bold")
# hint_label.grid(row=48, column=19, columnspan=55, sticky="EW")
hint_label.grid(columnspan=100, )

change_mouse_cursor()

mainloop()
