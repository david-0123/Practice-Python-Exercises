import json

def read():
    oldName = input("\nWho do you want to look up?\n").title()

    try:
        print("{}'s birthday is {}".format(oldName, birthdays[oldName]))
    except KeyError:
        print("{}'s birthday is not in the dictionary.".format(oldName))

def write():
    newName = input("\nWho do you want to write?\n").title()
    date = input("What is their birthday?\n")

    birthdays[newName] = date

    with open('birthdays.json', 'w') as outf:
        json.dump(birthdays, outf)

    print("{}'s birthday has been added to the dictionary".format(newName))


with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)

print("Welcome to the birthday dictionary! We know the birthdays of:")
for name in birthdays.keys():
    print(name)

while True:
    choice = input("\nDo you want to read or write to the dictionary? [r/w] ").lower()
    if choice == 'r':
        read()
        break
    elif choice == 'w':
        write()
        break
    else:
        print("Invalid input. Please enter 'r' to read or 'w' to write.")