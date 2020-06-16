from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="cities.py")


def get_synonyms(city):
    location = geolocator.geocode(city, namedetails=True)
    names = location.raw['namedetails']
    langs = {'en', 'uk', 'ru'}
    needed_synonyms = {
        f'{key[-2:]} - {names[key]}' for key in names if key[-2:] in langs
        }
    return location, needed_synonyms


rez = get_synonyms('Vinnitsa')
print(rez[0], rez[1], sep='\n')
