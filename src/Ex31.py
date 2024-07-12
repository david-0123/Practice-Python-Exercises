import random

with open("words.txt", "r") as f:
    words = f.read().splitlines()
    word = random.choice(words)

def showWord():
    text = ''
    for letter in guessed:
        text += letter
    print('\n'+text)

guessed = ["_" for x in range(len(word))]
gameOver = False

print("Welcome to Hangman!")
showWord()

while not gameOver:
    guess = input("Guess a letter: ").upper()

    if guess in guessed:
        print(f"You've already guessed {guess}")
    else:
        if guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    guessed[i] = guess
            showWord()
        else:
            print("Incorrect!\n")

    if "_" not in guessed:
        print("You win!")
        gameOver = True

print("Game Over!")