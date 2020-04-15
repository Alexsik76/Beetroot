# Product Store


class Product:
    def __init__(self, type1, name, price):
        self.type = type1
        self.name = name
        self.price = price


def except_decorator(func):
    def wrapper(self, *args):
        try:
            return func(self, *args)
        except TypeError as alert:
            print(alert)
    return wrapper


class ProductStore:
    def __init__(self):
        self.store = []
        self.money = 0

    @except_decorator
    def add(self, product, amount):
        """
        :arg product: Product.obj
        :arg amount: int
        Adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
        """
        self.store.append(
            {
                'type': product.type,
                'name': product.name,
                'price': product.price + (product.price * 0.3),
                'amount': amount
            })

    def description(self, item):
        string = f"type: {item['type']}, name: {item['name']}, price: {item['price']}, amount:{item['amount']}."
        return string

    @except_decorator
    def set_discount(self, identifier, percent, identifier_type='name'):
        """
        Adds a discount for all products specified by input identifiers (type or name).
        The discount must be specified in percentage.
        """
        for item in self.store:
            if item[identifier_type] == identifier:
                item['price'] = round((item['price'] - item['price'] * percent * 0.01), 2)

    @except_decorator
    def sell_product(self, product_name, amount):
        """
        removes a particular amount of products from the store if available,
        in other case raises an error. It also increments income if the sell_product method succeeds.
        """
        for item in self.store:
            if product_name == item['name'] and item['amount'] >= amount:
                self.money += amount * item['price']
                item['amount'] -= amount
                break
        else:
            print(f'There are no {product_name} in the store.')

    @except_decorator
    def get_income(self):
        """
        returns amount of many earned by ProductStore instance.
        :return: int
        """
        return self.money

    @except_decorator
    def get_all_products(self):
        """
        returns information about all available products in the store.
        :return: str
        """
        return "\n".join(map(self.description, self.store))

    @except_decorator
    def get_product_info(self, product_name):
        """
        returns a tuple with product name and amount of items in the store.
        :param product_name: str
        :return: tuple
        """
        prod = list(filter(lambda x: x['name'] == product_name, self.store))[0]
        thistuple = (prod['name'], prod['amount'])
        return thistuple

    @except_decorator
    def search_product(self, product):
        prod = list(filter(lambda x: x['name'] == product, self.store))[0]
        return prod


bananas = Product('fruits', 'bananas', 30)
apples = Product('fruit', 'apples', 10)
buckwheat = Product('groats', 'buckwheat', 90)
chicken_wings = Product('meet', 'chicken wings', 22)
pork_head = Product('meet', 'pork head', 33)
p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)
print(s.get_product_info('Ramen'))
print(s.get_all_products())
