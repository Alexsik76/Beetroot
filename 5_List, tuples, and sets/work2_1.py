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
list_n = range(10)
list1_fin = list(map(str, zip(list_n, list1)))
list2_fin = list(map(str, zip(list_n, list2)))
print('\n'.join(list1_fin))
print('\n'.join(list2_fin))
