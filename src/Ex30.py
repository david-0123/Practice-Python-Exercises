import random

with open("words.txt", "r") as f:
    words = f.read().splitlines()
    word = random.choice(words)

print(word)