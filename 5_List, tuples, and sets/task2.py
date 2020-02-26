# Exclusive common numbers
#
# This program is longer than necessary, but it helped to deal with 'while'.
# So I’ll leave it.
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
    j = 0
    while j < 10:
        if list1[i] == list2[j] and list1[i] not in list3:
            list3.append(list1[i])
        j += 1
    i += 1
print(list3)
