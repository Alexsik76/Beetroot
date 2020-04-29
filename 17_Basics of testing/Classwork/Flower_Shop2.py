from __future__ import annotations
from functools import wraps
from random import randint


class Flower:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Shop:
    def __init__(self):
        self.flowers = []
        self.sorted_flowers = sorted(self.flowers, key=lambda x: x.price)
        self.money: float = 100_000.00
        self.sold_bouquets = []

    def purchase_of_flowers(self, flower: str, number: int) -> None:
        price_of_transaction = number * types_of_flowers[flower]
        if flower in types_of_flowers.keys() and \
                price_of_transaction <= self.money:
            self.money -= price_of_transaction
            flower_price = types_of_flowers[flower] * 1.1
            for j in range(number):
                self.flowers.append(Flower(flower, flower_price))

    def sale_of_bouquet(self, purpose: str, desirable_price: float) -> Bouquet:
        purposes = {
            'marriage': BouquetMarriage(self, desirable_price),
            'birthday': BouquetBirthday(self, desirable_price),
            'funeral': BouquetFuneral(self, desirable_price),
            'other': BouquetOther(self, desirable_price)
        }
        if purpose not in purposes:
            purpose = 'other'
        bouquet = purposes[purpose]
        self.sold_bouquets.append(bouquet)
        self.money += bouquet.price()
        for item in bouquet.composition:
            self.flowers.remove(item)
        return bouquet


def correct_number(f):
    @wraps(f)
    def wrapper(self):
        if self.__class__.__name__ == 'BouquetFuneral':
            even = True
        else:
            even = False
        rez = f(self)
        if (even and (len(rez) % 2) == 0) or (not even and (len(rez) % 2) != 0):
            return rez
        else:
            rez.pop()
            return rez

    return wrapper


class Bouquet:
    def __init__(self, shop: Shop, desirable_price: float):
        self.shop = shop
        self.main_flower = 'white clove'
        self.min_number = 1
        self.desirable_price = desirable_price
        self.composition = self.create()
        self.price_of_bouquet = self.price()
        self.was_sold = False

    def price(self):
        price = sum(list([x.price for x in self.composition]))
        return round(price, 2)

    def default_create(self, money):
        composition = []
        sorted_by_prices = sorted(self.shop.flowers, key=lambda x: x.price)
        min_price = sorted_by_prices[0].price
        while money >= min_price:
            composition.append(sorted_by_prices.pop(0))
            money -= sorted_by_prices[0].price
        return composition

    @correct_number
    def create(self):
        need_flowers = list(filter(lambda x: x.name == self.main_flower, self.shop.flowers))
        if need_flowers:
            min_price = need_flowers[0].price * self.min_number
            if min_price <= self.desirable_price:
                number = int(self.desirable_price // min_price)
                if number <= len(need_flowers):
                    return need_flowers[:number]
                else:
                    temp_composition = need_flowers
                    temp_price = self.desirable_price - sum([list([x.price for x in self.composition])])
                    temp_composition.extend(self.default_create(temp_price))
                    return temp_composition
            else:
                return self.default_create(self.desirable_price)
        else:
            return self.default_create(self.desirable_price)

    def __str__(self):
        if self.composition:
            string = f"Bouquet for {self.__class__.__name__[7:]}.\n" \
                     f"Composition: {', '.join([y.name for y in self.composition])}," \
                     f"\nNumber of flowers: {len(self.composition)},\nPrice: {self.price_of_bouquet}."
            return string
        else:
            return 'No flowers'


class BouquetMarriage(Bouquet):
    def __init__(self, shop: Shop, desirable_price: float):
        super().__init__(shop, desirable_price)
        self.main_flower = 'white rose'
        self.composition = self.create()
        self.price_of_bouquet = self.price()


class BouquetBirthday(Bouquet):
    def __init__(self, shop: Shop, desirable_price: float):
        super().__init__(shop, desirable_price)
        self.main_flower = 'red rose'
        self.composition = self.create()
        self.price_of_bouquet = self.price()


class BouquetFuneral(Bouquet):
    def __init__(self, shop: Shop, desirable_price: float):
        super().__init__(shop, desirable_price)
        self.main_flower = 'red clove'
        self.min_number = 2
        self.composition = self.create()
        self.price_of_bouquet = self.price()


class BouquetOther(Bouquet):
    def __init__(self, shop: Shop, desirable_price: float):
        super().__init__(shop, desirable_price)
        self.main_flower = 'rose pink'
        self.composition = self.create()
        self.price_of_bouquet = self.price()


types_of_flowers = {
    'red rose': 50,
    'white rose': 45,
    'rose pink': 47,
    'red clove': 20,
    'white clove': 15
}

kvitka = Shop()
for i in types_of_flowers:
    kvitka.purchase_of_flowers(i, 100)

purp = [
    'marriage',
    'birthday',
    'funeral',
    'other']

for key in purp:
    temp_money = randint(50, 500)
    my_bouquet = kvitka.sale_of_bouquet(key, temp_money)
    print('money: ', temp_money, '\n', my_bouquet, end='\n\n')
