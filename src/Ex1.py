name = input("Enter your name: ")
age = int(input("Enter your age: "))
num = int(input("How many times? "))

for i in range(num):
    print("Hello {}, You'll turn 100 in {}".format(name, str(2024 - age + 100)))
