from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="cities.py")


def get_synonyms(city):
    geolocator.view_box = True
    print(dir(geolocator))
    location = geolocator.geocode(city, addressdetails=True, namedetails=True)
    z = location.geojson
    print(z)
    names = location.raw['namedetails']
    print(location.raw['address']['city'])
    print('5555: ', type(location.address[1]))
    langs = {'en', 'uk', 'ru'}
    needed_synonyms = {
        f'{key[-2:]} - {names[key]}' for key in names if key[-2:] in langs
        }
    return location, needed_synonyms


rez = get_synonyms('Дорошенка')
print(rez[0], rez[1], sep='\n')
