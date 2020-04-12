from matplotlib import pyplot as plt
from vehicles2.random_vehicles import matrix_objects


def statistic():
    list_minibus = list(filter(lambda x: x.__class__.__name__ == 'Minibus', matrix_objects))
    list_medium_trucks = list(filter(lambda x: x.__class__.__name__ == 'MediumTrucks', matrix_objects))
    list_heavy_trucks = list(filter(lambda x: x.__class__.__name__ == 'HeavyTrucks', matrix_objects))
    list_capacity = []
    list_payment = []
    list_of_names = ['Minibus', 'MediumTrucks', 'HeavyTrucks']
    sum_capacity = 0
    sum_payment = 0
    for vehicle in list_minibus:
        sum_capacity += sum([x.capacity for x in vehicle.cargo_finished])
        sum_payment += sum([x.payment for x in vehicle.cargo_finished])
    list_payment.append(sum_payment)
    list_capacity.append(sum_capacity)
    sum_capacity = 0
    sum_payment = 0
    for vehicle in list_medium_trucks:
        sum_capacity += sum([x.capacity for x in vehicle.cargo_finished])
        sum_payment += sum([x.payment for x in vehicle.cargo_finished])
    list_payment.append(sum_payment)
    list_capacity.append(sum_capacity)
    sum_capacity = 0
    sum_payment = 0
    for vehicle in list_heavy_trucks:
        sum_capacity += sum([x.capacity for x in vehicle.cargo_finished])
        sum_payment += sum([x.payment for x in vehicle.cargo_finished])
    list_payment.append(sum_payment)
    list_capacity.append(sum_capacity)
    x = list_capacity
    x2 = list_payment
    s = list_of_names
    fig, (ax1, ax2) = plt.subplots(
        nrows=1, ncols=2,
        figsize=(8, 4)
    )

    ax1.pie(x, labels=s, shadow=True, autopct='%1.1f%%')
    ax1.set_title('Capacity by vehicles')
    ax2.pie(x2, labels=s, shadow=True, autopct='%1.1f%%')
    ax2.set_title('Payment by vehicles')

    plt.show()
