# "Bomb_Game" By: Alston Sanford

# ----------------------------------------------------------------------------------------------------------------------
#                            Import Modules, Create Initial Canvas, and Begin Initial Code
# ----------------------------------------------------------------------------------------------------------------------

from Tkinter import *
# import os
import time
import webbrowser
# import math
# import random
import pickle
import anydbm
import background_premade_code


class ANSI:
    RED = '\033[91m'
    END = '\033[0m'

main_canvas = Tk()
main_canvas.title("Defuse the Bomb!")
game_window = Canvas(main_canvas, width=1080, height=680, bg="black")
game_window.grid(row=0, columnspan=4)

saw = PhotoImage(file='images/bomb_game_images/saw.gif')
wires = PhotoImage(file='images/bomb_game_images/ibg_1080x720.gif')
explode = PhotoImage(file='images/bomb_game_images/explosion.gif')
defused = PhotoImage(file='images/bomb_game_images/defused.gif')
win_screen = PhotoImage(file='images/bomb_game_images/win_screen.gif')
game_over = PhotoImage(file='images/bomb_game_images/game_over.gif')

countdown_stopped = False
out_of_time = False
error = False

global increment
increment = 1


# ----------------------------------------------------------------------------------------------------------------------
#                                           Create commands
# ----------------------------------------------------------------------------------------------------------------------

def countdown(n):
    start_button.destroy()
    if n == 90:
        global t0
        t0 = time.clock()
        game_window.bind("<Button-1>", cut_wire)  # enable clicking on game_window
        pause_button.config(state=NORMAL, cursor='wait')
        hint_button.config(state=NORMAL, cursor='question_arrow')
        status_box.delete(0, END)
        status_box.insert(0, "ARMED")
        status_box.config(bg='red')
        hint_box.delete(0, END)
        hint_box.insert(0, 'Caboose')
        game_window.create_image(0, 0, image=wires, anchor=NW)
    global out_of_time
    if out_of_time:
        return
    global countdown_stopped
    if countdown_stopped:
        timer_box.delete(0, END)
        timer_box.insert(0, '')
        countdown_stopped = False  # Update this for the next bomb
        pause_button.config(state=DISABLED)
        hint_button.config(state=DISABLED)
        status_box.delete(0, END)
        status_box.insert(0, 'DISARMED')
        status_box.config(bg='green')
        return
    if n < 0:
        lose()
        return
    else:
        timer_box.delete(0, END)
        timer_box.insert(0, n)  # keep the countdown going
        main_canvas.after(1000, countdown, n-increment)  # wait one second, then continue countdown.
        global error
        if error:
            timer_box.delete(0, END)
            timer_box.insert(0, 'ERROR')
            timer_box.config(bg='black', fg='red')


def hint():
    global hints_remaining
    if hints_remaining == 2:
        hints_remaining -= 1
        hints_remaining_box.delete(0, END)
        hints_remaining_box.insert(0, hints_remaining)
        hint_box.delete(0, END)
        hint_box.insert(0, 'Take this and the story ends')
    else:
        hint_button.config(state=DISABLED, cursor='arrow')
        hints_remaining_box.delete(0, END)
        hints_remaining_box.insert(0, "YOU'RE OUT!")
        hint_box.delete(0, END)
        hint_box.insert(0, 'Eiffel 65')


def trap():
    global increment
    increment = 10
    pause_button.config(state=DISABLED, cursor='arrow')
    hint_button.config(state=DISABLED, cursor='arrow')
    hints_remaining_box.delete(0, END)
    hints_remaining_box.insert(0, 'DEATH IS COMING')
    hint_box.delete(0, END)
    hint_box.insert(0, 'BOOBY TRAP ACTIVATED')


def lose():  # LOSE
    game_window.unbind("<Button 1>")
    game_window.config(cursor='arrow')
    timer_box.delete(0, END)
    timer_box.insert(0, 'BOOM!')
    timer_box.config(bg='red', fg='black')
    status_box.delete(0, END)
    status_box.insert(0, 'BOOM!')
    status_box.config(bg='red')
    hint_box.delete(0, END)
    hint_box.insert(0, 'BOOM!')
    hint_box.config(bg='red')
    hints_remaining_box.delete(0, END)
    hints_remaining_box.insert(0, 'BOOM!')
    hints_remaining_box.config(bg='red')
    pause_button.config(state=DISABLED)
    hint_button.config(state=DISABLED)
    game_window.create_image(350, 225, image=explode, anchor=CENTER)

    losers_screen = Toplevel()
    losers_screen.title("Loser's Screen")
    losers_or_winners_screen_canvas = Canvas(losers_screen, width=600, height=300, bg="black", cursor='pirate')
    losers_or_winners_screen_canvas.grid(row=0, columnspan=5)
    losers_or_winners_screen_canvas.create_image(20, 15, image=game_over, anchor=NW)
    home2_button = Button(losers_screen, text="RETURN HOME", bg='blue', cursor='X_cursor', command=return_home)
    home2_button.grid(column=2)
    home2_button.config(width=50)

    # Get the name of the current player
    db = anydbm.open("data/current_player.db", "c")
    current_player_name = db["name"]
    db.close()

    # Change his/her stat
    player_database = pickle.load(open("data/player_database.p", "rb"))
    player_database[current_player_name][6] = "L"
    pickle.dump(player_database, open("data/player_database.p", "wb"))


def win():
    global dt
    dt = int(time.clock() - t0)
    global countdown_stopped
    countdown_stopped = True
    hint_box.delete(0, END)
    hints_remaining_box.delete(0, END)
    game_window.unbind("<Button 1>")

    winners_screen = Toplevel()
    winners_screen.title("Winner's Screen")
    losers_or_winners_screen_canvas = Canvas(winners_screen, width=600, height=300, bg="black")
    losers_or_winners_screen_canvas.grid(row=0, columnspan=50)
    losers_or_winners_screen_canvas.create_image(0, 0, image=win_screen, anchor=NW)
    home2_button = Button(winners_screen, text="RETURN HOME", bg='blue', cursor='X_cursor', command=return_home)
    home2_button.grid(row=1, column=40)
    home2_button.config(width=25)
    Label(winners_screen, text="You defused the bomb in:").grid(row=1, column=10)
    score_box = Entry(winners_screen, justify=CENTER, width=3)
    score_box.grid(row=1, column=11)
    score_box.insert(0, dt)
    Label(winners_screen, text="seconds.").grid(row=1, column=12)

    # Change stat
    background_premade_code.write_value_to_pos("W", 3)


def start_game():
    start_button.config(state=NORMAL)
    pause_button.config(state=DISABLED)
    hint_button.config(state=DISABLED)
    game_window.create_image(540, 360, image=saw, anchor=CENTER)


def return_home():
    exit()


def cut_wire(event):

    x1, y1 = event.x, event.y  # Get mouse click coordinates

    if (334 >= x1 >= 280) & (374 >= y1 >= 157):  # green (explosion wire)
        global out_of_time
        out_of_time = True
        lose()

    elif (505 >= x1 >= 462) & (374 >= y1 >= 157):  # blue (correct wire)
        win()
        game_window.create_image(350, 225, image=defused, anchor=CENTER)

    elif (698 >= x1 >= 628) & (374 >= y1 >= 157):  # yellow (time display turns off)
        global error
        error = True

    elif (924 >= x1 >= 738) & (288 >= y1 >= 203):  # battery (bomb defused)
        win()
        game_window.create_image(350, 225, image=defused, anchor=CENTER)

    elif (737 >= x1 >= 215) & (460 >= y1 >= 375) or \
         (811 >= x1 >= 716) & (486 >= y1 >= 379) or \
         (868 >= x1 >= 773) & (418 >= y1 >= 380):  # pink (troll wire)
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


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
    if (334 >= x1 >= 280) & (374 >= y1 >= 157):
        main_canvas.config(cursor="hand1")
    elif (505 >= x1 >= 462) & (374 >= y1 >= 157):
        main_canvas.config(cursor="hand1")
    elif (698 >= x1 >= 628) & (374 >= y1 >= 157):
        main_canvas.config(cursor="hand1")
    elif (737 >= x1 >= 215) & (460 >= y1 >= 375) or \
         (811 >= x1 >= 716) & (486 >= y1 >= 379) or \
         (868 >= x1 >= 773) & (418 >= y1 >= 380):
        main_canvas.config(cursor="hand2")

    else:
        main_canvas.config(cursor="left_ptr")

    # Loop
    main_canvas.after(5, change_mouse_cursor)

# ----------------------------------------------------------------------------------------------------------------------
#                                           Add widgets to GUI
# ----------------------------------------------------------------------------------------------------------------------


Label(main_canvas, text="Time").grid(row=1, column=0)
timer_box = Entry(justify=CENTER)
timer_box.grid(row=1, column=1)
timer_box.insert(0, '90')

Label(main_canvas, text="STATUS").grid(row=2, column=0)
status_box = Entry(justify=CENTER)
status_box.grid(row=2, column=1)

Label(main_canvas, text="Hint").grid(row=3, column=0)
hint_box = Entry(justify=CENTER, width=25)
hint_box.grid(row=3, column=1)

Label(main_canvas, text="Hints Remaining").grid(row=4, column=0)
hints_remaining_box = Entry(justify=CENTER)
hints_remaining_box.grid(row=4, column=1)
hints_remaining = 2
hints_remaining_box.insert(0, hints_remaining)

# The four control buttons are constructed here.
start_button = Button(main_canvas, text="START", cursor='hand2', command=lambda: countdown(90))
start_button.grid(row=1, column=3)

pause_button = Button(main_canvas, text="PAUSE", command=trap)
pause_button.grid(row=2, column=3)

hint_button = Button(main_canvas, text="HINT", command=hint)
hint_button.grid(row=3, column=3)

start_game()

change_mouse_cursor()

main_canvas.mainloop()
