# Fraction


class Fraction:
    def __init__(self, numerator: int, denominator: int = 1):
        self.numerator = numerator
        assert denominator != 0, 'denominator mast bee not 0'
        self.denominator = denominator

    def __add__(self, other):
        assert isinstance(other, Fraction), 'The second term of the expression must be an Fraction.object'
        rez_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        rez_denominator = self.denominator * other.denominator
        return reducing(Fraction(rez_numerator, rez_denominator))

    def __sub__(self, other):
        assert isinstance(other, Fraction), 'The second term of the expression must be an Fraction.object'
        other.numerator = -other.numerator
        return self.__add__(other)

    def __mul__(self, other):
        assert isinstance(other, Fraction), 'The second term of the expression must be an Fraction.object'
        rez_numerator = self.numerator * other.numerator
        rez_denominator = self.denominator * other.denominator
        return reducing(Fraction(rez_numerator, rez_denominator))

    def __truediv__(self, other):
        assert isinstance(other, Fraction), 'The second term of the expression must be an Fraction.object'
        if other.numerator != 0:
            other.numerator, other.denominator = other.denominator, other.numerator
            return self.__mul__(other)
        else:
            print('Failed to divide by 0')

    def __str__(self):
        if self.denominator == 1:
            return f'{self.numerator}'
        elif self.numerator == 0:
            return '0'
        else:
            return f'{self.numerator} / {self.denominator}'


def reducing(obj: Fraction):
    a, b = obj.numerator, obj.denominator
    if b < 0:
        a, b, = -a, -b
    if a == 0:
        b = 1
    else:
        max_num = abs(a) if abs(a) > abs(b) else abs(b)
        for i in range(2, max_num + 1):
            while a % i == 0 and b % i == 0:
                a, b, = int(a / i), int(b / i)
    obj.numerator, obj.denominator = a, b
    return obj


x = Fraction(1, 2)
y = Fraction(1, 4)
z = x + y
print(z)
x1 = Fraction(-25, 5)
y1 = Fraction(-1, 32)
z1 = x1 / y1
print(z1)
