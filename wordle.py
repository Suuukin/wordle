import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image


class State:
    labels = {}  # {point, label}


def label_maker(frame):
    return tk.Label(frame, text="x", font=GRID_FONT, borderwidth=3, padx=20, pady=10)


def main():
    global GRID_FONT
    window = tk.Tk()
    window.title("Wordle")
    window.resizable(False, False)
    GRID_FONT = font.Font(family="Courier", size=50, weight="bold")

    guess_area = tk.Frame(window, width=300, height=50, bg="honeydew2")
    keyboard_row_1 = tk.Frame(window, width=300, height=50, bg="honeydew2")
    keys_row_1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
    keyboard_row_2 = tk.Frame(window, width=300, height=50, bg="honeydew2")
    keys_row_2 = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
    keyboard_row_3 = tk.Frame(window, width=300, height=50, bg="honeydew2")
    for y in range(1, 6):
        for x in range(1, 5):
            label = label_maker(guess_area)
            State.labels[(x, y)] = label
            label.grid(row=x, column=y, sticky="nsew")

    guess_area.grid(row=1, column=1, sticky="nsew")
    window.mainloop()


if __name__ == "__main__":
    main()
