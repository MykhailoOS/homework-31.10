
# Task1
class Discount:
    def discount(self):
        raise NotImplementedError


class RegularDiscount(Discount):
    def discount(self):
        return 0.9


class SilverDiscount(Discount):
    def discount(self):
        return 0.85


class GoldDiscount(Discount):
    def discount(self):
        return 0.8


class Product:
    def __init__(self, title: str, price: float | int):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price:.2f}'


class Cart:
    def __init__(self, discount: Discount = None):
        self.__products = []
        self.__quantities = []
        self.discount = discount

    def add_product(self, product: Product, quantity: int | float = 1):
        if isinstance(product, Product) and isinstance(quantity, int | float):
            self.__products.append(product)
            self.__quantities.append(quantity)

    def total(self):
        summa = sum(product.price * quantity for product, quantity in zip(self.__products, self.__quantities))
        return summa * self.discount.discount() if self.discount else summa

    def __iadd__(self, other):
        return Cart()
    def __str__(self):
        return '\n'.join(map(lambda items: f'{items[0]} x {items[1]} = {items[0].price * items[1]} UAH',
                          zip(self.__products, self.__quantities))) + f'\nTotal: {self.total():.2f} UAH\n'


pr_1 = Product('banana', 50)
pr_2 = Product('apple', 51)
pr_3 = Product('orange', 52)


cart_1 = Cart()
cart_2 = Cart(SilverDiscount())
cart_1 += cart_2
cart_1.add_product(pr_1)
cart_1.add_product(pr_2)
cart_1.add_product(pr_3)

cart_1.add_product(pr_1, 5)
print(cart_1)




























#Task 3
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
