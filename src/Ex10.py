from random import *

a = sample(range(1, 100), randint(1, 10))
b = sample(range(1, 100), randint(1, 10))

if len(a) > len(b):
    ans = [x for x in a if x in b]
else:
    ans = [x for x in b if x in a]

print(a)
print(b)
print(ans)