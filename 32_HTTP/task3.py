import requests
import sys


def get_location():
    location = input('Input location: ')
    return location


def get_weather(api_key, location):
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    param_of_request = f'q={location}&units=metric&appid={api_key}'
    r = requests.get(f'{url}{param_of_request}')
    return r.json()


def main():
    key_to_exit = {'q', 'Q', 'й', 'Й', ' ', ''}
    location = get_location()
    while True:
        if location in key_to_exit:
            break
            sys.exit()
        # api_key = get_api_key()
        print(location)
        weather = get_weather('5dc158e8a8dde73cdcfe9ac5c03d6a23', location)
        if weather['cod'] == 200:
            print(weather['main']['temp'], weather['cod'])
            print(weather)
            break
        else:
            print(weather['message'])
            location = get_location()


if __name__ == '__main__':
    main()
