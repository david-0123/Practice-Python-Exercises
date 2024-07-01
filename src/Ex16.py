from random import *
from string import *

def pwGen():
    pw = ""
    pwLength = randint(10,15)

    symbols = []
    for i in range(33,48):
        symbols.append(chr(i))
    for j in range(58,65):
        symbols.append(chr(j))
    for k in range(91,97):
        symbols.append(chr(k))
    for l in range(91,97):
        symbols.append(chr(l))

    while pwLength > 0:
        character = choice([ascii_letters, digits, symbols])
        length = randint(1, min(3,pwLength))
        for elem in choices(character, k=length):
            pw += elem
        pwLength -= length

    return pw

print(pwGen())