import random


def game():
    play = input("do you want to play a game?")
    if play in ["yes", "y", "yeah", "yup"]:
        print("Alright let's play the guessing game here's how you play:")
        print("I will choose a card between 1-100. I will give you hints if your guess is too low or too high.")
        print("If you get it right in less than 5 tries, you win. "
              "If you get my number within 5 or more tries, you lose.")
    else:
        return False


game()