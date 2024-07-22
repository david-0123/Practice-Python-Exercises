from random import *

number_of_guesses = 0
number = randint(1, 9)

while True:
    try:
        guess = int(input("Guess a number between 1 and 9: "))
    except ValueError:
        print("Invalid value entered\n")
    else:
        if 1 <= guess <= 9:
            number_of_guesses += 1
            if guess == number:
                break
        else:
            print("Number must be between 1 and 9\n")

print(f"You needed {number_of_guesses} guesses to guess the number {number}")