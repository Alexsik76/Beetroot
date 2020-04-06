def standard_vehicles():
    standard_data = {
        'PedalBikes': {
            'wheels': 2,
            'speed': 25,
            'power': 0,
            'load_capacity': 5,
            'capacity_of_people': 0,
            'fuel_costs': 0
        },
        'MotorBikes': {  # Honda CB 250 Hornet
            'wheels': 2,
            'speed': 80,
            'power': 50,
            'load_capacity': 30,
            'capacity_of_people': 0,
            'fuel_costs': 5.9
        },
        'Minibus': {  # Bogdan А09202
            'wheels': 4,
            'speed': 75,
            'power': 121,
            'load_capacity': 3230,
            'capacity_of_people': 43,
            'fuel_costs': 15
        },
        'SportCars': {  # Lamborghini Diablo
            'wheels': 4,
            'speed': 323,
            'power': 492,
            'load_capacity': 200,
            'capacity_of_people': 1,
            'fuel_costs': 20.52
        },
        'EstateCars': {  # Mercedes-Benz S-Class S 560
            'wheels': 4,
            'speed': 250,
            'power': 469,
            'load_capacity': 475,
            'capacity_of_people': 4,
            'fuel_costs': 9

        },
        'MediumTrucks': {  # Mercedes-Benz Sprinter 316 CDI L4H2
            'wheels': 4,
            'speed': 250,
            'power': 163,
            'load_capacity': 3500,
            'capacity_of_people': 3,
            'fuel_costs': 7.9

        },
        'HeavyTrucks': {  # MAN TGX 18.440
            'wheels': 6,
            'speed': 110,
            'power': 400,
            'load_capacity': 18000,
            'capacity_of_people': 2,
            'fuel_costs': 20.6
        }
    }
    matrix = [['name', 'wheels', 'speed', 'power', 'load_capacity', 'capacity_of_people', 'fuel_costs']]
    for key, value in standard_data.items():
        s = f"{key},{value['wheels']},{value['speed']},{value['power']}," \
            f"{value['load_capacity']},{value['capacity_of_people']},{value['fuel_costs']}"
        matrix.append(s.split(','))
    return matrix
