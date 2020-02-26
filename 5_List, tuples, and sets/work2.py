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
print(enumerate(list1))
for j, v in enumerate(list1):
    print(j, v)
j = 0
for j, v in enumerate(list2):
    print(j, v)
j = 0
list3 = list1
list3.extend(list2)
for j, v in enumerate(list3):
    print(j, v)
