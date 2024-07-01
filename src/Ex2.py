num = int(input("Enter a number: "))
if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is a multiple of 2")
else:
    print(num, "is an odd number")

check = int(input("Enter a number to divide by: "))
if num % check == 0:
    print(check, "is a factor of", num)
else:
    print(check, "is not a factor of", num)