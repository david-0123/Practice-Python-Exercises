won = False

while not won:
    p1 = input("Enter choice: ")
    p2 = input("Enter choice: ")

    if p1.lower() == "rock":
        if p2.lower() == "scissors":
            print("Player 1 won!")
        elif p2.lower() == "paper":
            print("Player 2 won!")
        elif p2.lower() == "rock":
            print("Draw!")
        else:
            print("Invalid input from Player 2")

    elif p1.lower() == "scissors":
        if p2.lower() == "scissors":
            print("Draw")
        elif p2.lower() == "paper":
            print("Player 1 won!")
        elif p2.lower() == "rock":
            print("Player 2 won!")
        else:
            print("Invalid input from Player 2")

    elif p1.lower() == "paper":
        if p2.lower() == "scissors":
            print("Player 2 won!")
        elif p2.lower() == "paper":
            print("Draw")
        elif p2.lower() == "rock":
            print("Player 1 won!")
        else:
            print("Invalid input from Player 2")

    else:
        print("Invalid input from Player 1")

    again = input("Would you like to play again? (y/n) ").lower()
    if again == "y": won = False
    else: won = True
