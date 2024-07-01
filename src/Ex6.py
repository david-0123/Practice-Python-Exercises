def palindrome(word):
    return word == word[::-1]

userStr = input("Enter a string: ").strip()
if palindrome(userStr):
    print("{} is a palindrome".format(userStr))
else:
    print("{} is not a palindrome".format(userStr))