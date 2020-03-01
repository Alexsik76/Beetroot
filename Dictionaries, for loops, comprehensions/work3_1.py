a = 'apple'
k = 'kiwi'
g = 'grapes'
print(a)
print(k)
print(g)
print(a, k, g, sep=', ')
# checking
list_of_fruits = [a, k, g]
user_input = input('Input a fruit: ')
print(user_input in list_of_fruits)
# creating list of persons
list_of_persons = ['Alex', 'Vova', 'Serg']
# checking for replays
list_of_fruits.append('apple')
for item in list_of_fruits:
    replays = list_of_fruits.count(item)
    if replays > 1:
        print(f'The {item} is repeated {replays} times')
    print('There are no replays')
for item in list_of_persons:
    replays = list_of_persons.count(item)
    if replays > 1:
        print(f'The {item} is repeated {replays} times')
    print('There are no replays')
# creating dictionares whith persons and fruits
dict_all = {}
list_of_persons_temp = list_of_persons.copy()
for item in list_of_fruits:
    if list_of_persons_temp:
        dict_all[list_of_persons_temp.pop()] = item
    else:
        break
print(dict_all)
# creating dictionares for every person and every fruits
for item in list_of_persons:
    item = {'have_fruits': '', 'money': 100}
for item in list_of_fruits:
    item = {'price': 0, 'numbers': 10}
# ended in classroom
