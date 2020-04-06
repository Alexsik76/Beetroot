from matplotlib import pyplot as plt
from vehicles2 import classes_of_cars


def statistic(data):
    stand_objects = [
        classes_of_cars.PedalBikes(random=False),
        classes_of_cars.MotorBikes(random=False),
        classes_of_cars.PickUps(random=False),
        classes_of_cars.SportCars(random=False),
        classes_of_cars.EstateCars(random=False),
        classes_of_cars.MediumTrucks(random=False),
        classes_of_cars.HeavyTrucks(random=False)
    ]
    list_of_founded = {
        'IN ALL': 0,
        'PedalBikes': 0,
        'MotorBikes': 0,
        'PickUps': 0,
        'SportCars': 0,
        'EstateCars': 0,
        'MediumTrucks': 0,
        'HeavyTrucks': 0
    }
    list_of_power = []
    for line in data:
        list_of_power.append(line[2])
        for item in stand_objects:
            if item.comparison(line):
                list_of_founded['IN ALL'] += 1
                list_of_founded[item.__class__.__name__] += 1
                break
    x = list(list_of_founded.values())[1:]
    s = list(list_of_founded.keys())[1:]
    fig, (ax1, ax2) = plt.subplots(
        nrows=1, ncols=2,
        figsize=(8, 4)
    )

    ax1.pie(x, labels=s, shadow=True, autopct='%1.1f%%')
    ax1.set_title('All vehicles2')
    ax2.scatter(x=range(1000), y=list_of_power, marker='o', c='g', edgecolor='b')
    ax2.set_title('Scatter: Powers of vehicles2')
    ax2.set_xlabel('vehicles2')
    ax2.set_ylabel('power')

    plt.show()
