from __future__ import annotations
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

        return purposes[purpose]
        #
        # if purposes[purpose] <= len(self.flowers):
        #     min_prices = sorted(self.flowers, key=lambda x: x.price)
        #     min_bouquet = list(min_prices[:purposes[purpose]])
        #     max_bouquet = list(min_prices[len(min_prices):-(purposes[purpose] + 1):-1])
        #     if sum([x.price for x in max_bouquet]) * 1.3 <= desirable_price:
        #         bouquet_level = max_bouquet
        #     elif sum([x.price for x in min_bouquet]) * 1.3 <= desirable_price:
        #         bouquet_level = min_bouquet
        #     else:
        #         message = 'We do not have a bouquet at your request.'
        #         print(f'\033[31m{message}\033[0m')
        #         return None
        #
        #     bouquet = Bouquet(self, desirable_price)
        #     self.sold_bouquets.append(bouquet)
        #     print('len: ', len(bouquet_level))
        #     for item in range(len(bouquet_level)):
        #         bouquet.composition.append(bouquet_level.pop())
        #     self.money += bouquet.price()
        #     bouquet.was_sold = True
        #     return bouquet


class Bouquet:
    def __init__(self, shop: Shop, desirable_price: float):
        self.shop = shop
        self.desirable_price = desirable_price
        self.composition = []
        self.price_of_bouquet = self.price()
        self.was_sold = False
        self.main_flower = types_of_flowers['white clove']
        self.min_number = 1

    def price(self):
        price = sum(list([x.price for x in self.composition]))
        return round(price * 1.3, 2)

    def default_create(self):
        sorted_by_prices = sorted(self.shop.flowers, key=lambda x: x.price)
        min_price = sorted_by_prices[0].price
        while self.desirable_price >= min_price:
            self.composition.append(sorted_by_prices.pop(0))
    def create(self):
        need_flowers = list(filter(lambda x: x.name == self.main_flower, self.shop.flowers))
        if need_flowers:
            min_price = need_flowers[0].price * 1.3 * self.min_number
            if min_price <= self.desirable_price:
                number = self.desirable_price // min_price
                if number <= len(need_flowers):
                    return need_flowers[:number + 1]
                else:
                    self.composition = need_flowers
                    self.desirable_price -= sum([list([x.price for x in self.composition])]) * 1.3



    def __str__(self):
        if self.composition:
            string = ', '.join([y.name for y in self.composition])
            return string
        else:
            return 'No flowers'


class BouquetMarriage(Bouquet):
    def __init__(self, shop: Shop, desirable_price: float):
        super().__init__(shop, desirable_price)
        self.main_flower = types_of_flowers['white rose']

class BouquetBirthday(Bouquet):
    def __init__(self, shop: Shop, desirable_price: float):
        super().__init__(shop, desirable_price)
        self.main_flower = types_of_flowers['red rose']

class BouquetFuneral(Bouquet):
    def __init__(self, shop: Shop, desirable_price: float):
        super().__init__(shop, desirable_price)
        self.main_flower = types_of_flowers['red clove']
        self.min_number = 2

class BouquetOther(Bouquet):
    def __init__(self, shop: Shop, desirable_price: float):
        super().__init__(shop, desirable_price)
        self.main_flower = types_of_flowers['rose pink']

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
my_bouquet = kvitka.sale_of_bouquet('other', 400)
print(my_bouquet, my_bouquet.price_of_bouquet, sep='; ')
print()