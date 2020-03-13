larder = {
            'bananas': [],
            'mangoes': [],
            'apples': [],
            'potatoes': [],
            'wheat': []
            }
date_of_harvests = [90, 110, 120, 130, 140]
harvest = dict(zip(larder.keys(), date_of_harvests))
print(harvest)
if 110 in harvest.values():
    print(harvest.values(), True)
print(harvest)
print(harvest.keys())
print(harvest.values())
print(type(harvest))
for x, y in harvest.items():
    print(' ', x, y, sep='\t')
harvest['meet'] = 10
print(harvest)
