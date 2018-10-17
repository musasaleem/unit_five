# Musa Saleem
# Date: October 17, 2018
# Last Modified: October 17, 2018
# Comments: In this program, I  asked if the user wanted to play a game and introduced the user to the guessing game
# I then used random.randint to have the game draw a random number between 1-100 without telling the user
# After, the game gave the user an opportunity to guess the game's number, and the game will either tell the user if
# the guess is too low or too high. Once the user correctly guesses the number, the game will congratulate the user
# and tell the user how many attempts it took to get the number. Finally, the game will ask the user if they want to
# play again. If yes, the user will play another game; if no, the game will end.

import random


def game():
    """
    This is asking the user if they want to play a game and then explaining the guessing game
    :return: True if yes, False if anything else
    """
    play = input("do you want to play a game?")
    if play in ["yes", "y", "yeah", "yup", "sure"]:
        print("Alright let's play the guessing game here's how you play:")
        print("I will choose a card between 1-100. I will give you hints if your guess is too low or too high.")
        return True
    else:
        return False


def draw():
    """
    This function is having the computer draw a random card & having the user guess the value
    :return: Number between 1-100
    """
    return random.randint(1, 100)


def main():
    while game():
        answer = draw()
        guess_total = 0
        while True:
            guess = int(input("Guess my number"))
            guess_total = guess_total + 1
            if guess > answer:
                print("Your guess was too high")

            elif guess < answer:
                print("Your guess was too low")

            elif guess == answer:
                print("Congrats you got my number")
                print("You got my number in", guess_total, "guesses.")
                break
    print("No games for you homie")


main()
