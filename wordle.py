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

print(State.wordle)

def label_maker(frame):
    return tk.Label(frame, text="x", font=GRID_FONT, borderwidth=3, padx=20, pady=10)

def btn_maker(frame, text):
    return tk.Button(frame, text=text, font=KEYBOARD_FONT, operation=btn_op(text))

def btn_op(text):
    return

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