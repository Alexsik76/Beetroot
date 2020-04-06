def intervals(value) :
    min = value - int(value/10)
    max = value + int(value/10)
    return [min, max]
