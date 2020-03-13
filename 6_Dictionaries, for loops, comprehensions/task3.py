# List comprehension exercise
list1 = []
for i in range(1, 11):
    list1.append({i: i**2})
    print(f'{i:2} -->{i**2:>4}')
print(list1)
