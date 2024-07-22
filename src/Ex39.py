import datetime as dt

name = input("Enter your name: ").title()
age = int(input("Enter your age: "))
num = int(input("How many times? "))

for i in range(num):
    print(f"Hello {name}, You'll turn 100 in {dt.datetime.now().year - age + 100}")
