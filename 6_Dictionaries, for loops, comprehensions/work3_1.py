from random import randint
a = 'apple'
k = 'kiwi'
g = 'grapes'
print(a)
print(k)
print(g)
print(a, k, g, sep=', ')
# checking
list_of_fruits = [a, k, g]
# user_input = input('Input a fruit: ')
# print(user_input in list_of_fruits)
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
dict_all_person = {}
dict_all_fruits = {}
for item in list_of_persons:
    dict_all_person[item] = {
                            'have_fruits': {},
                            'money': 100,
                            'fruits_needed': {}
                            }
for item in list_of_fruits:
    dict_all_fruits[item] = {
                            'price': 0,
                            'numbers': 10
                            }
# ended in classroom
print(type(dict_all_person))
print(dict_all_person)
print(type(dict_all_fruits))
print(dict_all_fruits)
# generating random prices for the every fruits
for item in dict_all_fruits:
    dict_all_fruits[item]['price'] = randint(1, 10)
print(dict_all_fruits)
# generating random wish of fruits for the every person
for person in dict_all_person:
    for fruit in dict_all_fruits:
        dict_all_person[person]['fruits_needed'][fruit] = randint(0, 10)
        dict_all_person[person]['have_fruits'][fruit] = 0
d_items = dict_all_person.items()
print('Dictionares of persons whith their wish of fruits', '\n')
print(*d_items, sep='\n')
# shopping
#
# 1. detect minimal prices
prices = []
for item in dict_all_fruits:
    prices.append(dict_all_fruits[item]['price'])
min_price = min(prices)
print('\n', 'Minimal prices is: ', min_price)
# 2. shop fruits every person
for person in dict_all_person:
    if dict_all_person[person]['money'] >= min_price:
        for fruit in dict_all_fruits:
            i_have = dict_all_person[person]['have_fruits'][fruit]
            i_wont = dict_all_person[person]['fruits_needed'][fruit]
            my_money = dict_all_person[person]['money']
            price = dict_all_fruits[fruit]['price']
            in_stock = dict_all_fruits[fruit]['numbers']
            while i_wont > 0 and in_stock > 0 and price <= my_money:
                dict_all_person[person]['have_fruits'][fruit] += 1
                dict_all_person[person]['fruits_needed'][fruit] -= 1
                dict_all_person[person]['money'] -= price
                dict_all_fruits[fruit]['numbers'] -= 1
                i_have = dict_all_person[person]['have_fruits'][fruit]
                i_wont = dict_all_person[person]['fruits_needed'][fruit]
                my_money = dict_all_person[person]['money']
                in_stock = dict_all_fruits[fruit]['numbers']
# 3. print results
d_items = dict_all_person.items()
print('\n', 'Dictionares of persons whith their wish of fruits', '\n')
print(*d_items, sep='\n')
