# Mathematician
import calendar


class Mathematician:

    def square_nums(self, arg):
        return list(map(lambda x: x**2, arg))

    def remove_positives(self, arg):
        return list(filter(lambda x: x < 0, arg))

    def filter_leaps(self, arg):
        return list(filter(calendar.isleap, arg))


m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
