from random import *

a = sample(range(1, 100), randint(1, 10))
b = sample(range(1, 100), randint(1, 10))

ans = list(set(a) & set(b))
print(a)
print(b)
print(ans)