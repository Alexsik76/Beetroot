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
# list1_1 = range(10)
# list1_3 = zip(list1_1, list1)
# print(','.join(list1))
list1_1 = list(enumerate(list1))
print(type(list1_1))
print(list1_1)
