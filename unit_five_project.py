import random


def game():
    play = input("do you want to play a game?")
    if play in ["yes", "y", "yeah", "yup"]:
        print("Alright let's play the guessing game here's how you play:")
        print("I will choose a card between 1-100. I will give you hints if your guess is too low or too high.")
        return True
    else:
        return False


def draw():
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
