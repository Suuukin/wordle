import random
import wordlist

wordle = random.choice(wordlist.wordle_list)
letters = list(wordle)
ask_end_game = True

print(wordle)

position_hints = input("Do you want positional hints (y, n, detailed)? ")


def position_check(string, guess):
    positions = []  # list to store positions for each 'char' in 'wordle'
    for location in range(len(string)):
        if string[location] == guess:
            positions.append(location + 1)
    return positions


while True:
    guess = input("Guess a letter in the wordle. ")

    if guess in list(wordle):
        print(f"The letter {guess} is in the wordle.")

        if position_hints == "y":
            position = wordle.find(guess)
            print(f"The first position of your guess in the wordle is {position+1}. ")
        elif position_hints == "detailed":
            positions = position_check(wordle, guess)
            print(f"Your guess is in the position(s) {positions}. ")
    else:
        print(f"The letter {guess} is not in the wordle.")

    if ask_end_game:
        end_game = input(
            "Want to end the game (y,n)? To turn off this question type 'never'. "
        )
        if end_game == "never":
            ask_end_game = False

    if end_game == "y":
        break

print("Thanks for playing!")
