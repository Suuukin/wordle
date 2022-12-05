import random
import wordlist

# flake8: noqa

class State:
    """Class to hold global variables."""
    wordle = random.choice(wordlist.wordle_list)
    letters = list(wordle)
    ask_end_game = True
    guess_words = None
    position_hints = None
    invalid_guess = False


State.guess_words = input("Do you want to enter full words as guesses (y,n)? ")
State.position_hints = input("Do you want positional hints (y, n, detailed, colors)? ")
 
print(State.wordle)


def detailed_position_check(guess_letter):
    """Checks for what positions the letter is in the wordle.
    Then returns all the positions that the letter is in."""
    positions = []  # list to store positions for each 'char' in 'wordle'
    for i, location in enumerate(State.letters):
        if State.letters[i] == guess_letter:
            positions.append(i + 1)
    return positions


def position_check(letter, guess_word=None, i=None):
    """Selects which hint and positional clues the simple_wordle should return."""
    if State.position_hints == "colors":
        if letter not in State.letters: 
            # if the letter not in the word then the color is red
            color = "Red"
        else:
            # sets the color to yellow if in the word
            color = "Yellow"
        if State.wordle[i] == letter:
            color = "Green"
        print(f"{letter} is {color}.")
        return

    if letter in State.letters:
        if State.position_hints == "y":
            # if position_hints is simple mode than it
            # returns the first position of the guessed letter in the word
            position = State.wordle.find(letter)
            print(f"The first position of {letter} in the wordle is {position+1}. ")

        elif State.position_hints == "detailed":
            # if position_hints is complex than it returns all positions of the guessed letter
            positions = detailed_position_check(letter)
            print(f"Letter {letter} is in the position(s) {positions}. ")

    else:
        print(f"The letter {letter} is not in the wordle.")


def word_in_wordle_list():
    if guess_word not in wordlist.wordle_list:
        State.invalid_guess = True
        print("Your guessed word is not in the wordle list.")
    else:
        State.invalid_guess = False
    

while True:
    """Loop that runs the game until the wordle is guessed."""
    if State.guess_words == "y":
        guess_word = input("Guess a five letter word. ")
        word_in_wordle_list()
        if not State.invalid_guess:
            if guess_word == State.wordle:
                # ends loop if guessed word is correct
                print("You guessed the Wordle!")
                break
            else:
                for i, letter in enumerate(guess_word):
                    # checks all the letters and returns the correct positional hints
                    position_check(letter, guess_word, i)

    else:
        guess_letter = input("Guess a letter in the wordle. ")
        position_check(guess_letter)

#    if State.ask_end_game:
#        end_game = input(
#            "Want to end the game (y,n)? To turn off this question type 'never'. "
#        )
#        if end_game == "never":
#            ask_end_game = False
#
#    if end_game == "y":
#        break

print("Thanks for playing!")
