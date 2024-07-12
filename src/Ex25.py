import math

low = 1
high = 100
current = math.floor((low+high)/2)
guessed = False
guesses = 0

while not guessed:
    response = input("Is your number {}? ".format(current))
    guesses += 1
    if response == "high":
        high = current
        current = math.ceil((low+high)/2)
    elif response == "low":
        low = current
        current = math.ceil((low+high)/2)
    elif response == "correct":
        print("Took me {} guesses!".format(guesses))
        guessed = True
    else:
        print("Sorry, I did not understand.")