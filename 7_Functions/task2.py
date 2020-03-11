# Creating a dictionary
dictionary = []


def make_country(name, capital):
    dictionary.append({'name': name, 'capital': capital})


make_country('USA', 'New York City')
make_country('Україна', 'Київ')

for i in dictionary:
    print(f"Країна: {(i['name']):10} Столиця: {(i['capital']):10}")
