# Product Store


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


bananas = Product('fruits', 'bananas', 30)
apples = Product('fruit', 'apples', 10)
buckwheat = Product('groats', 'buckwheat', 90)
chicken_wings = Product('meet', 'chicken_wings', 22)
pork_head = Product('meet', 'pork head', 33)


class ProductStore:
    def __init__(self):
        self.store = []

    def except_decorator(self, func):
        try:
            func()
        except TypeError as string:
            print(string)

    @except_decorator
    def add(self, product, amount):
        ''' Adds a specified quantity of a single product with a predefined price premium for your store(30 percent)'''
        self.store.append({
            'type':     product.type,
            'name':     product.name,
            'price':    product.price + (product.price * 0.3),
            'amount':   amount
        })


silmag = ProductStore

silmag.add(bananas, 100)

print(silmag.store)
