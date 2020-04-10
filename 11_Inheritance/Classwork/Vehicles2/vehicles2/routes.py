directions = [
    ['Vinnytsia', 'Nemyriv', 'Haisyn', 'Uman', 'Odesa'],
    ['Vinnytsia', 'Zmerynka', 'Shargorod', 'Mohyliv-Podilskyi', 'Chisinau'],
    ['Vinnytsia', 'Kalynivka', 'Berdychiv', 'Zhytomyr', 'Kyiv', 'Yahotyn', 'Poltava']
]
distances = {
    'Vinnytsia': 0,
    'Nemyriv': 50,
    'Haisyn': 100,
    'Uman': 160,
    'Odesa': 424,
    'Zmerynka': 46,
    'Shargorod': 84,
    'Mohyliv-Podilskyi': 123,
    'Chisinau': 327,
    'Kalynivka': 28,
    'Berdychiv': 87,
    'Zhytomyr': 128,
    'Kyiv': 268,
    'Yahotyn': 467,
    'Poltava': 716
}


def get_route(a, b):
    reverse = False
    route = []
    for item in directions:
        if (a in item) and (b in item):
            if item.index(b) < item.index(a):
                a, b, reverse = b, a, True
            route = list(filter(lambda z: item.index(a) <= item.index(z) <= item.index(b), item))
            if reverse:
                route.reverse()
    if not route:
        route = get_route(a, 'Vinnytsia') + get_route('Vinnytsia', b)[1:]
    return route


def distance(a, b):
    if any([True if (a in item and b in item) else False for item in directions]):
        return abs(distances[a] - distances[b])
    else:
        return distances[a] + distances[b]
