import requests
import sys
from geopy.geocoders import Nominatim

url = 'https://api.openweathermap.org/data/2.5/weather?'
geolocator = Nominatim(user_agent="task3_2.py")
langs = {'en', 'uk', 'ru'}
key_to_exit = {'q', 'Q', 'й', 'Й', ' ', ''}
api_key = '5dc158e8a8dde73cdcfe9ac5c03d6a23'


def get_user_input() -> str:
    city = input('Input location, or type "q" to exit: ')
    if city in key_to_exit:
        sys.exit()
    return city


def get_synonyms(city: str) -> set:
    """Get synonyms of user's input city,
    if not found, repeat input

    Args:
        city (str): user input city

    Returns:
        location(str): detail of city;
        needed_synonyms(set): set of synonyms by [langs]
    """
    while True:
        try:
            location = geolocator.geocode(city, namedetails=True)
            names = location.raw['namedetails']
            needed_synonyms = {
                f'{key[-2:]}: {names[key]}' for key in names
                if key[-2:] in langs
            }
        except AttributeError:
            print(f'GeoPy did not find the city {city}.')
            city = get_user_input()
            continue
        return location, needed_synonyms


def get_weather(api_key: str, location: str) -> dict:
    param_of_request = f'q={location}&units=metric&appid={api_key}'
    r = requests.get(f'{url}{param_of_request}')
    return r.json()


def main():
    while True:
        user_sity = get_user_input()
        location, synonyms = get_synonyms(user_sity)
        weather = get_weather(api_key, location)
        if weather['cod'] == 200:
            print(f'GeoPy found the city: {location},')
            print('also known as: ', *synonyms, sep='\n')
            print('The weather in this city is:')
            print(' temp: ', weather['main']['temp'],
                  '\n', 'humidity: ', weather['main']['humidity'],
                  '\n', 'pressure: ', weather['main']['pressure'],
                  '\n right now.')
            break
        else:
            print(weather['message'], end='.\n')
            print(f'But found: {location}')
            continue


if __name__ == '__main__':
    main()
