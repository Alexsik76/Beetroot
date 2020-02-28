# generating 2 lists with random items
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
# generating list with indexes
list_n = range(10)
# combinating every item from each list with an index
list1_fin = list(map(str, zip(list_n, list1)))
list2_fin = list(map(str, zip(list_n, list2)))
# printing each list
print('\n'.join(list1_fin))
print('\n'.join(list2_fin))
