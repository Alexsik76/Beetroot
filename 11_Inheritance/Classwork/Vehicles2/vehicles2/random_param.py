from random import randint, uniform
from vehicles2 import standard_classes


def intervals(value):
    min_value = value - int(value / 10)
    max_value = value + int(value / 10)
    if isinstance(value, int):
        rez = randint(min_value, max_value)
    else:
        rez = round(uniform(min_value, max_value), 2)
    return rez


def get_param(classes):
    st_params = standard_classes.standard_data[classes]
    rand_param = list(map(intervals, st_params.values()))
    return rand_param
