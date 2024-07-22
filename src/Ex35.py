from collections import Counter
import json

monthList = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

months = []

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

for date in birthdays.values():
    month = date.split("/")[1]
    if 0 < int(month) < 13:
        months.append(monthList[int(month)-1])

print("Scientists with birthdays in the following months:")
c = Counter(months)
for i in c:
    print(f"{i}: {c[i]}")