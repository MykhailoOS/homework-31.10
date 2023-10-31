import math


class Rational:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __add__(self, other):
        if not isinstance(other, int | float):
            return NotImplementedError()
        if other <= 0:
            return ValueError()

        return Rational(self.a + other, self.b + other)

    def __mul__(self, other):
        if not isinstance(other, int | float):
            return NotImplementedError()
        if other <= 0:
            return ValueError()
        return Rational(self.a * self.a, self.b * self.b)

    def __sub__(self, other):
        if not isinstance(other, int | float):
            return NotImplementedError()
        if other <= 0:
            return ValueError()

        return Rational(self.a - other, self.b - other)

    def __truediv__(self, other):
        if not isinstance(other, int | float):
            return NotImplementedError()
        if other <= 0:
            return ValueError()

        return Rational(self.a // other, self.b // 1)

    def __str__(self):
        tmp = math.gcd(self.a, self.b)
        self.a //= tmp
        self.b //= tmp


        return f'{self.a} / {self.b}'

x = Rational(-4, -2)
mul = x - 4
print(mul)
