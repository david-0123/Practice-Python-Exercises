import random

def showWord(guessed):
    text = ''
    for letter in guessed:
        text += letter
    print(text)

def drawHangman(num):
    parts = {
        "0": [],
        "1": ["  O"],
        "2": ["  O", "  ¦"],
        "3": ["  O", " /¦"],
        "4": ["  O", " /¦\\"],
        "5": ["  O", " /¦\\", " /"],
        "6": ["  O", " /¦\\", " / \\"]
    }

    print('''*****
  |''')
    for elem in parts[str(num)][:-1]:
        print(elem)
    print(parts[str(num)][-1], end="   ")

def main():
    with open("words.txt", "r") as f:
        words = f.read().splitlines()
        word = random.choice(words)

    guessed = ["_" for x in range(len(word))]
    userGuessed = []
    remaining = 6
    gameOver = False
    won = False

    print("Welcome to Hangman!\n")
    showWord(guessed)

    while not gameOver and remaining > 0:
        guess = input(f"Lives Remaining: {remaining}\nGuess a letter: ").upper().strip()
        if guess == "":
            continue

        if guess in userGuessed:
            print(f"You've already guessed {guess}")
        else:
            userGuessed.append(guess)
            if guess in word:
                for i in range(len(word)):
                    if guess == word[i]:
                        guessed[i] = guess
                print()
                showWord(guessed)
            else:
                print("\nIncorrect!")
                remaining -= 1
                drawHangman(6-remaining)

        if "_" not in guessed:
            print("You win!")
            gameOver = True
            won = True

    if not won:
        print("\nGame Over!")
        print("The word was ", end="")
        showWord(word)

    again = input("\nWould you like to play again? (y/n) ").lower()
    if again == "y":
        main()

main()