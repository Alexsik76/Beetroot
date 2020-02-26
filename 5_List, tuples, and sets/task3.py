# Extracting numbers
list1 = []
list2 = []
i = 0
while i < 101:
    list1.append(i)
    if (i % 7 == 0) and (i % 5 != 0):
        list2.append(i)
    i += 1
print(list2)
