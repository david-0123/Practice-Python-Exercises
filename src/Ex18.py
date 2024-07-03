import random

attempts = 1

def generate_num():
    rem_digits = [0,1,2,3,4,5,6,7,8,9]
    target = []
    for i in range(4):
        choice = random.choice(rem_digits)
        target.append(choice)
        rem_digits.remove(choice)

    return target

def check_guess(target, guess):
    global attempts

    for x in range(4):
        guess[x] = int(guess[x])

    if target == guess:
        print("4 cows, 0 bulls\nCorrect after {} guesses!".format(attempts))
        return True
    else:
        cows = 0
        bulls = 0
        for i in range(4):
            if guess[i] == target[i]:
                cows += 1
            else:
                if guess[i] in target:
                    bulls += 1
        print("{} cows, {} bulls\n".format(cows, bulls))
        attempts += 1
        return False

def main():
    print("Welcome to the Cows and Bulls Game!")
    target = generate_num()
    # print(target)

    correct = False
    while not correct:
        guess = input("Guess a number: ")
        guessList = [digit for digit in guess]

        correct = check_guess(target, guessList)

if __name__ == '__main__':
    main()