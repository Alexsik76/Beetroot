# Phone book
import os
import json
try:
    import readline
except ImportError:
    import pyreadline as readline
# enter a file name end check it
while True:
    name_file = input('Введіть назву файлу телефонної книги:')
    try:
        if name_file == '':
            name_file = 'book3.txt'
        elif name_file[-4:] != '.txt':
            name_file += '.txt'
        with open(name_file) as f:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Розпочато роботу з файлом {name_file}')
            break
    except IOError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Файл "{name_file}" не знайдено. Спробуйте ще')
# creating a new dict, if file is empty
with open(name_file) as f:
    try:
        book = json.load(f)
    except ValueError:
        print('Створюємо новий список')
        book = []
values = {
    'first_name': 'Ім\'я',
    'last_name': 'Прізвище',
    'tel_num': 'Телефон',
    'state': 'Область',
    'city': 'Місто'
}


def add_item(book):
    first_name = input('Введіть ім\'я: ')
    first_name = first_name.strip().title()
    last_name = input('Введіть прізвище: ')
    last_name = last_name.strip().title()
    while True:
        tel_num = input('Введіть номер телефону: ')
        if not tel_num.strip().isnumeric():
            print('Помилка: введений номер містить не лише цифри')
            continue
        elif len(tel_num.strip()) > 10:
            print('Помилка: Довжина номера більше 10')
            continue
        tel_num = tel_num.strip()
        break
    state = input('Введіть область: ')
    state = state.strip().title()
    city = input('Введіть місто: ')
    city = city.strip().title()
    # add entries to book
    book.append({
        'first_name': first_name,
        'last_name': last_name,
        'tel_num': tel_num,
        'state': state,
        'city': city
    })
    with open(name_file, 'w') as f:
        json.dump(book, f)
    print(f'Запис на особу {first_name} {last_name} додано до книги.')


def search_by_value(value, book=book):
    text_value = values[value]
    found_ind = []
    print(f'Пошук за значеням "{text_value}".')
    print(f'Ведіть {text_value}:')
    search_input = input().strip()
    search_results = []
    if value == 'city':
        for i in range(len(book)):
            if (
                book[i]['city'].lower() == search_input.lower()
                or book[i]['state'].lower() == search_input.lower()
            ):
                search_results.append(book[i])
                found_ind.append(i)
    else:
        for i in range(len(book)):
            if book[i][value].lower() == search_input.lower():
                search_results.append(book[i])
                found_ind.append(i)
    sr = search_results
    si = search_input
    print(f'За вашим запитом знайдено записів {len(sr)}, що містять {si}.')
    print_item(search_results)
    return found_ind


def search(book):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Пошук по імені "f"
    Пошук по прізвищу "l"
    Пошук по номеру телефону "n"
    Пошук по області або місту "c"
    Повернутись до меню "e"
    """)
    while True:
        user_input = input(': ')
        if user_input == 'f':
            search_by_value('first_name')
        elif user_input == 'l':
            search_by_value('last_name')
        elif user_input == 'n':
            search_by_value('tel_num')
        elif user_input == 'c':
            search_by_value('city')
        elif user_input == 'e':
            finish()


def print_item(elem):
    for v in values.values():
        print(f'\x1b[1m{v:<15}\x1b[0m', end='')
    print()
    if isinstance(elem, dict):
        for v1 in elem.values():
            print(f'{v1:<15}', end='')
    elif isinstance(elem, list):
        for i in elem:
            for v1 in i.values():
                print(f'{v1:<15}', end='')
            print()


def finish():
    y_n = 'n'
    while y_n == 'n':
        print('Повернутись до меню?')
        s = 'y/n'
        y_n = input(f'\x1b[5;31;40m{s}:\x1b[0m')
        if y_n.strip().lower() == 'y':
            user_menu()
        else:
            y_n = 'n'


def delete_by_tel_number(book):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Пошук та видалення запису за номером телефону')
    found = search_by_value('tel_num', book=book)
    print('Ви бажаєте видалити цей запис?')
    y_n = input('y/n:')
    if y_n.strip().lower() == 'y':
        ind = found[0]
        first_name = book[ind]['first_name']
        last_name = book[ind]['last_name']
        print(f'Запис на особу {first_name} {last_name} видалено з книги.')
        book.remove(book[ind])
        with open(name_file, 'w') as f:
            json.dump(book, f)
    finish()


def update_by_tel_number(book):
    ind = search_by_value('tel_num')
    item_update = book[ind[0]]
    for key, value in item_update.items():
        print(f'Змініть значення "{values[key]}, або натисніть "Enter"')
        s = value
        readline.set_startup_hook(lambda: readline.insert_text(s))
        s = (input(': '))
        item_update[key] = s
    s = ''
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Відредагований запис:')
    print_item(item_update)
    book[ind[0]] = item_update
    with open(name_file, 'w') as f:
        json.dump(book, f)
    finish()


def user_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Додати запис - натисніть "a"
    Пошук - натисніть "s"
    Видалити - натисність "r"
    Змінити запис - натисніть "c"
    Завершити роботу - натисніть "q"
    """)
    while True:
        user_input = input(': ')
        if user_input == 'a':
            add_item(book)
        elif user_input == 's':
            search(book)
        elif user_input == 'r':
            delete_by_tel_number(book)
        elif user_input == 'c':
            update_by_tel_number(book)
        elif user_input == 'q':
            quit()


user_menu()
