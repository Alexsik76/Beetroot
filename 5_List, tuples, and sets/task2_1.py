# Exclusive common numbers v.2
from random import randint
list1 = []
list2 = []
i = 0
while i < 10:
    a = randint(1, 10)
    b = randint(1, 10)
    list1.append(a)
    list2.append(b)
    i += 1
print(list1)
print(list2)
list3 = []
i = 0
while i < 10:
    if (list1[i] in list2) and (list1[i] not in list3):
        list3.append(list1[i])
    i += 1
print(list3)
