from random import *

guesses = 0
target = randint(1,9)

choice = ""

while choice != "exit":
    choice = input("Enter a number between 1 and 9 or \"exit\" to stop: ")

    if choice.isdigit():
        if int(choice) == target:
            print("Correct after {} guesses".format(guesses+1))
            break
        elif int(choice) < target:
            print("Too low\n")
            guesses += 1
        elif int(choice) > target:
            print("Too high\n")
            guesses += 1
        elif choice != "exit":
            print("Invalid input\n")