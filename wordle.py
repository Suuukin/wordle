import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image
import wordlist
import random
# flake8: noqa


class State:
    labels = {}  # {point, label}
    buttons = {} # {key_text, button}
    wordle = random.choice(wordlist.wordle_list)
    keyboard_frames = {}
    current_row = 1
    current_column = 1
    word = None
    game_won = False

print(State.wordle)

def label_maker(frame):
    """Function to creates the labels in the 5*6 grid."""
    return tk.Label(frame, text="x", font=GRID_FONT, borderwidth=3, padx=20, pady=10)

def btn_maker(frame, text):
    """Function to create the buttons for the keyboard."""
    return tk.Button(frame, text=text, font=KEYBOARD_FONT, command=lambda: btn_op(text))

def position_check(wordle,letter):
    positions = []  # list to store positions for each 'char' in 'wordle'
    for location in range(len(wordle)):
        if wordle[location] is letter:
            positions.append(location + 1)
    return positions

def letter_check(letter):
    if letter in State.wordle:
        position_check()
        

def submit_word():
    """When you press Enter checks your word and tells you what letters are in the wordle."""
    if State.word is State.wordle:
        State.game_won = True
    if State.word in wordlist.wordle_list:
        State.current_row += 1
        for letter in list(State.word):
            letter_check(letter)

def clear_line():
    """Resets all the labels in the row."""
    return

#def row_selector():
#    """Moves to the next row after a guess is successfully submitted."""
#    return
#
#def column_selector():
#    """Selects which slot in the row the letter clicked should go."""
#    return

def update_label(row, column, text):
    """Updates the label on the grid with the key pressed."""
    label = State.labels[(row, column)]
    label.configure(text=text)
    State.word = State.word+text
    return

def update_square(text):
    """Finds the right slot in the grid and then updates label."""
    #row = row_selector()
    #column = column_selector()
    update_label(State.current_row, State.current_column, text)
    State.current_row += 1
    print(State.current_row)

def btn_op(text):
    """Checks if it's a special button or to just run the default for keyboard."""
    if text == "ENTER":
        submit_word()
    elif text == "CE":
        clear_line()
    else:
        update_square(text)


KEY_ROWS = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]

def main():
    global GRID_FONT
    global KEYBOARD_FONT

    window = tk.Tk()
    window.title("Wordle")
    window.resizable(False, False)

    GRID_FONT = font.Font(family="Courier", size=50, weight="bold")
    KEYBOARD_FONT = font.Font(family='Courier', size=30, weight="bold")

    guess_area = tk.Frame(window, width=300, height=200, bg="honeydew2")
    guess_area.grid(row=0, column=1)


    for y in range(1, 7):
        for x in range(1, 6):
            label = label_maker(guess_area)
            State.labels[(x, y)] = label
            label.grid(row=y, column=x, sticky="nsew")


    for row, key_row in enumerate(KEY_ROWS):
        State.keyboard_frames[row] = frame = tk.Frame(window, width=300, height=50, bg="honeydew2")
        frame.grid(row=row+2, column=1)
        keys = list(key_row)
        for column, key_text in enumerate(keys):
            State.buttons[key_text] = button = btn_maker(frame, key_text)
            button.grid(row=1, column=column+1)

    enter_btn = btn_maker(State.keyboard_frames[2], "ENTER")
    enter_btn.grid(row=1, column=0)
    clear_btn = btn_maker(State.keyboard_frames[2], "CE")
    clear_btn.grid(row=1, column=10)


    window.mainloop()


if __name__ == "__main__":
    main()