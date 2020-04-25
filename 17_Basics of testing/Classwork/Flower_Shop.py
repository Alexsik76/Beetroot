class Flower:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Shop:
    def __init__(self):
        self.flowers = []
        self.money = 100_000
        self.sold_bouquets = []

    def purchase_of_flowers(self, flower: str, number: int) -> None:
        price_of_transaction = number * types_of_flowers[flower]
        if flower in types_of_flowers.keys() and \
                price_of_transaction <= self.money:
            self.money -= price_of_transaction
            flower_price = types_of_flowers[flower] * 1.1
            for j in range(number):
                self.flowers.append(Flower(flower, flower_price))

    def sale_of_bouquet(self, purpose: str, desirable_price: float):
        purposes = {
            'marriage': 33,
            'birthday': 15,
            'funeral': 10,
            'other': 5
        }
        if purpose not in purposes:
            purpose = 'other'
        if purposes[purpose] <= len(self.flowers):
            min_prices = sorted(self.flowers, key=lambda x: x.price)
            min_bouquet = list(min_prices[:purposes[purpose] + 1])
            max_bouquet = list(min_prices[len(min_prices):-(purposes[purpose] + 1):-1])
            if sum([x.price for x in max_bouquet]) <= desirable_price:
                self.sold_bouquets.append(Bouquet())
                self.sold_bouquets[-1].composition = max_bouquet.copy()
                self.money += self.sold_bouquets[-1].price()
                self.sold_bouquets[-1].was_sold = True
                return self.sold_bouquets[-1]
            elif sum([x.price for x in min_bouquet]) <= desirable_price:
                self.sold_bouquets.append(Bouquet())
                self.sold_bouquets[-1].composition = min_bouquet.copy()
                self.money += self.sold_bouquets[-1].price()
                self.sold_bouquets[-1].was_sold = True
                return self.sold_bouquets[-1]
            else:
                message = 'We do not have a bouquet at your request.'
                print(f'\033[31m{message}\033[0m')


kvitka = Shop()


class Bouquet:
    def __init__(self, shop: Shop = kvitka):
        self.composition = []
        self.shop = shop
        self.price_of_bouquet = 0
        self.was_sold = False

    def price(self):
        price = sum(list([x.price for x in self.composition]))
        self.price_of_bouquet = round(price, 2)
        return price

    def __str__(self):
        string = ', '.join([y.name for y in self.composition])
        return string

types_of_flowers = {
    'red rose': 50,
    'white rose': 45,
    'rose pink': 47,
    'red clove': 35,
    'white clove': 33
}

for i in types_of_flowers:
    kvitka.purchase_of_flowers(i, 100)
print('kvitka.money', kvitka.money)
my_bouquet = kvitka.sale_of_bouquet('other', 400)
print(my_bouquet, my_bouquet.price_of_bouquet, sep='; ')
print('kvitka.money', kvitka.money)
