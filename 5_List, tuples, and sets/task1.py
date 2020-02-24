# The greatest number
from random import randint
list1 = []
i = 0
while i < 10:
    a = randint(0, 9)
    list1.append(a)
    i += 1
print(list1)
print(sorted(list1)[-1])
