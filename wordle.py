import tkinter as tk
import tkinter.font as font
import wordlist
import random

# flake8: noqa


class State:
    labels = {}  # {point, label}
    buttons = {}  # {key_text, button}
    wordle = random.choice(wordlist.wordle_list)
    letters = list(wordle)
    keyboard_frames = {}
    current_y = 1
    current_x = 1
    guess = ""
    game_over = False
    invalid_guess = False


print(State.wordle)


def label_maker(frame):
    """Function to creates the labels in the 5*6 grid."""
    return tk.Label(
        frame,
        text=" ",
        font=GRID_FONT,
        borderwidth=3,
        padx=20,
        pady=10,
        relief="groove",
    )


def btn_maker(frame, text):
    """Function to create the buttons for the keyboard."""
    return tk.Button(frame, text=text, font=KEYBOARD_FONT, command=lambda: btn_op(text))


def update_label(label, text=None, color=None):
    label.configure(text=text, bg=color)


def position_check(guess_letter):
    """Checks for what positions the letter is in the wordle.
    Then returns all the positions that the letter is in."""
    positions = []  # list to store positions for each 'char' in 'wordle'
    for i, location in enumerate(State.letters):
        if State.letters[i] == guess_letter:
            positions.append(i + 1)
    return positions


def letter_check(wordle, letter, i):
    if letter not in State.letters:
        color = "grey"
    else:
        # sets the color to yellow if in the word
        color = "yellow"
    if State.wordle[i] == letter:
        color = "green"
    return color


def clear_line():
    """Resets all the labels in the row."""
    for x in range(1, 6):
        label = State.labels[(x, State.current_y)]
        update_label(label, text=" ")
    State.current_x = 1
    State.guess = ""


def submit_word():
    """When you press Enter checks your word and tells you what letters are in the wordle."""
    if State.guess is State.wordle:
        State.game_over = True
        return
    if State.guess in wordlist.wordle_list:
        for i, letter in enumerate(State.guess):
            color = letter_check(State.wordle, letter, i)
            label = State.labels[(i + 1, State.current_y)]
            update_label(label, text=None, color=color)
        State.current_y += 1
        print(State.current_y)
        State.current_x = 1
        State.guess = ""
    else:
        clear_line()



def update_letter(x, y, text):
    """Updates the label on the grid with the key pressed."""
    label = State.labels[(x, y)]
    update_label(label, text=text)
    State.guess = State.guess + text
    return


def update_square(text):
    """Finds the right slot in the grid and then updates label."""
    update_letter(State.current_x, State.current_y, text)
    State.current_x += 1
    print(State.current_x)


def btn_op(text):
    """Checks if it's a special button or to just run the default for keyboard."""
    if not State.game_over:
        if State.current_y <= 7:
            if text == "ENTER":
                submit_word()
            elif text == "CE":
                clear_line()
            else:
                update_square(text)


KEY_ROWS = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]


def main():
    global GRID_FONT
    global KEYBOARD_FONT

    window = tk.Tk()
    window.title("Wordle")
    window.resizable(False, False)

    GRID_FONT = font.Font(family="Courier", size=50, weight="bold")
    KEYBOARD_FONT = font.Font(family="Courier", size=30, weight="bold")

    guess_area = tk.Frame(window, width=300, height=200, bg="honeydew2")
    guess_area.grid(row=0, column=1)

    for y in range(1, 7):
        for x in range(1, 6):
            label = label_maker(guess_area)
            State.labels[(x, y)] = label
            label.grid(row=y, column=x, sticky="nsew")

    for row, key_row in enumerate(KEY_ROWS):
        State.keyboard_frames[row] = frame = tk.Frame(
            window, width=300, height=50, bg="honeydew2"
        )
        frame.grid(row=row + 2, column=1)
        keys = list(key_row)
        for column, key_text in enumerate(keys):
            State.buttons[key_text] = button = btn_maker(frame, key_text)
            button.grid(row=1, column=column + 1)

    enter_btn = btn_maker(State.keyboard_frames[2], "ENTER")
    enter_btn.grid(row=1, column=9)
    clear_btn = btn_maker(State.keyboard_frames[0], "CE")
    clear_btn.grid(row=1, column=11)

    window.mainloop()


if __name__ == "__main__":
    main()
