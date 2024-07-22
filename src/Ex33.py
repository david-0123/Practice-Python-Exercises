birthdays = {
    "Albert":"1/2/2000",
    "Bob":"1/2/2001",
    "Carl":"1/2/2002"
}

print("Welcome to the birthday dictionary! We know the birthdays of:")
for name in birthdays.keys():
    print(name)

choice = input("\nWho do you want to look up?\n").title()

try:
    print("{}'s birthday is {}".format(choice, birthdays[choice]))
except KeyError:
    print("{}'s birthday is not in the dictionary.".format(choice))